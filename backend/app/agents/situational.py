"""
Situational Agent — Agent 1.

Responsibilities:
  - Accept raw inputs from all four source types
  - Geocode missing coordinates (Nominatim + Hindi transliteration)
  - Detect and normalize language (English / Hindi)
  - Normalize to ProtoIncident
  - Emit event to Verification Agent

Implemented in Phase 1.
"""

import logging

from app.schemas import (
    CitizenReportInput,
    ProtoIncident,
    SatellitePolygonInput,
    SensorStreamInput,
    SocialPostInput,
)

logger = logging.getLogger(__name__)


class SituationalAgent:
    """Normalizes all incoming data streams into ProtoIncident objects."""

    async def process_citizen_report(self, report: CitizenReportInput) -> ProtoIncident:
        """TODO (Phase 1): geocode, language-detect, normalize."""
        raise NotImplementedError("Implement in Phase 1")

    async def process_social_post(self, post: SocialPostInput) -> ProtoIncident:
        """TODO (Phase 1): extract geo from text, normalize."""
        raise NotImplementedError("Implement in Phase 1")

    async def process_satellite_polygon(self, polygon: SatellitePolygonInput) -> ProtoIncident:
        """TODO (Phase 1): extract centroid from GeoJSON, normalize."""
        raise NotImplementedError("Implement in Phase 1")

    async def process_sensor(self, sensor: SensorStreamInput) -> ProtoIncident:
        """TODO (Phase 1): threshold check, normalize."""
        raise NotImplementedError("Implement in Phase 1")

    async def _geocode(self, address: str) -> tuple[float, float] | None:
        """TODO (Phase 1): Nominatim lookup with Hindi transliteration."""
        return None

    async def _detect_language(self, text: str) -> str:
        """TODO (Phase 1): langdetect or fasttext."""
        return "en"
