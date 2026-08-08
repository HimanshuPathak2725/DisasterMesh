"""
Canonical Pydantic schemas for DisasterMesh.

These models are the shared language between all six agents.
"""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field

# ── Enums ─────────────────────────────────────────────────────────────────────


class SourceType(StrEnum):
    SMS = "sms"
    WHATSAPP = "whatsapp"
    WEB_FORM = "web_form"
    TWEET = "tweet"
    SATELLITE = "satellite"
    IOT_SENSOR = "iot_sensor"
    NEWS = "news"


class IncidentStatus(StrEnum):
    REPORTED = "REPORTED"
    VERIFIED = "VERIFIED"
    ASSIGNED = "ASSIGNED"
    EN_ROUTE = "EN_ROUTE"
    ON_SCENE = "ON_SCENE"
    RESOLVED = "RESOLVED"


class Priority(StrEnum):
    P1 = "P1"  # Critical — immediate life threat
    P2 = "P2"  # High
    P3 = "P3"  # Medium
    P4 = "P4"  # Low


# ── Ingestion models (input to Situational Agent) ─────────────────────────────


class ProtoIncident(BaseModel):
    """Normalized incident before verification and deduplication."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    source: SourceType
    text: str
    lat: float | None = None
    lon: float | None = None
    address: str | None = None  # fallback for geocoding
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    media_urls: list[str] = []
    metadata: dict[str, Any] = {}
    raw_payload: dict[str, Any] = {}  # original input preserved for audit


class CitizenReportInput(BaseModel):
    source: SourceType = SourceType.SMS
    text: str
    lat: float | None = None
    lon: float | None = None
    address: str | None = None
    timestamp: datetime | None = None
    media_urls: list[str] = []


class SocialPostInput(BaseModel):
    source: SourceType = SourceType.TWEET
    text: str
    url: str | None = None
    lat: float | None = None
    lon: float | None = None
    timestamp: datetime | None = None


class SatellitePolygonInput(BaseModel):
    source: SourceType = SourceType.SATELLITE
    geojson: dict[str, Any]  # GeoJSON Feature or FeatureCollection
    timestamp: datetime | None = None
    media_urls: list[str] = []


class SensorStreamInput(BaseModel):
    source: SourceType = SourceType.IOT_SENSOR
    sensor_id: str
    sensor_type: str  # e.g. "water_level", "air_quality"
    value: float
    unit: str
    lat: float
    lon: float
    timestamp: datetime | None = None


# ── Needs & severity (output of Victim Agent) ─────────────────────────────────


class NeedsProfile(BaseModel):
    medical: bool = False
    shelter: bool = False
    evacuation: bool = False
    rescue: bool = False
    water: bool = False
    food: bool = False


class SeverityAssessment(BaseModel):
    needs: NeedsProfile
    severity_score: float = Field(ge=0.0, le=1.0)
    priority: Priority
    factors: dict[str, float] = {}  # breakdown of scoring factors


# ── Verified incident (shared across agents 3–6) ──────────────────────────────


class VerifiedIncident(BaseModel):
    cluster_id: str = Field(default_factory=lambda: f"cluster_{uuid4()}")
    source_provenance: list[SourceType] = []
    lat: float
    lon: float
    timestamp: datetime
    confidence: float = Field(ge=0.0, le=1.0)
    severity: Priority = Priority.P4
    needs: NeedsProfile = Field(default_factory=NeedsProfile)
    media_urls: list[str] = []
    status: IncidentStatus = IncidentStatus.REPORTED


# ── Responder / Resource models (Resource Agent) ──────────────────────────────


class ResponderCapability(StrEnum):
    MEDICAL = "medical"
    RESCUE = "rescue"
    WATER = "water"
    LOGISTICS = "logistics"
    EVACUATION = "evacuation"


class Responder(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    capabilities: list[ResponderCapability] = []
    lat: float
    lon: float
    available: bool = True
    team_size: int = 1


# ── Dispatch / Assignment (Orchestrator Agent) ────────────────────────────────


class Assignment(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    cluster_id: str
    responder_id: str
    eta_seconds: float
    route: dict[str, Any] = {}
    assigned_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


# ── API response helpers ───────────────────────────────────────────────────────


class HealthResponse(BaseModel):
    status: str = "ok"
    version: str = "0.1.0"
    environment: str


class IngestResponse(BaseModel):
    status: str = "received"
    message_id: str
    lat: float | None = None  # resolved coordinates (None if geocoding failed)
    lon: float | None = None


# ── Internal carrier types (not serialized) ───────────────────────────────────


from dataclasses import dataclass, field  # noqa: E402


@dataclass
class ClusterMatchResult:
    """
    Intermediate result of the 3-D clustering step inside VerificationAgent.

    Not a Pydantic model — this is a pure in-process carrier type that is never
    serialized to JSON or stored in any database.

    Fields
    ------
    cluster_id
        The cluster to join (may be a pre-existing one or a freshly-generated
        ``cluster_{uuid4()}``).
    members
        Raw Qdrant payload dicts for every proto-incident already in the cluster.
    member_vectors
        Stored embedding vectors corresponding to ``members`` (same order).
    similarity_scores
        Cosine similarity between the incoming proto's vector and each member
        vector (same order as ``members``).
    """

    cluster_id: str
    members: list[dict] = field(default_factory=list)
    member_vectors: list[list[float]] = field(default_factory=list)
    similarity_scores: list[float] = field(default_factory=list)
