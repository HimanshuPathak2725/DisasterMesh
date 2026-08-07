"""
Communication Agent — Agent 6.

Responsibilities:
  - Notify assigned responders (SMS via Twilio, WhatsApp optional)
  - Notify incident reporter of status updates
  - Manage incident lifecycle state machine:
      REPORTED → VERIFIED → ASSIGNED → EN_ROUTE → ON_SCENE → RESOLVED
  - Log all communications for audit

Implemented in Phase 6.
"""

import logging

from app.schemas import Assignment, IncidentStatus, VerifiedIncident

logger = logging.getLogger(__name__)

# Valid state transitions
VALID_TRANSITIONS: dict[IncidentStatus, list[IncidentStatus]] = {
    IncidentStatus.REPORTED: [IncidentStatus.VERIFIED],
    IncidentStatus.VERIFIED: [IncidentStatus.ASSIGNED],
    IncidentStatus.ASSIGNED: [IncidentStatus.EN_ROUTE],
    IncidentStatus.EN_ROUTE: [IncidentStatus.ON_SCENE],
    IncidentStatus.ON_SCENE: [IncidentStatus.RESOLVED],
    IncidentStatus.RESOLVED: [],
}


class CommunicationAgent:
    """Handles notifications and incident lifecycle transitions."""

    async def notify_assignment(self, assignment: Assignment, responder_phone: str) -> None:
        """
        SMS the responder with assignment details.

        TODO (Phase 6): Twilio client integration.
        """
        raise NotImplementedError("Implement in Phase 6")

    async def notify_reporter(self, phone: str, status: IncidentStatus) -> None:
        """
        Notify the original reporter of status updates.

        TODO (Phase 6): Twilio SMS.
        """
        raise NotImplementedError("Implement in Phase 6")

    def transition(
        self, incident: VerifiedIncident, new_status: IncidentStatus
    ) -> VerifiedIncident:
        """
        Apply a lifecycle transition.

        Raises ValueError for invalid transitions.
        """
        allowed = VALID_TRANSITIONS.get(incident.status, [])
        if new_status not in allowed:
            raise ValueError(
                f"Invalid transition: {incident.status} → {new_status}. Allowed: {allowed}"
            )
        incident.status = new_status
        logger.info("Incident %s → %s", incident.cluster_id, new_status)
        return incident
