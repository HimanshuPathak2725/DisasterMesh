"""
Unit tests for the ingest endpoints.

Run:
    cd backend
    pytest app/tests/unit/test_ingest.py -v
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ingest_citizen_report() -> None:
    response = client.post(
        "/ingest/report",
        json={
            "source": "sms",
            "text": "Water rising fast near Yamuna Bazar",
            "lat": 28.6667,
            "lon": 77.2333,
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "received"
    assert "message_id" in body


def test_ingest_citizen_report_address_only() -> None:
    """Accepts report with address but no lat/lon."""
    response = client.post(
        "/ingest/report",
        json={
            "text": "Flooding at Times Square Delhi",
            "address": "Times Square, Delhi",
        },
    )
    assert response.status_code == 200


def test_ingest_social_post() -> None:
    response = client.post(
        "/ingest/social",
        json={
            "source": "tweet",
            "text": "Massive flooding in Yamuna Bazar #Delhi #Flood",
        },
    )
    assert response.status_code == 200


def test_ingest_satellite_polygon() -> None:
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[77.2, 28.6], [77.3, 28.6], [77.3, 28.7], [77.2, 28.7], [77.2, 28.6]]],
        },
        "properties": {},
    }
    response = client.post(
        "/ingest/satellite",
        json={
            "source": "satellite",
            "geojson": geojson,
        },
    )
    assert response.status_code == 200


def test_ingest_sensor() -> None:
    response = client.post(
        "/ingest/sensor",
        json={
            "sensor_id": "sensor_yamuna_001",
            "sensor_type": "water_level",
            "value": 4.7,
            "unit": "metres",
            "lat": 28.6667,
            "lon": 77.2333,
        },
    )
    assert response.status_code == 200
