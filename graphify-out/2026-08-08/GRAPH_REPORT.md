# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 38 files · ~12,783 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 349 nodes · 482 edges · 34 communities (15 shown, 19 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 63 edges (avg confidence: 0.73)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7b50fc99`
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

## God Nodes (most connected - your core abstractions)
1. `SituationalAgent` - 20 edges
2. `🌐 DisasterMesh` - 19 edges
3. `VerifiedIncident` - 16 edges
4. `VectorStore` - 13 edges
5. `EmbeddingService` - 10 edges
6. `VictimAgent` - 9 edges
7. `_lookup_landmark()` - 8 edges
8. `_detect_language()` - 8 edges
9. `CommunicationAgent` - 8 edges
10. `VerificationAgent` - 8 edges

## Surprising Connections (you probably didn't know these)
- `VectorStore` --uses--> `EmbeddingService`  [INFERRED]
  backend/app/agents/vector_store.py → backend/app/agents/embeddings.py
- `test_landmark_case_insensitive()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_exact_match()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_hindi()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py
- `test_landmark_substring_match()` --calls--> `_lookup_landmark()`  [INFERRED]
  backend/app/tests/unit/test_situational.py → backend/app/agents/situational.py

## Import Cycles
- None detected.

## Communities (34 total, 19 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.08
Nodes (20): get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, lifespan(), DisasterMesh FastAPI application entrypoint.  Run locally:     cd backend     uv, dispatch_incident(), Dispatch router — trigger responder assignment. (+12 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (52): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, ProtoIncident, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table. (+44 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.06
Nodes (43): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d (+35 more)

### Community 7 - "schemas.py"
Cohesion: 0.10
Nodes (17): async_sessionmaker, AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, db_session() (+9 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.09
Nodes (22): get_vector_store(), _haversine_m(), init_vector_store(), _proto_to_document(), Any, ProtoIncident, QdrantClient, Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the (+14 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.16
Nodes (9): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent, ProtoIncident (+1 more)

### Community 10 - "seed_data.py"
Cohesion: 0.23
Nodes (14): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., seed_citizen_reports() (+6 more)

### Community 11 - "Contributing to DisasterMesh"
Cohesion: 0.09
Nodes (32): AsyncQdrantClient, AsyncSession, get_db(), _get_engine(), get_qdrant_client(), get_qdrant_client_sync(), get_redis_client(), _get_session_factory() (+24 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 14 - "incidents.py"
Cohesion: 0.12
Nodes (13): EmbeddingService, get_embedding_service(), get_langchain_embeddings(), ProtoIncident, Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Return the shared EmbeddingService singleton. (+5 more)

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VerifiedIncident` connect `VerifiedIncident` to `VerificationAgent`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `CommunicationAgent` to `incidents.py`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Why does `EmbeddingService` connect `incidents.py` to `CommunicationAgent`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 12 inferred relationships involving `SituationalAgent` (e.g. with `test_process_citizen_report_address_only()` and `test_process_citizen_report_hindi_language()`) actually correct?**
  _`SituationalAgent` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro`, `Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow`, `Async embedding service built on LangChain's HuggingFaceEmbeddings.      All pub` to the rest of the system?**
  _131 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `🌐 DisasterMesh` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._