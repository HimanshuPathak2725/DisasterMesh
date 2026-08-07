"""Dispatch router — trigger responder assignment."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/{cluster_id}", summary="Dispatch responders to incident")
async def dispatch_incident(cluster_id: str) -> dict:
    """
    Trigger the Orchestrator Agent to assign responders to an incident.

    TODO (Phase 5): run OR-Tools optimizer and return assignment.
    """
    return {
        "cluster_id": cluster_id,
        "assignment": None,
        "note": "stub — implement in Phase 5",
    }
