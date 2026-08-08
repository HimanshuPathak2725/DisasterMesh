"""
Integration tests for Dispatch & Responders REST APIs — Phase 5.

Validates:
  - POST /responders & GET /responders
  - PUT /responders/{id}/location & PUT /responders/{id}/status
  - POST /dispatch/{cluster_id} with Qdrant vector store integration
  - POST /dispatch/optimize batch dispatch
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest
from httpx import ASGITransport, AsyncClient

from app.agents.vector_store import get_vector_store
from app.main import app
from app.schemas import NeedsProfile, Priority, VerifiedIncident


@pytest.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_responder_crud_flow(async_client):
    # 1. Register a responder
    payload = {
        "name": "Integration Squad",
        "team_type": "rescue",
        "capabilities": ["medical", "rescue"],
        "team_size": 5,
        "capacity": 2,
        "lat": 28.667,
        "lon": 77.233,
    }
    resp = await async_client.post("/responders", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    resp_id = data["id"]
    assert data["name"] == "Integration Squad"
    assert data["status"] == "available"

    # 2. Get responder by ID
    resp = await async_client.get(f"/responders/{resp_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == resp_id

    # 3. List responders
    resp = await async_client.get("/responders?status=available")
    assert resp.status_code == 200
    items = resp.json()
    assert any(i["id"] == resp_id for i in items)

    # 4. Update location
    loc_payload = {"lat": 28.670, "lon": 77.240}
    resp = await async_client.put(f"/responders/{resp_id}/location", json=loc_payload)
    assert resp.status_code == 200
    assert resp.json()["lat"] == 28.670

    # 5. Update status to assigned
    status_payload = {"status": "assigned", "incident_id": "cluster_99", "eta_minutes": 10}
    resp = await async_client.put(f"/responders/{resp_id}/status", json=status_payload)
    assert resp.status_code == 200
    assert resp.json()["status"] == "assigned"
    assert resp.json()["assigned_incident_id"] == "cluster_99"

    # 6. Reset status to available
    reset_payload = {"status": "available"}
    resp = await async_client.put(f"/responders/{resp_id}/status", json=reset_payload)
    assert resp.status_code == 200
    assert resp.json()["status"] == "available"
    assert resp.json()["assigned_incident_id"] is None


@pytest.mark.asyncio
async def test_dispatch_nonexistent_cluster(async_client, memory_vector_store):
    resp = await async_client.post("/dispatch/cluster_does_not_exist_123")
    assert resp.status_code == 404
    assert "not found" in resp.json()["detail"].lower()


@pytest.mark.asyncio
async def test_dispatch_cluster_flow(async_client, memory_vector_store):
    # 1. Register a responder
    resp = await async_client.post(
        "/responders",
        json={
            "name": "Delhi Rescue Team 1",
            "team_type": "rescue",
            "capabilities": ["medical", "rescue", "water"],
            "team_size": 10,
            "capacity": 3,
            "lat": 28.667,
            "lon": 77.233,
        },
    )
    assert resp.status_code == 201

    # 2. Upsert a verified incident into memory vector store
    v_store = get_vector_store()
    incident = VerifiedIncident(
        cluster_id="cluster_integ_001",
        lat=28.667,
        lon=77.233,
        timestamp=datetime.now(UTC),
        confidence=0.9,
        severity=Priority.P1,
        needs=NeedsProfile(medical=True, rescue=True),
    )
    # Dummy embedding vector of 384 floats
    dummy_vec = [0.1] * 384
    await v_store.upsert_verified(incident, dummy_vec)

    # 3. Call POST /dispatch/cluster_integ_001
    resp = await async_client.post(f"/dispatch/{incident.cluster_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["cluster_id"] == incident.cluster_id
    assert data["status"] in ("ASSIGNED", "HEURISTIC_FALLBACK")
    assert len(data["assignments"]) >= 1


@pytest.mark.asyncio
async def test_dispatch_batch_optimize(async_client, memory_vector_store):
    # Register responder
    await async_client.post(
        "/responders",
        json={
            "name": "Batch Team 1",
            "capabilities": ["medical", "rescue"],
            "lat": 28.6,
            "lon": 77.2,
        },
    )

    v_store = get_vector_store()
    inc1 = VerifiedIncident(
        cluster_id="batch_inc_1",
        lat=28.6,
        lon=77.2,
        timestamp=datetime.now(UTC),
        confidence=0.9,
        severity=Priority.P2,
    )
    await v_store.upsert_verified(inc1, [0.1] * 384)

    # Call POST /dispatch/optimize with 1 valid and 1 invalid cluster_id
    resp = await async_client.post(
        "/dispatch/optimize",
        json={"cluster_ids": ["batch_inc_1", "nonexistent_cluster_999"]},
    )
    assert resp.status_code == 200
    results = resp.json()
    assert len(results) == 2
    assert results[0]["cluster_id"] == "batch_inc_1"
    assert results[0]["status"] in ("ASSIGNED", "HEURISTIC_FALLBACK")
    assert results[1]["cluster_id"] == "nonexistent_cluster_999"
    assert results[1]["status"] == "NO_RESPONDERS_AVAILABLE"
