# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 49 files · ~23,023 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 596 nodes · 1034 edges · 38 communities (30 shown, 8 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 145 edges (avg confidence: 0.73)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `811c2c12`
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
- get_redis_client
- QdrantClient

## God Nodes (most connected - your core abstractions)
1. `VictimAgent` - 57 edges
2. `ProtoIncident` - 31 edges
3. `VectorStore` - 27 edges
4. `SituationalAgent` - 26 edges
5. `VerifiedIncident` - 25 edges
6. `VerificationAgent` - 22 edges
7. `NeedsProfile` - 22 edges
8. `_mock_agent()` - 20 edges
9. `_incident()` - 19 edges
10. `🌐 DisasterMesh` - 19 edges

## Surprising Connections (you probably didn't know these)
- `test_citizen_report_input_valid()` --calls--> `CitizenReportInput`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `EmbeddingService` --uses--> `ProtoIncident`  [INFERRED]
  backend/app/agents/embeddings.py → backend/app/schemas.py
- `VectorStore` --uses--> `EmbeddingService`  [INFERRED]
  backend/app/agents/vector_store.py → backend/app/agents/embeddings.py
- `VerificationAgent` --uses--> `EmbeddingService`  [INFERRED]
  backend/app/agents/verification.py → backend/app/agents/embeddings.py
- `_index_in_vector_store()` --calls--> `get_embedding_service()`  [INFERRED]
  backend/app/routers/ingest.py → backend/app/agents/embeddings.py

## Import Cycles
- None detected.

## Communities (38 total, 8 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.22
Nodes (8): AsyncQdrantClient, get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_qdrant_client(), Return a cached Qdrant client.      - QDRANT_URL is set  → connect to cloud / se, BaseSettings

### Community 5 - "📦 Data schema"
Cohesion: 0.06
Nodes (51): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+43 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.06
Nodes (41): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, OrchestratorAgent, Orchestrator Agent — Agent 5.  Responsibilities:   - Solve the multi-responder d (+33 more)

