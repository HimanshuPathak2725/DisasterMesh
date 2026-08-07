"""
Unit tests for incidents query router — Phase 2.

Run:
    cd backend
    pytest app/tests/unit/test_incidents.py -v
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_query_incidents_geo() -> None:
    response = client.get("/incidents/?lat=28.6667&lon=77.2333&radius=1000")
    assert response.status_code == 200
    data = response.json()
    assert "incidents" in data
    assert data["lat"] == 28.6667
    assert data["lon"] == 77.2333


def test_search_incidents_semantic() -> None:
    response = client.get("/incidents/search/semantic?q=flooding")
    assert response.status_code == 200
    data = response.json()
    assert "incidents" in data
    assert data["query"] == "flooding"


def test_get_incident_not_found() -> None:
    response = client.get("/incidents/unknown-id-12345")
    assert response.status_code == 404
