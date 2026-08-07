"""
Unit tests for the health check endpoint.

Run:
    cd backend
    pytest app/tests/unit/test_health.py -v
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_200() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_shape() -> None:
    response = client.get("/health")
    body = response.json()
    assert body["status"] == "ok"
    assert "version" in body
    assert "environment" in body


def test_health_version() -> None:
    response = client.get("/health")
    assert response.json()["version"] == "0.1.0"
