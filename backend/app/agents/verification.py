"""
Verification Agent — Agent 2.

Responsibilities:
  - Deduplicate reports using spatial (150 m) + temporal (30 min) + semantic (cosine > 0.7) clustering
  - Compute confidence scores (corroboration × cross-source bonus × stale penalty)
  - Filter spam and stale reports
  - Choose canonical representative per cluster
  - Upsert verified incident back to Qdrant

Implemented in Phase 3.
"""

import logging

from app.schemas import ProtoIncident, VerifiedIncident

logger = logging.getLogger(__name__)

GEO_RADIUS_M = 150
TIME_WINDOW_SECONDS = 30 * 60  # 30 minutes
SIMILARITY_THRESHOLD = 0.7


class VerificationAgent:
    """
    Deduplicates and verifies proto-incidents.

    Uses three-dimensional clustering:
    - Spatial: Haversine distance ≤ GEO_RADIUS_M
    - Temporal: within TIME_WINDOW_SECONDS
    - Semantic: cosine similarity ≥ SIMILARITY_THRESHOLD
    """

    async def verify(self, proto: ProtoIncident) -> VerifiedIncident:
        """
        Main entry point: verify + deduplicate a proto-incident.

        TODO (Phase 3): implement full clustering pipeline.
        """
        raise NotImplementedError("Implement in Phase 3")

    async def _search_nearby(self, lat: float, lon: float) -> list[VerifiedIncident]:
        """TODO (Phase 3): Qdrant geo + time filter."""
        return []

    def _compute_confidence(self, cluster_members: list, new_proto: ProtoIncident) -> float:
        """TODO (Phase 3): corroboration × cross-source bonus × stale penalty."""
        return 0.5

    @staticmethod
    def _haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Distance in metres between two lat/lon points."""
        from math import asin, cos, radians, sin, sqrt

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat, dlon = lat2 - lat1, lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        return 2 * asin(sqrt(a)) * 6_371_000
