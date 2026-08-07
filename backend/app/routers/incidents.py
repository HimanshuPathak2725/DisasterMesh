"""Incidents query router."""

from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/{cluster_id}", summary="Get incident by cluster ID")
async def get_incident(cluster_id: str) -> dict:
    """
    Fetch a verified incident cluster by ID.

    TODO (Phase 2): query Qdrant for the cluster.
    """
    # Stub — returns placeholder
    return {"cluster_id": cluster_id, "status": "stub — implement in Phase 2"}


@router.get("/", summary="Geo query for nearby incidents")
async def query_incidents(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    radius: float = Query(5000, description="Radius in metres"),
) -> dict:
    """
    Return incidents within `radius` metres of (lat, lon).

    TODO (Phase 2): geo-filter query against Qdrant.
    """
    return {
        "lat": lat,
        "lon": lon,
        "radius_m": radius,
        "incidents": [],
        "note": "stub — implement in Phase 2",
    }
