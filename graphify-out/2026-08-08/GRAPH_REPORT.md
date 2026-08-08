# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 43 files · ~18,400 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 468 nodes · 769 edges · 37 communities (29 shown, 8 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 111 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `55fbb43a`
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
- test_verification_integration.py
- .verify
- .upsert
- FastAPI
- vector_store.py
- db.py
- main.py
- QdrantClient

## God Nodes (most connected - your core abstractions)
1. `ProtoIncident` - 30 edges
2. `VectorStore` - 26 edges
3. `SituationalAgent` - 26 edges
4. `VerificationAgent` - 21 edges
5. `VerifiedIncident` - 20 edges
6. `_mock_agent()` - 20 edges
7. `🌐 DisasterMesh` - 19 edges
8. `_proto()` - 17 edges
9. `_ingest()` - 14 edges
10. `_proto()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `VectorStore` --uses--> `VerifiedIncident`  [INFERRED]
  backend/app/agents/vector_store.py → backend/app/schemas.py
- `VerificationAgent` --uses--> `VectorStore`  [INFERRED]
  backend/app/agents/verification.py → backend/app/agents/vector_store.py
- `_index_in_vector_store()` --calls--> `get_vector_store()`  [INFERRED]
  backend/app/routers/ingest.py → backend/app/agents/vector_store.py

## Import Cycles
- None detected.

## Communities (37 total, 8 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.06
Nodes (33): AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_db(), _get_engine(), get_qdrant_client() (+25 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (51): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+43 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.23
Nodes (10): OrchestratorAgent, Dispatch optimizer using Google OR-Tools CP-SAT / routing solver.      Algorithm, Run OR-Tools optimizer and return optimal assignments.          TODO (Phase 5):, Cost = ETA_seconds × priority_weight.         Priority weights: P1=4, P2=3, P3=2, Return available responders within radius of the incident,         filtered by c, Run the VerificationAgent 3D clustering & deduplication pipeline on a ProtoIncid, verify_proto_incident(), Responder (+2 more)

### Community 7 - "schemas.py"
Cohesion: 0.14
Nodes (22): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, _index_in_vector_store(), ingest_citizen_report() (+14 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.22
Nodes (12): Return the total number of points in the collection., LangChain-based vector store backed by Qdrant.      Wraps QdrantVectorStore for, VectorStore, ProtoIncident, Normalized incident before verification and deduplication., memory_vector_store(), Integration tests for VectorStore with Qdrant — Phase 2.  Uses an in-memory Qdra, Create a fresh in-memory VectorStore for each test. (+4 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.13
Nodes (15): get_verification_agent(), datetime, Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Main entry point: verify + deduplicate a proto-incident.          Steps, Determine which cluster to join (or create a new one).          Collect cluster_, Confidence = corroboration_factor × cross_source_bonus × stale_penalty, Choose the most authoritative / recent representative.          Priority order:, Return the shared VerificationAgent singleton. (+7 more)

### Community 10 - "seed_data.py"
Cohesion: 0.23
Nodes (14): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., seed_citizen_reports() (+6 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.17
Nodes (10): async_sessionmaker, db_session(), patch_get_db(), patch_init_db(), conftest.py for unit tests.  Provides an in-memory SQLite database and in-memory, Create all tables in an in-memory SQLite DB once per test session., Yield a fresh async session, rolling back after each test., Replace the FastAPI `get_db` dependency with one that returns the     test sessi (+2 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 13 - "CitizenReportInput"
Cohesion: 0.31
Nodes (7): Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d, IncidentStatus, Priority, Canonical Pydantic schemas for DisasterMesh.  These models are the shared langua, ResponderCapability, SourceType, StrEnum

### Community 14 - "incidents.py"
Cohesion: 0.10
Nodes (18): EmbeddingService, get_embedding_service(), get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Return the shared EmbeddingService singleton., Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow (+10 more)

### Community 22 - "SatellitePolygonInput"
Cohesion: 0.19
Nodes (11): get_vector_store(), Return the shared VectorStore singleton (initialised in main.py lifespan)., EmbeddingService, get_incident(), query_incidents(), Return proto incidents within `radius` metres of (lat, lon)., Search incidents by semantic similarity using LangChain embeddings & Qdrant., Fetch a proto incident by ID from Qdrant vector store and run the     Verificati (+3 more)

### Community 23 - "SensorStreamInput"
Cohesion: 0.25
Nodes (5): Resource Agent — Agent 4.  Responsibilities:   - Maintain live responder registr, Tracks and queries the responder registry., TODO (Phase 5): update responder GPS in DB and Redis., TODO (Phase 5): toggle responder availability., ResourceAgent

### Community 24 - "SocialPostInput"
Cohesion: 0.33
Nodes (4): Any, Find ProtoIncident payloads (and optional vectors) within geo radius + optional, Fetch a payload by proto_id., Return ``(payload, vector)`` for every point whose ``proto_id`` payload

### Community 25 - "AsyncSession"
Cohesion: 0.29
Nodes (5): Victim Agent — Agent 3.  Responsibilities:   - Extract needs (medical, shelter,, Extracts needs and computes severity for verified incidents., Assess needs and severity for a verified incident.          TODO (Phase 4): impl, VictimAgent, SeverityAssessment

### Community 26 - "CommunicationAgent"
Cohesion: 0.20
Nodes (7): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, Assignment

### Community 27 - "test_schemas.py"
Cohesion: 0.25
Nodes (7): Unit tests for Pydantic schemas.  Validates that models accept valid input and r, Address without lat/lon should be accepted (geocoded later)., Smoke-test the state machine transition table., test_citizen_report_input_address_only(), test_citizen_report_input_valid(), test_confidence_bounds(), test_lifecycle_transition_map()

### Community 28 - "AsyncSession"
Cohesion: 0.06
Nodes (54): Step-function penalty based on how old the proto-incident timestamp is., Distance in metres between two lat/lon points (great-circle)., _mock_agent(), _proto(), Unit tests for VerificationAgent — Phase 3.  All tests mock VectorStore and Embe, Delhi (28.6139, 77.2090) → Agra (27.1767, 78.0081) ≈ 178 km ±10%., A point displaced ~140 m north should be within the 150 m window., A point displaced ~200 m north should be outside the 150 m window. (+46 more)

### Community 29 - "test_verification_integration.py"
Cohesion: 0.12
Nodes (27): embedding_service(), _ingest(), _now(), _proto(), datetime, EmbeddingService, Integration tests for VerificationAgent — Phase 3.  Uses an in-memory Qdrant ins, A satellite + 3× SMS cluster should have higher confidence than an     SMS-only (+19 more)

### Community 30 - ".verify"
Cohesion: 0.33
Nodes (4): Create a lone (single-member) cluster for a proto-incident that cannot         p, Fast keyword-based needs extraction (bilingual)., NeedsProfile, test_verified_incident_defaults()

### Community 31 - ".upsert"
Cohesion: 0.33
Nodes (4): Store a ProtoIncident and its pre-computed embedding in Qdrant., Persist a :class:`~app.schemas.VerifiedIncident` back into the Qdrant         co, Convert a UUID string to an integer suitable as a Qdrant point ID., _uuid_to_int()

### Community 32 - "FastAPI"
Cohesion: 0.40
Nodes (4): EmbeddingService, Fresh in-memory Qdrant per test so tests are fully isolated., vector_store(), QdrantClient

### Community 33 - "vector_store.py"
Cohesion: 0.22
Nodes (7): _haversine_m(), _proto_to_document(), Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Semantic similarity search using LangChain interface.          Returns list of (, Great-circle distance in metres between two lat/lon points., Convert a ProtoIncident to a LangChain Document.      page_content  = the text u, Document

### Community 38 - "QdrantClient"
Cohesion: 0.25
Nodes (6): init_vector_store(), Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Initialise the VectorStore singleton and ensure the Qdrant collection exists., memory_vector_store(), Initialize an in-memory VectorStore for unit tests., QdrantVectorStore

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ProtoIncident` connect `CommunicationAgent` to `vector_store.py`, `📦 Data schema`, `VerifiedIncident`, `schemas.py`, `VerificationAgent`, `CitizenReportInput`, `incidents.py`, `SatellitePolygonInput`, `AsyncSession`, `test_verification_integration.py`, `.verify`, `.upsert`?**
  _High betweenness centrality (0.150) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `CommunicationAgent` to `FastAPI`, `vector_store.py`, `QdrantClient`, `VerifiedIncident`, `VerificationAgent`, `SatellitePolygonInput`, `SocialPostInput`, `test_verification_integration.py`, `.upsert`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Why does `VerifiedIncident` connect `VerifiedIncident` to `CommunicationAgent`, `VerificationAgent`, `CitizenReportInput`, `SatellitePolygonInput`, `SensorStreamInput`, `AsyncSession`, `CommunicationAgent`, `test_schemas.py`, `.verify`, `.upsert`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `ProtoIncident` (e.g. with `EmbeddingService` and `SituationalAgent`) actually correct?**
  _`ProtoIncident` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `VectorStore` (e.g. with `ProtoIncident` and `VerifiedIncident`) actually correct?**
  _`VectorStore` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerificationAgent` (e.g. with `VectorStore` and `ClusterMatchResult`) actually correct?**
  _`VerificationAgent` has 7 INFERRED edges - model-reasoned connections that need verification._