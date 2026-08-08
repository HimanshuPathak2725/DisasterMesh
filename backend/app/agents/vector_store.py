"""
Vector Store — Phase 2.

Uses LangChain's QdrantVectorStore wrapper so both the embedding model
and the vector store share the same LangChain interface.

Architecture:
  EmbeddingService  (langchain-huggingface)  ─┐
                                               ├─► VectorStore (langchain-qdrant)
  QdrantVectorStore (langchain-qdrant)       ─┘

Collection: "proto_incidents"
  - Vector size  : 384 (all-MiniLM-L6-v2)
  - Distance     : Cosine
  - Metadata keys: proto_id, source, lat, lon, timestamp_epoch, text, language

Geo strategy:
  LangChain's QdrantVectorStore supports metadata filtering.
  For geo radius queries we pull candidates and apply Haversine post-filtering
  in Python (correct + fast for demo scale, easy to upgrade to native Qdrant
  geo index later).
"""

from __future__ import annotations

import logging
import math
from datetime import UTC, datetime
from typing import Any

from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.models import Distance, VectorParams

from app.agents.embeddings import EmbeddingService, get_embedding_service
from app.schemas import ProtoIncident, VerifiedIncident

logger = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────────

COLLECTION_NAME = "proto_incidents"
VECTOR_SIZE = 384
EARTH_RADIUS_M = 6_371_000.0


# ── Helpers ───────────────────────────────────────────────────────────────────


