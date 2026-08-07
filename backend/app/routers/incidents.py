"""Incidents query router — Phase 2 vector memory integration."""

from fastapi import APIRouter, HTTPException, Query

from app.agents.vector_store import get_vector_store

router = APIRouter()


@router.get("/search/semantic", summary="Semantic search for incidents")
async def search_incidents_semantic(
    q: str = Query(..., description="Query text"),
    limit: int = Query(10, description="Max results"),
    min_score: float = Query(0.0, description="Minimum similarity score [0..1]"),
) -> dict:
    """
    Search incidents by semantic similarity using LangChain embeddings & Qdrant.
    """
    store = get_vector_store()
    results = await store.search_similar(query_text=q, limit=limit, min_score=min_score)

    incidents = []
    for doc, score in results:
        payload = dict(doc.metadata) if hasattr(doc, "metadata") else {}
        payload.pop("_id", None)
        payload.pop("_collection_name", None)
        if hasattr(doc, "page_content") and "text" not in payload:
            payload["text"] = doc.page_content
        payload["similarity_score"] = float(score)
        incidents.append(payload)

    return {
        "query": q,
        "count": len(incidents),
        "incidents": incidents,
    }


@router.get("/{proto_id}", summary="Get incident by proto ID")
async def get_incident(proto_id: str) -> dict:
    """
    Fetch a proto incident by ID from Qdrant vector store.
    """
    store = get_vector_store()
    incident = await store.get_by_proto_id(proto_id)
    if not incident:
        raise HTTPException(status_code=404, detail=f"Incident {proto_id} not found")
    return incident


@router.get("/", summary="Geo query for nearby incidents")
async def query_incidents(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    radius: float = Query(5000.0, description="Radius in metres"),
    limit: int = Query(50, description="Max results"),
) -> dict:
    """
    Return proto incidents within `radius` metres of (lat, lon).
    """
    store = get_vector_store()
    incidents = await store.search_nearby(lat=lat, lon=lon, radius_m=radius, limit=limit)
    return {
        "lat": lat,
        "lon": lon,
        "radius_m": radius,
        "count": len(incidents),
        "incidents": incidents,
    }
