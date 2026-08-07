"""
Victim Agent — Agent 3.

Responsibilities:
  - Extract needs (medical, shelter, evacuation, rescue, water, food) from incident text
  - Compute multi-factor severity score (0.0 – 1.0)
  - Assign priority label (P1–P4)
  - Optionally use LLM for bilingual (Hindi/English) needs extraction

Implemented in Phase 4.
"""

import logging

from app.schemas import NeedsProfile, Priority, SeverityAssessment, VerifiedIncident

logger = logging.getLogger(__name__)

# Keyword → need type mapping (bilingual)
KEYWORD_MAP: dict[str, list[str]] = {
    "medical": [
        "injured",
        "bleeding",
        "medical",
        "ambulance",
        "hospital",
        "doctor",
        "घायल",
        "खून",
        "अस्पताल",
        "डॉक्टर",
    ],
    "shelter": ["homeless", "shelter", "tent", "displaced", "refuge", "बेघर", "शरण", "तंबू"],
    "evacuation": ["evacuate", "evacuation", "flee", "escape", "निकासी", "भागो", "बाहर"],
    "rescue": ["rescue", "trapped", "stuck", "help", "save", "बचाओ", "फंसे", "मदद"],
    "water": ["water", "drinking", "flood", "पानी", "बाढ़"],
    "food": ["food", "hungry", "starving", "खाना", "भूख"],
}


class VictimAgent:
    """Extracts needs and computes severity for verified incidents."""

    async def assess(self, incident: VerifiedIncident) -> SeverityAssessment:
        """
        Assess needs and severity for a verified incident.

        TODO (Phase 4): implement full multi-factor scoring.
        """
        raise NotImplementedError("Implement in Phase 4")

    def _extract_needs_keyword(self, text: str) -> NeedsProfile:
        """Fast keyword-based needs extraction (bilingual)."""
        text_lower = text.lower()
        return NeedsProfile(
            **{
                need: any(kw in text_lower for kw in keywords)
                for need, keywords in KEYWORD_MAP.items()
            }
        )

    def _score_to_priority(self, score: float) -> Priority:
        if score >= 0.75:
            return Priority.P1
        if score >= 0.5:
            return Priority.P2
        if score >= 0.25:
            return Priority.P3
        return Priority.P4
