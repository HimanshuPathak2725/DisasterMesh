"""
Resource Agent — Agent 4.

Responsibilities:
  - Maintain live responder registry (location, availability, capabilities)
  - Match incident needs to responder capabilities
  - Track resource availability in real time

Implemented in Phase 5.
"""

import logging

from app.schemas import Responder, VerifiedIncident

logger = logging.getLogger(__name__)


class ResourceAgent:
    """Tracks and queries the responder registry."""

    async def get_available_responders(
        self,
        incident: VerifiedIncident,
        radius_m: float = 10_000,
    ) -> list[Responder]:
        """
        Return available responders within radius of the incident,
        filtered by capabilities matching incident needs.

        TODO (Phase 5): query responder registry DB and sort by Haversine distance.
        """
        raise NotImplementedError("Implement in Phase 5")

    async def update_responder_location(self, responder_id: str, lat: float, lon: float) -> None:
        """TODO (Phase 5): update responder GPS in DB and Redis."""
        raise NotImplementedError("Implement in Phase 5")

    async def set_availability(self, responder_id: str, available: bool) -> None:
        """TODO (Phase 5): toggle responder availability."""
        raise NotImplementedError("Implement in Phase 5")