def _haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance in metres between two lat/lon points."""
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * math.asin(math.sqrt(a)) * EARTH_RADIUS_M


def _uuid_to_int(uid: str) -> int:
    """Convert a UUID string to an integer suitable as a Qdrant point ID."""
    import uuid

    return uuid.UUID(uid).int % (2**63)


def _proto_to_document(proto: ProtoIncident) -> Document:
    """
    Convert a ProtoIncident to a LangChain Document.

    page_content  = the text used for embedding (set by EmbeddingService)
    metadata      = all payload fields stored in Qdrant alongside the vector
    """
    content = proto.text
    if proto.lat is not None and proto.lon is not None:
        content = f"{proto.text} near {proto.lat:.4f},{proto.lon:.4f}"

    metadata: dict[str, Any] = {
        "proto_id": proto.id,
        "source": proto.source.value if hasattr(proto.source, "value") else str(proto.source),
        "lat": proto.lat,
        "lon": proto.lon,
        "timestamp_epoch": proto.timestamp.timestamp(),
        "text": proto.text,
        "language": proto.metadata.get("language", "en"),
        "address": proto.address,
    }
    return Document(page_content=content, metadata=metadata)


# ── VectorStore ───────────────────────────────────────────────────────────────


class VectorStore:
    """
    LangChain-based vector store backed by Qdrant.

    Wraps QdrantVectorStore for upsert / similarity search and adds:
    - Geo+time radius search with Haversine post-filtering
    - proto_id lookup helper
    - Collection size helper
    """

    def __init__(
        self,
        qdrant_client: QdrantClient,
        embedding_service: EmbeddingService | None = None,
    ) -> None:
        self._raw_client = qdrant_client
        self._embeddings = embedding_service or get_embedding_service()
        # QdrantVectorStore is initialised after ensure_collection() is called
        self._lc_store: QdrantVectorStore | None = None

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    async def ensure_collection(self) -> None:
        """
        Create the Qdrant collection if it doesn't exist, then bind
        the LangChain QdrantVectorStore to it.

        Idempotent — safe to call on every startup.
        """
        try:
            self._raw_client.get_collection(COLLECTION_NAME)
            logger.info("Qdrant collection %r already exists", COLLECTION_NAME)
        except (UnexpectedResponse, Exception):
            logger.info("Creating Qdrant collection %r …", COLLECTION_NAME)
            self._raw_client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,
                    distance=Distance.COSINE,
                ),
            )
            logger.info(
                "Created Qdrant collection %r — dim=%d cosine",
                COLLECTION_NAME,
                VECTOR_SIZE,
            )

        # Bind LangChain store to the (now-existing) collection
        self._lc_store = QdrantVectorStore(
            client=self._raw_client,
            collection_name=COLLECTION_NAME,
            embedding=self._embeddings._lc,  # LangChain Embeddings object
        )
        logger.info("QdrantVectorStore bound to %r", COLLECTION_NAME)

    @property
    def _store(self) -> QdrantVectorStore:
        if self._lc_store is None:
            raise RuntimeError("VectorStore not ready. Call ensure_collection() first.")
        return self._lc_store

    # ── Write ─────────────────────────────────────────────────────────────────

    async def upsert(self, proto: ProtoIncident, vector: list[float]) -> None:
        """
        Store a ProtoIncident and its pre-computed embedding in Qdrant.
        """
        import asyncio

        from qdrant_client.models import PointStruct

        doc = _proto_to_document(proto)
        point_id = _uuid_to_int(proto.id)
        # Store page_content in metadata too for search compatibility
        payload = dict(doc.metadata)
        payload["page_content"] = doc.page_content

        point = PointStruct(id=point_id, vector=vector, payload=payload)

        await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: self._raw_client.upsert(
                collection_name=COLLECTION_NAME,
                points=[point],
            ),
        )
        logger.debug("Upserted proto_id=%s point_id=%d to Qdrant", proto.id, point_id)

    # ── Read ──────────────────────────────────────────────────────────────────

    async def search_similar(
        self,
        query_text: str,
        limit: int = 10,
        min_score: float = 0.0,
    ) -> list[tuple[Document, float]]:
        """
        Semantic similarity search using LangChain interface.

        Returns list of (Document, score) tuples, score ∈ [0, 1].
        Used for: "find incidents similar to this query text."
        """
        import asyncio

        results: list[tuple[Document, float]] = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: self._store.similarity_search_with_score(
                query=query_text,
                k=limit,
            ),
        )
        return [(doc, score) for doc, score in results if score >= min_score]

    async def search_nearby(
        self,
        lat: float,
        lon: float,
        radius_m: float = 150.0,
        time_window_s: float | None = None,
        query_text: str | None = None,
        limit: int = 50,
        with_vectors: bool = False,
    ) -> list[dict[str, Any]] | list[tuple[dict[str, Any], list[float]]]:
        """
        Find ProtoIncident payloads (and optional vectors) within geo radius + optional time window.

        Strategy:
          1. Pull broad candidates via semantic search (if query_text given)
             or scroll the full collection.
          2. Haversine post-filter to radius_m.
          3. Optionally filter by time_window_s (recency).

        Returns payload dicts (or (payload, vector) tuples if with_vectors=True)
        sorted by distance ascending.
        Used by Phase 3 VerificationAgent for dedup clustering.
        """
        import asyncio

        # Step 1: Broad candidate retrieval
        if query_text:
            raw: list[Document] = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self._store.similarity_search(query_text, k=limit * 10),
            )
            if with_vectors:
                proto_ids = [
                    doc.metadata.get("proto_id")
                    for doc in raw
                    if doc.metadata.get("proto_id")
                ]
                candidates_with_vec = await self.get_vectors_by_filter(
                    proto_ids, limit=limit * 10
                )
            else:
                candidates = [doc.metadata for doc in raw]
        else:
            # Scroll via raw Qdrant client
            scroll_result = self._raw_client.scroll(
                collection_name=COLLECTION_NAME,
                limit=limit * 10,
                with_payload=True,
                with_vectors=with_vectors,
            )
            if with_vectors:
                candidates_with_vec = []
                for p in scroll_result[0]:
                    if p.payload and p.vector is not None:
                        vec = (
                            p.vector
                            if isinstance(p.vector, list)
                            else list(p.vector.values())[0]
                        )
                        candidates_with_vec.append((p.payload, vec))
            else:
                candidates = [p.payload for p in scroll_result[0] if p.payload]

        if with_vectors:
            nearby_vec: list[tuple[float, dict[str, Any], list[float]]] = []
            for payload, vec in candidates_with_vec:
                p_lat = payload.get("lat")
                p_lon = payload.get("lon")
                if p_lat is None or p_lon is None:
                    continue
                dist = _haversine_m(lat, lon, float(p_lat), float(p_lon))
                if dist <= radius_m:
                    nearby_vec.append((dist, payload, vec))

            if time_window_s is not None:
                now_epoch = datetime.now(UTC).timestamp()
                nearby_vec = [
                    (d, p, v)
                    for d, p, v in nearby_vec
                    if p.get("timestamp_epoch") is not None
                    and (now_epoch - p["timestamp_epoch"]) <= time_window_s
                ]

            nearby_vec.sort(key=lambda x: x[0])
            return [(p, v) for _, p, v in nearby_vec[:limit]]
        else:
            nearby: list[tuple[float, dict[str, Any]]] = []
            for payload in candidates:
                p_lat = payload.get("lat")
                p_lon = payload.get("lon")
                if p_lat is None or p_lon is None:
                    continue
                dist = _haversine_m(lat, lon, float(p_lat), float(p_lon))
                if dist <= radius_m:
                    nearby.append((dist, payload))

            if time_window_s is not None:
                now_epoch = datetime.now(UTC).timestamp()
                nearby = [
                    (d, p)
                    for d, p in nearby
                    if p.get("timestamp_epoch") is not None
                    and (now_epoch - p["timestamp_epoch"]) <= time_window_s
                ]

            nearby.sort(key=lambda x: x[0])
            return [p for _, p in nearby[:limit]]

    async def get_by_proto_id(self, proto_id: str) -> dict[str, Any] | None:
        """Fetch a payload by proto_id."""
        import asyncio

        def _do_get():
            try:
                pid = _uuid_to_int(proto_id)
            except ValueError:
                return None

            try:
                records = self._raw_client.retrieve(
                    collection_name=COLLECTION_NAME,
                    ids=[pid],
                    with_payload=True,
                    with_vectors=False,
                )
                if records and records[0].payload:
                    return records[0].payload
            except Exception:
                pass

            # Fallback to scroll search by payload field
            from qdrant_client.models import FieldCondition, Filter, MatchValue

            try:
                results = self._raw_client.scroll(
                    collection_name=COLLECTION_NAME,
                    scroll_filter=Filter(
                        must=[FieldCondition(key="proto_id", match=MatchValue(value=proto_id))]
                    ),
                    limit=1,
                    with_payload=True,
                    with_vectors=False,
                )
                points = results[0]
                if points and points[0].payload:
                    return points[0].payload
            except Exception:
                pass

            return None

        return await asyncio.get_event_loop().run_in_executor(None, _do_get)

    async def get_by_cluster_id(self, cluster_id: str) -> dict[str, Any] | None:
        """
        Return the payload dict for the *verified* point with the given cluster_id.

        Attempts direct retrieval by point_id (derived from cluster_id) first,
        falling back to a scroll search by payload field.
        """
        import asyncio as _asyncio
        import uuid

        def _do_get():
            # 1. Direct point lookup by ID derived from cluster_id
            raw_id = cluster_id.removeprefix("cluster_")
            try:
                point_id = uuid.UUID(raw_id).int % (2**63)
            except ValueError:
                point_id = abs(hash(cluster_id)) % (2**63)

            try:
                records = self._raw_client.retrieve(
                    collection_name=COLLECTION_NAME,
                    ids=[point_id],
                    with_payload=True,
                    with_vectors=False,
                )
                if records and records[0].payload:
                    return records[0].payload
            except Exception:
                pass

            # 2. Fallback: scroll search by cluster_id payload field
            from qdrant_client.models import FieldCondition, Filter, MatchValue

            try:
                results = self._raw_client.scroll(
                    collection_name=COLLECTION_NAME,
                    scroll_filter=Filter(
                        must=[
                            FieldCondition(
                                key="cluster_id", match=MatchValue(value=cluster_id)
                            ),
                        ]
                    ),
                    limit=1,
                    with_payload=True,
                    with_vectors=False,
                )
                points = results[0]
                if points and points[0].payload:
                    return points[0].payload
            except Exception:
                pass

            return None

        return await _asyncio.get_event_loop().run_in_executor(None, _do_get)



    async def collection_size(self) -> int:
        """Return the total number of points in the collection."""
        info = self._raw_client.get_collection(COLLECTION_NAME)
        return info.points_count or 0

    async def get_vectors_by_filter(
        self,
        proto_ids: list[str],
        limit: int = 50,
    ) -> list[tuple[dict[str, Any], list[float]]]:
        """
        Return ``(payload, vector)`` for every point whose ``proto_id`` payload
        field is in *proto_ids*.

        Used by :class:`~app.agents.verification.VerificationAgent` to retrieve
        the ground-truth stored embedding vectors for nearby candidates so that
        cosine similarity can be computed without re-embedding the candidate
        texts (Option B from the Phase 3 design).

        Parameters
        ----------
        proto_ids:
            List of ``proto_id`` values (UUID strings) to fetch.
        limit:
            Maximum number of points returned.

        Returns
        -------
        List of ``(payload_dict, vector)`` tuples in arbitrary order.
        Only points that actually exist in Qdrant are returned — missing
        IDs are silently skipped.
        """
        import asyncio

        from qdrant_client.models import FieldCondition, Filter, MatchAny

        def _do_fetch() -> list[tuple[dict[str, Any], list[float]]]:
            results: list[tuple[dict[str, Any], list[float]]] = []
            if not proto_ids:
                return results

            scroll_filter = Filter(
                must=[
                    FieldCondition(
                        key="proto_id",
                        match=MatchAny(any=proto_ids),
                    )
                ]
            )
            try:
                points, _ = self._raw_client.scroll(
                    collection_name=COLLECTION_NAME,
                    scroll_filter=scroll_filter,
                    limit=limit,
                    with_payload=True,
                    with_vectors=True,
                )
                for p in points:
                    if p.payload and p.vector is not None:
                        vec = (
                            p.vector
                            if isinstance(p.vector, list)
                            else list(p.vector.values())[0]  # named-vector layout
                        )
                        results.append((p.payload, vec))
            except Exception as exc:  # pragma: no cover
                logger.warning("get_vectors_by_filter failed: %s", exc)
            return results

        return await asyncio.get_event_loop().run_in_executor(None, _do_fetch)

    async def upsert_verified(
        self,
        verified: VerifiedIncident,
        vector: list[float],
    ) -> None:
        """
        Persist a :class:`~app.schemas.VerifiedIncident` back into the Qdrant
        collection so that future incoming proto-incidents can discover and join
        this cluster.

        The point is tagged ``point_type="verified"`` in its payload to
        distinguish it from raw ``ProtoIncident`` points
        (``point_type="proto"``).

        Uses the ``cluster_id`` UUID fragment as the point ID so that
        successive upserts for the same cluster overwrite the previous
        verified snapshot rather than creating duplicates.
        """
        import asyncio
        import uuid

        from qdrant_client.models import PointStruct

        # Derive a stable integer point ID from the cluster_id string.
        # cluster_id has the form "cluster_<uuid4>"; strip the prefix.
        raw_id = verified.cluster_id.removeprefix("cluster_")
        try:
            point_id = uuid.UUID(raw_id).int % (2**63)
        except ValueError:
            # Fallback: hash the full string if it doesn't parse as UUID.
            point_id = abs(hash(verified.cluster_id)) % (2**63)

        payload: dict[str, Any] = {
            "point_type": "verified",
            "cluster_id": verified.cluster_id,
            "source_provenance": [
                s.value if hasattr(s, "value") else str(s)
                for s in verified.source_provenance
            ],
            "lat": verified.lat,
            "lon": verified.lon,
            "timestamp_epoch": verified.timestamp.timestamp(),
            "confidence": verified.confidence,
            "severity": str(verified.severity),
            "status": str(verified.status),
        }

        point = PointStruct(id=point_id, vector=vector, payload=payload)

        await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: self._raw_client.upsert(
                collection_name=COLLECTION_NAME,
                points=[point],
            ),
        )
        logger.debug(
            "Upserted verified cluster_id=%s point_id=%d to Qdrant",
            verified.cluster_id,
            point_id,
        )

    async def get_incident(self, cluster_id: str) -> dict[str, Any] | None:
        """
        Return the payload dict for a verified incident cluster.

        Thin alias for :meth:`get_by_cluster_id` — provides a clean, stable
        name for callers that only need incident lookup (e.g. the Communication
        router).

        Parameters
        ----------
        cluster_id:
            The cluster identifier, e.g. ``"cluster_abc123"``.

        Returns
        -------
        dict | None
            Qdrant payload dict, or ``None`` if not found.
        """
        return await self.get_by_cluster_id(cluster_id)

    async def upsert_incident_status(
        self,
        cluster_id: str,
        new_status: str | Any,
    ) -> None:
        """
        Patch only the ``status`` field of an existing verified incident point.

        Uses Qdrant's ``set_payload`` operation so no re-embedding is needed.
        The point is located by its integer point ID derived from *cluster_id*
        (same derivation used in :meth:`upsert_verified`).

        Parameters
        ----------
        cluster_id:
            The cluster to update, e.g. ``"cluster_abc123"``.
        new_status:
            The new :class:`~app.schemas.IncidentStatus` value (or string).
        """
        import asyncio
        import uuid

        from qdrant_client.models import Filter, FieldCondition, MatchValue

        status_str = new_status.value if hasattr(new_status, "value") else str(new_status)

        # Derive stable integer point ID from cluster_id (mirrors upsert_verified)
        raw_id = cluster_id.removeprefix("cluster_")
        try:
            point_id = uuid.UUID(raw_id).int % (2**63)
        except ValueError:
            point_id = abs(hash(cluster_id)) % (2**63)

        def _do_patch() -> None:
            # Try direct point ID patch first
            try:
                self._raw_client.set_payload(
                    collection_name=COLLECTION_NAME,
                    payload={"status": status_str},
                    points=[point_id],
                )
                return
            except Exception:
                pass

            # Fallback: patch by cluster_id payload filter
            try:
                self._raw_client.set_payload(
                    collection_name=COLLECTION_NAME,
                    payload={"status": status_str},
                    points=Filter(
                        must=[
                            FieldCondition(
                                key="cluster_id",
                                match=MatchValue(value=cluster_id),
                            )
                        ]
                    ),
                )
            except Exception as exc:
                logger.warning(
                    "upsert_incident_status fallback failed for %s: %s",
                    cluster_id,
                    exc,
                )

        await asyncio.get_event_loop().run_in_executor(None, _do_patch)
        logger.info(
            "Status patched in Qdrant: cluster_id=%s → %s", cluster_id, status_str
        )



# ── Module-level singleton ────────────────────────────────────────────────────

_vector_store: VectorStore | None = None


def get_vector_store() -> VectorStore:
    """Return the shared VectorStore singleton (initialised in main.py lifespan)."""
    if _vector_store is None:
        raise RuntimeError(
            "VectorStore not initialised. Call init_vector_store() during app startup."
        )
    return _vector_store


async def init_vector_store(qdrant_client: QdrantClient) -> VectorStore:
    """
    Initialise the VectorStore singleton and ensure the Qdrant collection exists.
    Called once from main.py lifespan.
    """
    global _vector_store
    _vector_store = VectorStore(qdrant_client=qdrant_client)
    await _vector_store.ensure_collection()
    return _vector_store
