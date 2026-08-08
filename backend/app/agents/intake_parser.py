"""
Intake Parser Agent — LLM Smart Intake Layer (Phase 4.5).

Uses LangChain's ChatGroq with .with_structured_output(ParsedIntake) to parse
unstructured, multilingual (English, Hindi, Hinglish, mixed) crisis reports into
structured ParsedIntake objects.
"""

from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

from app.schemas import ParsedIntake

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a crisis report parser for DisasterMesh, an emergency response coordination system.
Your job is to analyze unstructured disaster/crisis reports submitted by citizens or social media posts in ANY language (English, Hindi, Hinglish, regional dialects, or mixed text).

Extract the following structured information accurately:
1. address: The location name, landmark, neighbourhood, city, or address mentioned (e.g. "Yamuna Bazar, Delhi", "Connaught Place", "sector 62 noida"). Null if no location name is mentioned.
2. lat / lon: Explicit numerical geographic coordinates if directly provided in the text (e.g. "lat 28.66, lon 77.23"). Null if coordinates are not explicitly written as numbers.
3. language: Detected language code ("hi" for Hindi, "en" for English, "hinglish" for Hindi written in Latin script, or appropriate code).
4. incident_type: Primary classification of the disaster ("flood", "fire", "building_collapse", "earthquake", "medical_emergency", "landslide", "storm", or "other").
5. needs: Boolean profile flagging what aid is required:
   - medical: True if injuries, bleeding, ambulance, hospital, or doctor needed.
   - shelter: True if homeless, displaced, shelter, or tent needed.
   - evacuation: True if evacuation, fleeing, or immediate removal needed.
   - rescue: True if trapped, stuck, underwater, under rubble, or SOS rescue needed.
   - water: True if drinking water or severe flooding water supply issue mentioned.
   - food: True if hunger, food, rations needed.
6. urgency_level: Integer from 1 (low/informational) to 5 (extreme SOS/immediate life threat).
7. time_reference: Time indicator string if mentioned (e.g. "since 2 hours ago", "this morning", "just now"). Null if absent.
8. cleaned_text: A concise, normalized English translation / summary of the crisis report.

Be extremely empathetic and precise. Never fabricate location names or coordinates that were not stated or implied in the text.
"""

_intake_parser: IntakeParserAgent | None = None


def get_intake_parser() -> IntakeParserAgent:
    """Return the shared IntakeParserAgent singleton."""
    global _intake_parser
    if _intake_parser is None:
        _intake_parser = IntakeParserAgent()
    return _intake_parser


class IntakeParserAgent:
    """Parses free-text crisis reports into structured ParsedIntake using ChatGroq."""

    def __init__(self, api_key: str | None = None, model_name: str | None = None) -> None:
        self.api_key = api_key or os.getenv("GROQ_API_KEY", "").strip()
        self.model_name = model_name or os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()

    def is_available(self) -> bool:
        """Return True if GROQ_API_KEY is configured."""
        return bool(self.api_key or os.getenv("GROQ_API_KEY", "").strip())

    async def parse(self, raw_text: str) -> ParsedIntake:
        """
        Parse raw unstructured text using Groq LLM via LangChain.

        Returns
        -------
        ParsedIntake
            Typed Pydantic object containing extracted location, needs, urgency, etc.

        Raises
        ------
        RuntimeError
            If GROQ_API_KEY is not configured or LLM invocation fails.
        """
        key = self.api_key or os.getenv("GROQ_API_KEY", "").strip()
        if not key:
            raise RuntimeError("GROQ_API_KEY is not configured in environment")

        llm = ChatGroq(
            groq_api_key=key,
            model_name=self.model_name,
            temperature=0.0,
        )

        structured_llm = llm.with_structured_output(ParsedIntake)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Report text to parse:\n\"\"\"{raw_text}\"\"\""),
        ]

        logger.info("IntakeParserAgent parsing text (len=%d) via Groq model=%s", len(raw_text), self.model_name)
        try:
            result = await structured_llm.ainvoke(messages)
            if isinstance(result, ParsedIntake):
                return result
            # Fallback if dictionary returned
            return ParsedIntake.model_validate(result)
        except Exception as err:
            logger.warning("IntakeParserAgent LLM call failed: %s", err)
            raise RuntimeError(f"IntakeParserAgent failed: {err}") from err
