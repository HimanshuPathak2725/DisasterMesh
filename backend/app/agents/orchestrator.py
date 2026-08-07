"""
Orchestrator Agent — Agent 5.

Responsibilities:
  - Solve the multi-responder dispatch optimization with Google OR-Tools
  - Minimize weighted sum of ETA, severity, and coverage
  - Produce Assignment objects consumed by Communication Agent

Implemented in Phase 5.
"""

import logging

from app.schemas import Assignment, Responder, VerifiedIncident

logger = logging.getLogger(__name__)


class OrchestratorAgent:
    """
    Dispatch optimizer using Google OR-Tools CP-SAT / routing solver.

    Algorithm overview:
      1. Build cost matrix (ETA × priority weight) for each (incident, responder) pair
      2. Add constraints: responder capacity, capability match, availability
      3. Minimize total weighted response time
      4. Return list of Assignments
    """

    async def optimize(
        self,
        incidents: list[VerifiedIncident],
        responders: list[Responder],
    ) -> list[Assignment]:
        """
        Run OR-Tools optimizer and return optimal assignments.

        TODO (Phase 5): implement CP-SAT model.
        """
        raise NotImplementedError("Implement in Phase 5")

    def _build_cost_matrix(
        self,
        incidents: list[VerifiedIncident],
        responders: list[Responder],
    ) -> list[list[float]]:
        """
        Cost = ETA_seconds × priority_weight.
        Priority weights: P1=4, P2=3, P3=2, P4=1.

        TODO (Phase 5): compute real ETAs via routing API or Haversine approximation.
        """
        raise NotImplementedError("Implement in Phase 5")
