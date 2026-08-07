# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 36 files · ~11,041 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 289 nodes · 403 edges · 21 communities (15 shown, 6 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 51 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `13301c84`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 🌐 DisasterMesh
- 🏗️ Architecture
- AGENTS.md
- graphify.md
- graphify.md
- 📦 Data schema
- VerifiedIncident
- schemas.py
- CommunicationAgent
- VerificationAgent
- seed_data.py
- Contributing to DisasterMesh
- test_ingest.py
- incidents.py
- __init__.py
- __init__.py
- __init__.py

## God Nodes (most connected - your core abstractions)
1. `SituationalAgent` - 20 edges
2. `🌐 DisasterMesh` - 19 edges
3. `VerifiedIncident` - 16 edges
4. `_persist()` - 9 edges
5. `VictimAgent` - 9 edges
6. `_lookup_landmark()` - 8 edges
7. `_detect_language()` - 8 edges
8. `CommunicationAgent` - 8 edges
9. `VerificationAgent` - 8 edges
10. `_extract_geometry()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `test_landmark_case_insensitive()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_exact_match()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_hindi()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_substring_match()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_unknown_address()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py

## Import Cycles
- None detected.

## Communities (21 total, 6 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.07
Nodes (28): AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_db(), _get_engine(), get_qdrant_client() (+20 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.05
Nodes (52): Any, _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), CitizenReportInput, SatellitePolygonInput, SensorStreamInput (+44 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.06
Nodes (43): OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d, Dispatch optimizer using Google OR-Tools CP-SAT / routing solver.      Algorithm, Run OR-Tools optimizer and return optimal assignments.          TODO (Phase 5):, Cost = ETA_seconds × priority_weight.         Priority weights: P1=4, P2=3, P3=2, Resource Agent — Agent 4.  Responsibilities:   - Maintain live responder registr, Tracks and queries the responder registry., Return available responders within radius of the incident,         filtered by c (+35 more)

### Community 7 - "schemas.py"
Cohesion: 0.17
Nodes (10): async_sessionmaker, db_session(), patch_get_db(), patch_init_db(), conftest.py for unit tests.  Provides an in-memory SQLite database for ingest en, Create all tables in an in-memory SQLite DB once per test session., Yield a fresh async session, rolling back after each test., Replace the FastAPI `get_db` dependency with one that returns the     test sessi (+2 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.22
Nodes (7): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, IncidentStatus

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (7): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent

### Community 10 - "seed_data.py"
Cohesion: 0.23
Nodes (14): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., seed_citizen_reports() (+6 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.11
Nodes (24): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, ingest_citizen_report(), ingest_satellite_polygon() (+16 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 14 - "incidents.py"
Cohesion: 0.33
Nodes (5): get_incident(), query_incidents(), Incidents query router., Fetch a verified incident cluster by ID.      TODO (Phase 2): query Qdrant for t, Return incidents within `radius` metres of (lat, lon).      TODO (Phase 2): geo-

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VerifiedIncident` connect `VerifiedIncident` to `CommunicationAgent`, `VerificationAgent`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 12 inferred relationships involving `SituationalAgent` (e.g. with `test_process_citizen_report_address_only()` and `test_process_citizen_report_hindi_language()`) actually correct?**
  _`SituationalAgent` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `_persist()` (e.g. with `AuditLog` and `RawIngestionRecord`) actually correct?**
  _`_persist()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f`, `Case-insensitive prefix scan of the landmark table.`, `Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi` to the rest of the system?**
  _110 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `🌐 DisasterMesh` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._
- **Should `🏗️ Architecture` be split into smaller, more focused modules?**
  _Cohesion score 0.06685633001422475 - nodes in this community are weakly interconnected._