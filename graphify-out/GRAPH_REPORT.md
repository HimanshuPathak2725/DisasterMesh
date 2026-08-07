# Graph Report - DisasterMesh  (2026-08-07)

## Corpus Check
- 34 files · ~7,825 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 227 nodes · 296 edges · 22 communities (16 shown, 6 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1fcc0ead`
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
- Local Setup Guide
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
1. `🌐 DisasterMesh` - 19 edges
2. `VerifiedIncident` - 16 edges
3. `SituationalAgent` - 13 edges
4. `ProtoIncident` - 11 edges
5. `VictimAgent` - 9 edges
6. `Local Setup Guide` - 9 edges
7. `CommunicationAgent` - 8 edges
8. `VerificationAgent` - 8 edges
9. `Contributing to DisasterMesh` - 8 edges
10. `OrchestratorAgent` - 7 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `VerificationAgent` --uses--> `ProtoIncident`  [INFERRED]
  backend/app/agents/verification.py → backend/app/schemas.py
- `VerificationAgent` --uses--> `VerifiedIncident`  [INFERRED]
  backend/app/agents/verification.py → backend/app/schemas.py
- `VictimAgent` --uses--> `VerifiedIncident`  [INFERRED]
  backend/app/agents/victim.py → backend/app/schemas.py

## Import Cycles
- None detected.

## Communities (22 total, 6 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.07
Nodes (22): AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_qdrant_client(), get_redis_client(), Database and service client factories.  Qdrant:  local file mode by default (no (+14 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.10
Nodes (25): Normalizes all incoming data streams into ProtoIncident objects., TODO (Phase 1): geocode, language-detect, normalize., TODO (Phase 1): extract geo from text, normalize., TODO (Phase 1): extract centroid from GeoJSON, normalize., TODO (Phase 1): threshold check, normalize., TODO (Phase 1): Nominatim lookup with Hindi transliteration., TODO (Phase 1): langdetect or fasttext., SituationalAgent (+17 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.10
Nodes (20): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d (+12 more)

### Community 7 - "schemas.py"
Cohesion: 0.13
Nodes (15): Resource Agent — Agent 4.  Responsibilities:   - Maintain live responder registr, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Victim Agent — Agent 3.  Responsibilities:   - Extract needs (medical, shelter,, Extracts needs and computes severity for verified incidents., Assess needs and severity for a verified incident.          TODO (Phase 4): impl, Fast keyword-based needs extraction (bilingual)., VictimAgent, NeedsProfile (+7 more)

### Community 8 - "Local Setup Guide"
Cohesion: 0.13
Nodes (14): 1. Clone and enter the repo, 2. Create a virtual environment, 3. Install dependencies, 4. Configure environment variables, 5. Start the backend, Backend setup, Frontend setup (Phase 8+), Local Setup Guide (+6 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (7): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent

### Community 10 - "seed_data.py"
Cohesion: 0.27
Nodes (9): Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, TODO (Phase 1): generate realistic Hindi/English SMS reports., TODO (Phase 1): generate realistic tweet-style posts., TODO (Phase 1): generate Sentinel-2 GeoJSON flood polygons., seed_citizen_reports(), seed_satellite_polygons(), seed_social_posts(), _write() (+1 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.22
Nodes (8): 🗂️ Architecture decision records (ADRs), 🌿 Branch naming, 🤝 Code of conduct, 🎨 Code style, ✅ Commit message style, Contributing to DisasterMesh, 🔁 Pull Request checklist, 🧪 Running the test suite locally

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
- **45 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `🌿 Branch naming`, `✅ Commit message style` (+40 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VerifiedIncident` connect `VerifiedIncident` to `VerificationAgent`, `test_schemas.py`, `📦 Data schema`, `schemas.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `ProtoIncident` connect `📦 Data schema` to `VerificationAgent`, `schemas.py`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `SituationalAgent` connect `📦 Data schema` to `schemas.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ProtoIncident` (e.g. with `SituationalAgent` and `VerificationAgent`) actually correct?**
  _`ProtoIncident` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `DisasterMesh backend package.`, `Agents package — six-agent pipeline.`, `Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders` to the rest of the system?**
  _109 weakly-connected nodes found - possible documentation gaps or missing edges._