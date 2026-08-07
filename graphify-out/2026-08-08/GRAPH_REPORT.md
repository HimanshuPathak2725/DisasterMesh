# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 36 files · ~11,041 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 279 nodes · 425 edges · 21 communities (15 shown, 6 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8cf15519`
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
- VerificationAgent
- seed_data.py
- Contributing to DisasterMesh
- test_ingest.py
- test_schemas.py
- incidents.py
- __init__.py
- __init__.py
- __init__.py

## God Nodes (most connected - your core abstractions)
1. `SituationalAgent` - 26 edges
2. `🌐 DisasterMesh` - 19 edges
3. `VerifiedIncident` - 16 edges
4. `ProtoIncident` - 12 edges
5. `CitizenReportInput` - 12 edges
6. `VictimAgent` - 9 edges
7. `_persist()` - 9 edges
8. `CommunicationAgent` - 8 edges
9. `_lookup_landmark()` - 8 edges
10. `_detect_language()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `test_landmark_case_insensitive()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_exact_match()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_hindi()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py

## Import Cycles
- None detected.

## Communities (21 total, 6 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.07
Nodes (29): AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_db(), _get_engine(), get_qdrant_client() (+21 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (53): Any, _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Lightweight language detection.      Returns 'hi' if the text contains Devanagar, Normalizes all incoming data streams into ProtoIncident objects. (+45 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.07
Nodes (35): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d (+27 more)

### Community 7 - "schemas.py"
Cohesion: 0.17
Nodes (10): async_sessionmaker, db_session(), patch_get_db(), patch_init_db(), conftest.py for unit tests.  Provides an in-memory SQLite database for ingest en, Create all tables in an in-memory SQLite DB once per test session., Yield a fresh async session, rolling back after each test., Replace the FastAPI `get_db` dependency with one that returns the     test sessi (+2 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (7): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent

### Community 10 - "seed_data.py"
Cohesion: 0.23
Nodes (14): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., seed_citizen_reports() (+6 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.14
Nodes (20): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, ingest_citizen_report(), ingest_satellite_polygon() (+12 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 13 - "test_schemas.py"
Cohesion: 0.25
Nodes (7): Unit tests for Pydantic schemas.  Validates that models accept valid input and r, Address without lat/lon should be accepted (geocoded later)., Smoke-test the state machine transition table., test_citizen_report_input_address_only(), test_citizen_report_input_valid(), test_confidence_bounds(), test_lifecycle_transition_map()

### Community 14 - "incidents.py"
Cohesion: 0.33
Nodes (5): get_incident(), query_incidents(), Incidents query router., Fetch a verified incident cluster by ID.      TODO (Phase 2): query Qdrant for t, Return incidents within `radius` metres of (lat, lon).      TODO (Phase 2): geo-

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VerifiedIncident` connect `VerifiedIncident` to `VerificationAgent`, `test_schemas.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `ProtoIncident` connect `📦 Data schema` to `VerificationAgent`, `VerifiedIncident`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `SituationalAgent` connect `📦 Data schema` to `VerifiedIncident`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `ProtoIncident` (e.g. with `SituationalAgent` and `VerificationAgent`) actually correct?**
  _`ProtoIncident` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DisasterMesh backend package.`, `Agents package — six-agent pipeline.`, `Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders` to the rest of the system?**
  _110 weakly-connected nodes found - possible documentation gaps or missing edges._