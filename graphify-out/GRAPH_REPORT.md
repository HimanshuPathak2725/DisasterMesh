# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 41 files · ~13,566 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 358 nodes · 557 edges · 27 communities (20 shown, 7 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 98 edges (avg confidence: 0.73)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e4014337`
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
- QdrantClient

## God Nodes (most connected - your core abstractions)
1. `SituationalAgent` - 26 edges
2. `ProtoIncident` - 22 edges
3. `VectorStore` - 20 edges
4. `🌐 DisasterMesh` - 19 edges
5. `VerifiedIncident` - 16 edges
6. `get_embedding_service()` - 13 edges
7. `CitizenReportInput` - 12 edges
8. `EmbeddingService` - 11 edges
9. `VictimAgent` - 9 edges
10. `_persist()` - 9 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `EmbeddingService` --uses--> `ProtoIncident`  [INFERRED]
  backend/app/agents/embeddings.py → backend/app/schemas.py
- `VectorStore` --uses--> `EmbeddingService`  [INFERRED]
  backend/app/agents/vector_store.py → backend/app/agents/embeddings.py
- `_index_in_vector_store()` --calls--> `get_embedding_service()`  [INFERRED]
  backend/app/routers/ingest.py → backend/app/agents/embeddings.py
- `test_search_nearby_geo_radius()` --calls--> `get_embedding_service()`  [INFERRED]
  backend/app/tests/integration/test_vector_store.py → backend/app/agents/embeddings.py

## Import Cycles
- None detected.

## Communities (27 total, 7 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.07
Nodes (32): AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_db(), _get_engine(), get_qdrant_client() (+24 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (51): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+43 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.06
Nodes (42): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d (+34 more)

### Community 7 - "schemas.py"
Cohesion: 0.14
Nodes (22): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, _index_in_vector_store(), ingest_citizen_report() (+14 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.17
Nodes (10): _haversine_m(), _proto_to_document(), Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Store a ProtoIncident and its pre-computed embedding in Qdrant., Semantic similarity search using LangChain interface.          Returns list of (, Great-circle distance in metres between two lat/lon points., Convert a UUID string to an integer suitable as a Qdrant point ID., Convert a ProtoIncident to a LangChain Document.      page_content  = the text u (+2 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (7): Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, Main entry point: verify + deduplicate a proto-incident.          TODO (Phase 3), TODO (Phase 3): Qdrant geo + time filter., TODO (Phase 3): corroboration × cross-source bonus × stale penalty., Distance in metres between two lat/lon points., VerificationAgent

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
Cohesion: 0.22
Nodes (12): Return the total number of points in the collection., LangChain-based vector store backed by Qdrant.      Wraps QdrantVectorStore for, VectorStore, ProtoIncident, Normalized incident before verification and deduplication., memory_vector_store(), Integration tests for VectorStore with Qdrant — Phase 2.  Uses an in-memory Qdra, Create a fresh in-memory VectorStore for each test. (+4 more)

### Community 14 - "incidents.py"
Cohesion: 0.14
Nodes (10): EmbeddingService, get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow, Async embedding service built on LangChain's HuggingFaceEmbeddings.      All pub, Encode a single text string into a 384-dim float list.          Uses LangChain's (+2 more)

### Community 22 - "SatellitePolygonInput"
Cohesion: 0.24
Nodes (9): get_vector_store(), Return the shared VectorStore singleton (initialised in main.py lifespan)., get_incident(), query_incidents(), Incidents query router — Phase 2 vector memory integration., Search incidents by semantic similarity using LangChain embeddings & Qdrant., Fetch a proto incident by ID from Qdrant vector store., Return proto incidents within `radius` metres of (lat, lon). (+1 more)

### Community 23 - "SensorStreamInput"
Cohesion: 0.33
Nodes (8): get_embedding_service(), Return the shared EmbeddingService singleton., Unit tests for EmbeddingService — Phase 2.  Run:     cd backend     pytest app/t, test_cosine_similarity(), test_embed_batch(), test_embed_incident_with_and_without_coords(), test_embed_text_english_and_hindi(), test_embed_text_returns_384_dims()

### Community 24 - "SocialPostInput"
Cohesion: 0.40
Nodes (3): Any, Find ProtoIncident payloads within geo radius + optional time window.          S, Fetch a payload by proto_id using metadata filter.

### Community 38 - "QdrantClient"
Cohesion: 0.20
Nodes (7): init_vector_store(), QdrantClient, Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Initialise the VectorStore singleton and ensure the Qdrant collection exists., memory_vector_store(), Initialize an in-memory VectorStore for unit tests., QdrantVectorStore

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ProtoIncident` connect `CitizenReportInput` to `📦 Data schema`, `VerifiedIncident`, `schemas.py`, `CommunicationAgent`, `VerificationAgent`, `incidents.py`, `SensorStreamInput`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `CitizenReportInput` to `QdrantClient`, `CommunicationAgent`, `incidents.py`, `SatellitePolygonInput`, `SocialPostInput`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `VerifiedIncident` connect `VerifiedIncident` to `VerificationAgent`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `ProtoIncident` (e.g. with `EmbeddingService` and `SituationalAgent`) actually correct?**
  _`ProtoIncident` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `VectorStore` (e.g. with `EmbeddingService` and `ProtoIncident`) actually correct?**
  _`VectorStore` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `OrchestratorAgent`) actually correct?**
  _`VerifiedIncident` has 7 INFERRED edges - model-reasoned connections that need verification._