"""
Unit tests for IntakeParserAgent (Phase 4.5).

Mocks ChatGroq so no real Groq network calls take place during testing.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from app.agents.intake_parser import IntakeParserAgent, get_intake_parser
from app.schemas import NeedsProfile, ParsedIntake


def test_is_available_returns_false_when_no_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    agent = IntakeParserAgent(api_key="")
    assert agent.is_available() is False


def test_is_available_returns_true_when_api_key_set(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GROQ_API_KEY", "gsk_test_12345")
    agent = IntakeParserAgent(api_key="gsk_test_12345")
    assert agent.is_available() is True


@pytest.mark.anyio
async def test_parse_raises_runtime_error_if_no_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    agent = IntakeParserAgent(api_key="")
    with pytest.raises(RuntimeError, match="GROQ_API_KEY is not configured"):
        await agent.parse("help flood")


@pytest.mark.anyio
async def test_parse_success_mocked_llm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GROQ_API_KEY", "gsk_test_key")

    mock_parsed = ParsedIntake(
        address="Yamuna Bazar, Delhi",
        lat=28.6670,
        lon=77.2335,
        language="hinglish",
        incident_type="flood",
        needs=NeedsProfile(rescue=True, water=True),
        urgency_level=4,
        time_reference="since morning",
        cleaned_text="Flooding at Yamuna Bazar, rescue and water needed",
    )

    agent = IntakeParserAgent(api_key="gsk_test_key")

    # Patch ChatGroq inside intake_parser.py
    mock_runnable = AsyncMock()
    mock_runnable.ainvoke.return_value = mock_parsed

    with patch("app.agents.intake_parser.ChatGroq") as MockChatGroq:
        mock_chat = MockChatGroq.return_value
        mock_chat.with_structured_output.return_value = mock_runnable

        result = await agent.parse("bhai yamuna bazar mein pani bhar gaya phanse hain")

        assert result.address == "Yamuna Bazar, Delhi"
        assert result.language == "hinglish"
        assert result.incident_type == "flood"
        assert result.needs.rescue is True
        assert result.needs.water is True
        assert result.urgency_level == 4
        assert result.cleaned_text == "Flooding at Yamuna Bazar, rescue and water needed"


def test_get_intake_parser_singleton() -> None:
    p1 = get_intake_parser()
    p2 = get_intake_parser()
    assert p1 is p2
