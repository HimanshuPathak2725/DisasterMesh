"""
SQLAlchemy ORM models for DisasterMesh.

Tables
------
raw_ingestion_records  — every normalised ProtoIncident row, keyed by its ID.
audit_log              — immutable append-only trail: who did what, when.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import JSON, Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RawIngestionRecord(Base):
    """
    Persists the raw payload **and** the normalised ProtoIncident produced
    by the SituationalAgent for every inbound message.
    """

    __tablename__ = "raw_ingestion_records"

    # Primary key matches ProtoIncident.id (UUID string)
    id: Mapped[str] = mapped_column(String, primary_key=True)
    source_type: Mapped[str] = mapped_column(String(32), nullable=False, index=True)

    # Raw input as-received (JSON blob)
    raw_payload: Mapped[dict] = mapped_column(JSON, nullable=False)

    # Normalised ProtoIncident fields (redundant with payload but queryable)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    lat: Mapped[float | None] = mapped_column(Float, nullable=True)
    lon: Mapped[float | None] = mapped_column(Float, nullable=True)
    address: Mapped[str | None] = mapped_column(String(512), nullable=True)
    language: Mapped[str] = mapped_column(String(8), default="en", nullable=False)
    media_urls: Mapped[list] = mapped_column(JSON, default=list, nullable=False)

    # Full normalised payload (for downstream agents to replay without re-parsing)
    normalized_payload: Mapped[dict] = mapped_column(JSON, nullable=False)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
        index=True,
    )
    processed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"<RawIngestionRecord id={self.id!r} source={self.source_type!r}>"


class AuditLog(Base):
    """
    Immutable append-only audit trail — captures who/what/when for every
    significant action in the pipeline.
    """

    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    action: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    entity_type: Mapped[str] = mapped_column(String(64), nullable=False)
    entity_id: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    details: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    success: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
        index=True,
    )

    def __repr__(self) -> str:
        return (
            f"<AuditLog id={self.id} action={self.action!r} entity={self.entity_id!r}>"
        )
