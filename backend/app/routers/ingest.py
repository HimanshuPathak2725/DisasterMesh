"""Ingestion router — accepts reports from all source types."""

from uuid import uuid4

from fastapi import APIRouter

from app.schemas import (
    CitizenReportInput,
    IngestResponse,
    SatellitePolygonInput,
    SensorStreamInput,
    SocialPostInput,
)

router = APIRouter()


@router.post("/report", response_model=IngestResponse, summary="Citizen report")
async def ingest_citizen_report(report: CitizenReportInput) -> IngestResponse:
    """
    Accept a citizen report (SMS / WhatsApp / web form).

    Passes to the Situational Agent for normalization and embedding.
    """
    # TODO (Phase 1): call situational_agent.process(report)
    message_id = str(uuid4())
    return IngestResponse(message_id=message_id)


@router.post("/social", response_model=IngestResponse, summary="Social post")
async def ingest_social_post(post: SocialPostInput) -> IngestResponse:
    """Accept a social media post (tweet, news article)."""
    # TODO (Phase 1): call situational_agent.process(post)
    return IngestResponse(message_id=str(uuid4()))


@router.post("/satellite", response_model=IngestResponse, summary="Satellite polygon")
async def ingest_satellite_polygon(polygon: SatellitePolygonInput) -> IngestResponse:
    """Accept a GeoJSON polygon from Sentinel-2 flood detection."""
    # TODO (Phase 1): call situational_agent.process(polygon)
    return IngestResponse(message_id=str(uuid4()))


@router.post("/sensor", response_model=IngestResponse, summary="IoT sensor")
async def ingest_sensor_stream(sensor: SensorStreamInput) -> IngestResponse:
    """Accept an IoT sensor reading (water level, air quality, etc.)."""
    # TODO (Phase 1): call situational_agent.process(sensor)
    return IngestResponse(message_id=str(uuid4()))