### Community 7 - "schemas.py"
Cohesion: 0.14
Nodes (22): AuditLog, Base, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord, _index_in_vector_store(), ingest_citizen_report() (+14 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.22
Nodes (12): Return the total number of points in the collection., LangChain-based vector store backed by Qdrant.      Wraps QdrantVectorStore for, VectorStore, ProtoIncident, Normalized incident before verification and deduplication., memory_vector_store(), Integration tests for VectorStore with Qdrant — Phase 2.  Uses an in-memory Qdra, Create a fresh in-memory VectorStore for each test. (+4 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.17
Nodes (11): Main entry point: verify + deduplicate a proto-incident.          Steps, Determine which cluster to join (or create a new one).          Collect cluster_, Confidence = corroboration_factor × cross_source_bonus × stale_penalty, Choose the most authoritative / recent representative.          Priority order:, Create a lone (single-member) cluster for a proto-incident that cannot         p, Deduplicates and verifies proto-incidents.      Uses three-dimensional clusterin, VerificationAgent, ClusterMatchResult (+3 more)

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
Cohesion: 0.09
Nodes (24): get_intake_parser(), IntakeParserAgent, Intake Parser Agent — LLM Smart Intake Layer (Phase 4.5).  Uses LangChain's Chat, Return the shared IntakeParserAgent singleton., Parses free-text crisis reports into structured ParsedIntake using ChatGroq., Return True if GROQ_API_KEY is configured., Parse raw unstructured text using Groq LLM via LangChain.          Returns, ParsedIntake (+16 more)

### Community 14 - "incidents.py"
Cohesion: 0.12
Nodes (14): EmbeddingService, get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow, Async embedding service built on LangChain's HuggingFaceEmbeddings.      All pub, Encode a single text string into a 384-dim float list.          Uses LangChain's (+6 more)

### Community 22 - "SatellitePolygonInput"
Cohesion: 0.16
Nodes (14): get_vector_store(), Return the shared VectorStore singleton (initialised in main.py lifespan)., get_verification_agent(), Return the shared VerificationAgent singleton., get_incident(), query_incidents(), Return proto incidents within `radius` metres of (lat, lon)., Search incidents by semantic similarity using LangChain embeddings & Qdrant. (+6 more)

### Community 23 - "SensorStreamInput"
Cohesion: 0.15
Nodes (18): _assess_body(), Integration tests for the VictimAgent assess endpoint — Phase 4.  Tests the full, Medical + rescue text in Delhi high-density zone → P1 or P2., Empty text → all needs=False, so base_needs_score=0.     Formula: (0 + 1.0 + pop, Response body must include all 6 scoring-factor keys., 3-source cluster should score higher than a 1-source cluster (same text)., Including satellite in provenance triggers the satellite_area factor., Valid request → 200 with well-formed SeverityAssessment JSON. (+10 more)

### Community 24 - "SocialPostInput"
Cohesion: 0.25
Nodes (6): _haversine_m(), Any, Find ProtoIncident payloads (and optional vectors) within geo radius + optional, Fetch a payload by proto_id., Return ``(payload, vector)`` for every point whose ``proto_id`` payload, Great-circle distance in metres between two lat/lon points.

### Community 25 - "AsyncSession"
Cohesion: 0.05
Nodes (66): get_victim_agent(), _in_bbox(), Victim Agent — Agent 3.  Responsibilities:   - Extract needs (medical, shelter,, Return the shared VictimAgent singleton., Return True if (lat, lon) falls inside *bbox*., Extracts needs and computes severity for verified incidents., Assess needs and severity for a verified incident cluster.          Parameters, Fast bilingual keyword-based needs extraction. (+58 more)

### Community 26 - "CommunicationAgent"
Cohesion: 0.20
Nodes (8): get_intake_queue(), IntakeQueue, Any, Intake Queue — Redis-backed retry queue for pending LLM intake parsing tasks (Ph, Return the shared IntakeQueue singleton., Queue for retrying failed LLM intake parsing requests., Enqueue a report item for background LLM parsing retry., Process pending queued intake items.          Attempt to parse each item via Int

### Community 27 - "test_schemas.py"
Cohesion: 0.33
Nodes (8): get_embedding_service(), Return the shared EmbeddingService singleton., Unit tests for EmbeddingService — Phase 2.  Run:     cd backend     pytest app/t, test_cosine_similarity(), test_embed_batch(), test_embed_incident_with_and_without_coords(), test_embed_text_english_and_hindi(), test_embed_text_returns_384_dims()

### Community 28 - "AsyncSession"
Cohesion: 0.06
Nodes (54): Step-function penalty based on how old the proto-incident timestamp is., Distance in metres between two lat/lon points (great-circle)., _mock_agent(), _proto(), Unit tests for VerificationAgent — Phase 3.  All tests mock VectorStore and Embe, Delhi (28.6139, 77.2090) → Agra (27.1767, 78.0081) ≈ 178 km ±10%., A point displaced ~140 m north should be within the 150 m window., A point displaced ~200 m north should be outside the 150 m window. (+46 more)

### Community 29 - "test_verification_integration.py"
Cohesion: 0.10
Nodes (25): agent(), embedding_service(), _now(), _proto(), datetime, Integration tests for VerificationAgent — Phase 3.  Uses an in-memory Qdrant ins, A satellite + 3× SMS cluster should have higher confidence than an     SMS-only, A report 300 m away from an existing cluster should land in a     different clus (+17 more)

### Community 30 - ".verify"
Cohesion: 0.22
Nodes (7): dispatch_incident(), Dispatch router — trigger responder assignment., Trigger the Orchestrator Agent to assign responders to an incident.      TODO (P, health(), Returns 200 when the API is up. Used by CI and load balancers., HealthResponse, FastAPI

### Community 31 - ".upsert"
Cohesion: 0.33
Nodes (8): get_db(), _get_engine(), _get_session_factory(), init_db(), AsyncSession, Database and service client factories.  Qdrant:      local file mode by default, Create all ORM tables on startup (idempotent).      Called once from the FastAPI, FastAPI dependency — yields an async DB session per request.      Usage in a rou

### Community 33 - "vector_store.py"
Cohesion: 0.17
Nodes (9): _proto_to_document(), Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Store a ProtoIncident and its pre-computed embedding in Qdrant., Semantic similarity search using LangChain interface.          Returns list of (, Persist a :class:`~app.schemas.VerifiedIncident` back into the Qdrant         co, Convert a UUID string to an integer suitable as a Qdrant point ID., Convert a ProtoIncident to a LangChain Document.      page_content  = the text u, _uuid_to_int() (+1 more)

### Community 34 - "db.py"
Cohesion: 0.50
Nodes (4): get_qdrant_client_sync(), QdrantClient, Return a cached synchronous Qdrant client.      Required by langchain-qdrant's Q, lifespan()

### Community 36 - "get_redis_client"
Cohesion: 0.67
Nodes (3): get_redis_client(), Return a cached async Redis client.      Uses REDIS_URL from .env (Upstash redis, Redis

### Community 38 - "QdrantClient"
Cohesion: 0.20
Nodes (7): init_vector_store(), QdrantClient, Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Initialise the VectorStore singleton and ensure the Qdrant collection exists., memory_vector_store(), Initialize an in-memory VectorStore for unit tests., QdrantVectorStore

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ProtoIncident` connect `CommunicationAgent` to `vector_store.py`, `📦 Data schema`, `VerifiedIncident`, `schemas.py`, `VerificationAgent`, `incidents.py`, `SatellitePolygonInput`, `test_schemas.py`, `AsyncSession`, `test_verification_integration.py`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `CommunicationAgent` to `vector_store.py`, `QdrantClient`, `VerifiedIncident`, `VerificationAgent`, `incidents.py`, `SatellitePolygonInput`, `SocialPostInput`, `test_verification_integration.py`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **Why does `VerifiedIncident` connect `VerifiedIncident` to `vector_store.py`, `CommunicationAgent`, `VerificationAgent`, `SatellitePolygonInput`, `AsyncSession`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `VictimAgent` (e.g. with `NeedsProfile` and `Priority`) actually correct?**
  _`VictimAgent` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `ProtoIncident` (e.g. with `EmbeddingService` and `SituationalAgent`) actually correct?**
  _`ProtoIncident` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `VectorStore` (e.g. with `EmbeddingService` and `ProtoIncident`) actually correct?**
  _`VectorStore` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `SituationalAgent` (e.g. with `CitizenReportInput` and `ProtoIncident`) actually correct?**
  _`SituationalAgent` has 18 INFERRED edges - model-reasoned connections that need verification._