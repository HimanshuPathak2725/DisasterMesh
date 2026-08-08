# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 41 files · ~13,629 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 369 nodes · 537 edges · 30 communities (20 shown, 10 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 78 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `93d942fd`
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
- CitizenReportInput
- incidents.py
- __init__.py
- __init__.py
- __init__.py
- SatellitePolygonInput
- SensorStreamInput
- SocialPostInput
- AsyncSession
- CommunicationAgent
- test_schemas.py
- AsyncSession
- QdrantClient

## God Nodes (most connected - your core abstractions)
1. `SituationalAgent` - 26 edges
2. `🌐 DisasterMesh` - 19 edges
3. `VectorStore` - 18 edges
4. `VerifiedIncident` - 16 edges
5. `ProtoIncident` - 14 edges
6. `CitizenReportInput` - 11 edges
7. `EmbeddingService` - 9 edges
8. `VictimAgent` - 9 edges
9. `_index_in_vector_store()` - 8 edges
10. `CommunicationAgent` - 8 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `_index_in_vector_store()` --calls--> `get_vector_store()`  [INFERRED]
  backend/app/routers/ingest.py → backend/app/agents/vector_store.py
- `lifespan()` --calls--> `init_vector_store()`  [INFERRED]
  backend/app/main.py → backend/app/agents/vector_store.py
- `CommunicationAgent` --uses--> `VerifiedIncident`  [INFERRED]
  backend/app/agents/communication.py → backend/app/schemas.py

## Import Cycles
- None detected.

## Communities (30 total, 10 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.10
Nodes (23): async_sessionmaker, AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_db(), _get_engine() (+15 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (54): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+46 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.18
Nodes (11): OrchestratorAgent, Dispatch optimizer using Google OR-Tools CP-SAT / routing solver.      Algorithm, Run OR-Tools optimizer and return optimal assignments.          TODO (Phase 5):, Cost = ETA_seconds × priority_weight.         Priority weights: P1=4, P2=3, P3=2, Tracks and queries the responder registry., Return available responders within radius of the incident,         filtered by c, TODO (Phase 5): update responder GPS in DB and Redis., TODO (Phase 5): toggle responder availability. (+3 more)

### Community 7 - "schemas.py"
Cohesion: 0.17
Nodes (20): AsyncSession, _index_in_vector_store(), ingest_citizen_report(), ingest_satellite_polygon(), ingest_sensor_stream(), ingest_social_post(), _persist(), ProtoIncident (+12 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.07
Nodes (32): Any, _haversine_m(), init_vector_store(), _proto_to_document(), ProtoIncident, Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Store a ProtoIncident and its pre-computed embedding in Qdrant. (+24 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (7): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent

### Community 10 - "seed_data.py"
Cohesion: 0.23
Nodes (14): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., seed_citizen_reports() (+6 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.10
Nodes (16): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, db_session(), patch_get_db() (+8 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.08
Nodes (11): lifespan(), DisasterMesh FastAPI application entrypoint.  Run locally:     cd backend     uv, dispatch_incident(), Dispatch router — trigger responder assignment., Trigger the Orchestrator Agent to assign responders to an incident.      TODO (P, Unit tests for the health check endpoint.  Run:     cd backend     pytest app/te, Unit tests for incidents query router — Phase 2.  Run:     cd backend     pytest, Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u (+3 more)

### Community 13 - "CitizenReportInput"
Cohesion: 0.16
Nodes (10): Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d, Resource Agent — Agent 4.  Responsibilities:   - Maintain live responder registr, health(), Returns 200 when the API is up. Used by CI and load balancers., HealthResponse, IngestResponse, Canonical Pydantic schemas for DisasterMesh.  These models are the shared langua, ResponderCapability (+2 more)

### Community 14 - "incidents.py"
Cohesion: 0.13
Nodes (12): EmbeddingService, get_embedding_service(), get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Return the shared EmbeddingService singleton., Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow (+4 more)

### Community 22 - "SatellitePolygonInput"
Cohesion: 0.24
Nodes (9): get_vector_store(), Return the shared VectorStore singleton (initialised in main.py lifespan)., get_incident(), query_incidents(), Incidents query router — Phase 2 vector memory integration., Search incidents by semantic similarity using LangChain embeddings & Qdrant., Fetch a proto incident by ID from Qdrant vector store., Return proto incidents within `radius` metres of (lat, lon). (+1 more)

### Community 25 - "AsyncSession"
Cohesion: 0.19
Nodes (9): Victim Agent — Agent 3.  Responsibilities:   - Extract needs (medical, shelter,, Extracts needs and computes severity for verified incidents., Assess needs and severity for a verified incident.          TODO (Phase 4): impl, Fast keyword-based needs extraction (bilingual)., VictimAgent, NeedsProfile, Priority, SeverityAssessment (+1 more)

### Community 26 - "CommunicationAgent"
Cohesion: 0.21
Nodes (8): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, Assignment, IncidentStatus

### Community 27 - "test_schemas.py"
Cohesion: 0.25
Nodes (7): Unit tests for Pydantic schemas.  Validates that models accept valid input and r, Address without lat/lon should be accepted (geocoded later)., Smoke-test the state machine transition table., test_citizen_report_input_address_only(), test_citizen_report_input_valid(), test_confidence_bounds(), test_lifecycle_transition_map()

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VectorStore` connect `CommunicationAgent` to `SatellitePolygonInput`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `ProtoIncident` connect `📦 Data schema` to `VerificationAgent`, `CitizenReportInput`, `incidents.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Why does `VerifiedIncident` connect `VerifiedIncident` to `📦 Data schema`, `VerificationAgent`, `CitizenReportInput`, `AsyncSession`, `CommunicationAgent`, `test_schemas.py`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `ProtoIncident` (e.g. with `EmbeddingService` and `SituationalAgent`) actually correct?**
  _`ProtoIncident` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the`, `Great-circle distance in metres between two lat/lon points.`, `Convert a UUID string to an integer suitable as a Qdrant point ID.` to the rest of the system?**
  _139 weakly-connected nodes found - possible documentation gaps or missing edges._