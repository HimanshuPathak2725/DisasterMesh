"""
Integration tests for VectorStore with Qdrant — Phase 2.

Uses an in-memory QdrantClient (no disk I/O, no Docker required).

Run:
    cd backend
    pytest app/tests/integration/test_vector_store.py -v
"""

from __future__ import annotations

import pytest
from qdrant_client import QdrantClient

from app.agents.embeddings import get_embedding_service
from app.agents.vector_store import VectorStore
from app.schemas import ProtoIncident, SourceType


@pytest.fixture
async def memory_vector_store() -> VectorStore:
    """Create a fresh in-memory VectorStore for each test."""
    client = QdrantClient(":memory:")
    store = VectorStore(qdrant_client=client)
    await store.ensure_collection()
    return store


@pytest.mark.asyncio
async def test_ensure_collection_is_idempotent(memory_vector_store: VectorStore) -> None:
    # Ensure collection can be called multiple times without error
    await memory_vector_store.ensure_collection()
    size = await memory_vector_store.collection_size()
    assert size == 0


@pytest.mark.asyncio
async def test_upsert_and_get_by_proto_id(memory_vector_store: VectorStore) -> None:
    embedder = get_embedding_service()
    proto = ProtoIncident(
        source=SourceType.SMS,
        text="Flood at Yamuna Bazar",
        lat=28.6667,
        lon=77.2333,
    )
    vector = await embedder.embed_incident(proto)
    await memory_vector_store.upsert(proto, vector)

    payload = await memory_vector_store.get_by_proto_id(proto.id)
    assert payload is not None
    assert payload["proto_id"] == proto.id
    assert payload["lat"] == 28.6667
    assert payload["text"] == "Flood at Yamuna Bazar"


@pytest.mark.asyncio
async def test_search_similar(memory_vector_store: VectorStore) -> None:
    embedder = get_embedding_service()

    p1 = ProtoIncident(source=SourceType.SMS, text="Water level rising rapidly in river")
    p2 = ProtoIncident(
        source=SourceType.TWEET, text="Heavy rains causing severe flooding in the valley"
    )
    p3 = ProtoIncident(source=SourceType.IOT_SENSOR, text="Air quality index normal at 45")

    for p in (p1, p2, p3):
        vec = await embedder.embed_incident(p)
        await memory_vector_store.upsert(p, vec)

    results = await memory_vector_store.search_similar("flooding in river", limit=2)
    assert len(results) >= 1
    top_doc, top_score = results[0]
    assert "rising" in top_doc.page_content or "flooding" in top_doc.page_content


@pytest.mark.asyncio
async def test_search_nearby_geo_radius(memory_vector_store: VectorStore) -> None:
    embedder = get_embedding_service()

    # Yamuna Bazar (lat: 28.6667, lon: 77.2333)
    p_near = ProtoIncident(
        source=SourceType.SMS,
        text="Water entering homes at Yamuna Bazar",
        lat=28.6667,
        lon=77.2333,
    )
    # Connaught Place (~4.5 km away)
    p_far = ProtoIncident(
        source=SourceType.SMS,
        text="Water logging at Connaught Place",
        lat=28.6315,
        lon=77.2167,
    )

    for p in (p_near, p_far):
        vec = await embedder.embed_incident(p)
        await memory_vector_store.upsert(p, vec)

    # Search within 500 metres of Yamuna Bazar
    nearby = await memory_vector_store.search_nearby(
        lat=28.6667,
        lon=77.2333,
        radius_m=500.0,
    )

    assert len(nearby) == 1
    assert nearby[0]["proto_id"] == p_near.id
