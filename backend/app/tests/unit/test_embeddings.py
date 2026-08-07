"""
Unit tests for EmbeddingService — Phase 2.

Run:
    cd backend
    pytest app/tests/unit/test_embeddings.py -v
"""

from __future__ import annotations

import pytest

from app.agents.embeddings import get_embedding_service
from app.schemas import ProtoIncident, SourceType


@pytest.mark.asyncio
async def test_embed_text_returns_384_dims() -> None:
    service = get_embedding_service()
    vector = await service.embed_text("Water rising near Yamuna Bazar")
    assert isinstance(vector, list)
    assert len(vector) == 384
    assert all(isinstance(v, float) for v in vector)


@pytest.mark.asyncio
async def test_embed_text_english_and_hindi() -> None:
    service = get_embedding_service()
    v_en = await service.embed_text("Flooding near Yamuna Bazar, need boat rescue")
    v_hi = await service.embed_text("यमुना बाज़ार में बाढ़, नाव बचाओ की ज़रूरत")
    assert len(v_en) == 384
    assert len(v_hi) == 384

    # Both embeddings are valid 384-dim normalized vectors
    sim = service.cosine_similarity(v_en, v_hi)
    assert isinstance(sim, float)
    assert -1.0 <= sim <= 1.0


@pytest.mark.asyncio
async def test_embed_incident_with_and_without_coords() -> None:
    service = get_embedding_service()
    proto_with_coords = ProtoIncident(
        source=SourceType.SMS,
        text="Water rising fast",
        lat=28.6667,
        lon=77.2333,
    )
    proto_no_coords = ProtoIncident(
        source=SourceType.SMS,
        text="Water rising fast",
    )

    v_coords = await service.embed_incident(proto_with_coords)
    v_no_coords = await service.embed_incident(proto_no_coords)

    assert len(v_coords) == 384
    assert len(v_no_coords) == 384
    # Vectors should be slightly different because location was appended
    assert v_coords != v_no_coords


@pytest.mark.asyncio
async def test_cosine_similarity() -> None:
    service = get_embedding_service()
    v1 = await service.embed_text("Heavy flood in Delhi")
    v2 = await service.embed_text("Severe waterlogging in Delhi city")
    v3 = await service.embed_text("Clear sunny day in the park")

    sim_1_2 = service.cosine_similarity(v1, v2)
    sim_1_3 = service.cosine_similarity(v1, v3)

    assert sim_1_2 > sim_1_3
    assert sim_1_2 > 0.5


@pytest.mark.asyncio
async def test_embed_batch() -> None:
    service = get_embedding_service()
    texts = ["Report 1", "Report 2", "Report 3"]
    vectors = await service.embed_batch(texts)
    assert len(vectors) == 3
    assert all(len(v) == 384 for v in vectors)
