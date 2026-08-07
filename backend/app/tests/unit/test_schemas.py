"""
Unit tests for Pydantic schemas.

Validates that models accept valid input and reject bad input.
"""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from app.schemas import (
    CitizenReportInput,
    IncidentStatus,
    NeedsProfile,
    Priority,
    SourceType,
    VerifiedIncident,
)


def test_citizen_report_input_valid() -> None:
    report = CitizenReportInput(
        text="Water rising near Yamuna Bazar",
        lat=28.6667,
        lon=77.2333,
    )
    assert report.source == SourceType.SMS
    assert report.lat == 28.6667


def test_citizen_report_input_address_only() -> None:
    """Address without lat/lon should be accepted (geocoded later)."""
    report = CitizenReportInput(
        text="Flooding at Connaught Place",
        address="Connaught Place, Delhi",
    )
    assert report.lat is None
    assert report.address == "Connaught Place, Delhi"


def test_verified_incident_defaults() -> None:
    incident = VerifiedIncident(
        lat=28.6139,
        lon=77.2090,
        timestamp=datetime.now(UTC),
        confidence=0.9,
    )
    assert incident.status == IncidentStatus.REPORTED
    assert incident.severity == Priority.P4
    assert incident.needs == NeedsProfile()


def test_confidence_bounds() -> None:
    with pytest.raises(ValidationError):
        VerifiedIncident(
            lat=0,
            lon=0,
            timestamp=datetime.now(UTC),
            confidence=1.5,  # out of range
        )


def test_lifecycle_transition_map() -> None:
    """Smoke-test the state machine transition table."""
    from app.agents.communication import VALID_TRANSITIONS

    assert IncidentStatus.VERIFIED in VALID_TRANSITIONS[IncidentStatus.REPORTED]
    assert VALID_TRANSITIONS[IncidentStatus.RESOLVED] == []
