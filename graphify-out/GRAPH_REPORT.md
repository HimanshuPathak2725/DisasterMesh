# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 38 files · ~12,772 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 350 nodes · 488 edges · 43 communities (16 shown, 27 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 69 edges (avg confidence: 0.7)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3f532ad9`
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
- CitizenReportInput
- SatellitePolygonInput
- SensorStreamInput
- SocialPostInput
- IngestResponse
- ProtoIncident
- Any
- AsyncSession
- test_schemas.py
- ProtoIncident
- ProtoIncident
- ProtoIncident
- QdrantClient
- CitizenReportInput
- SatellitePolygonInput
- SensorStreamInput
- SocialPostInput

## God Nodes (most connected - your core abstractions)
1. `SituationalAgent` - 26 edges
2. `🌐 DisasterMesh` - 19 edges
3. `ProtoIncident` - 17 edges
4. `VerifiedIncident` - 16 edges
5. `VectorStore` - 14 edges
6. `CitizenReportInput` - 12 edges
7. `EmbeddingService` - 11 edges
8. `VictimAgent` - 9 edges
9. `_lookup_landmark()` - 8 edges
10. `_detect_language()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `EmbeddingService` --uses--> `ProtoIncident`  [INFERRED]
  backend/app/agents/embeddings.py → backend/app/schemas.py
- `VectorStore` --uses--> `EmbeddingService`  [INFERRED]
  backend/app/agents/vector_store.py → backend/app/agents/embeddings.py
- `test_landmark_case_insensitive()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py

## Import Cycles
- None detected.

## Communities (43 total, 27 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.08
Nodes (20): get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, lifespan(), DisasterMesh FastAPI application entrypoint.  Run locally:     cd backend     uv, dispatch_incident(), Dispatch router — trigger responder assignment. (+12 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (53): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+45 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.07
Nodes (34): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d (+26 more)

### Community 7 - "schemas.py"
Cohesion: 0.10
Nodes (16): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, db_session(), patch_get_db() (+8 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.09
Nodes (20): get_vector_store(), _haversine_m(), init_vector_store(), _proto_to_document(), Any, Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Store a ProtoIncident and its pre-computed embedding in Qdrant.          We pass (+12 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (7): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent

### Community 10 - "seed_data.py"
Cohesion: 0.23
Nodes (14): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., seed_citizen_reports() (+6 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.09
Nodes (30): async_sessionmaker, AsyncQdrantClient, AsyncSession, get_db(), _get_engine(), get_qdrant_client(), get_qdrant_client_sync(), get_redis_client() (+22 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 14 - "incidents.py"
Cohesion: 0.12
Nodes (13): EmbeddingService, get_embedding_service(), get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Return the shared EmbeddingService singleton., Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow (+5 more)

### Community 34 - "test_schemas.py"
Cohesion: 0.22
Nodes (8): Unit tests for Pydantic schemas.  Validates that models accept valid input and r, Address without lat/lon should be accepted (geocoded later)., Smoke-test the state machine transition table., test_citizen_report_input_address_only(), test_citizen_report_input_valid(), test_confidence_bounds(), test_lifecycle_transition_map(), test_verified_incident_defaults()

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ProtoIncident` connect `📦 Data schema` to `CommunicationAgent`, `VerificationAgent`, `incidents.py`, `VerifiedIncident`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `CommunicationAgent` to `📦 Data schema`, `incidents.py`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `VerifiedIncident` connect `VerifiedIncident` to `VerificationAgent`, `test_schemas.py`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `ProtoIncident` (e.g. with `EmbeddingService` and `SituationalAgent`) actually correct?**
  _`ProtoIncident` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `VectorStore` (e.g. with `EmbeddingService` and `ProtoIncident`) actually correct?**
  _`VectorStore` has 2 INFERRED edges - model-reasoned connections that need verification._