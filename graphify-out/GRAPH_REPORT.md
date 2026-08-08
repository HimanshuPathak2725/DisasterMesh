# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 55 files · ~28,860 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 720 nodes · 1378 edges · 43 communities (34 shown, 9 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 275 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `58cb3f44`
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
- conftest.py
- main.py
- get_redis_client
- init_vector_store
- get_embedding_service
- .search_nearby
- main.py
- embeddings.py
- get_qdrant_client_sync

## God Nodes (most connected - your core abstractions)
1. `VictimAgent` - 57 edges
2. `ResourceAgent` - 42 edges
3. `VerifiedIncident` - 42 edges
4. `NeedsProfile` - 36 edges
5. `ProtoIncident` - 31 edges
6. `VectorStore` - 30 edges
7. `Responder` - 29 edges
8. `SituationalAgent` - 26 edges
9. `OrchestratorAgent` - 25 edges
10. `VerificationAgent` - 22 edges

## Surprising Connections (you probably didn't know these)
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
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

## Communities (43 total, 9 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.67
Nodes (3): AsyncQdrantClient, get_qdrant_client(), Return a cached Qdrant client.      - QDRANT_URL is set  → connect to cloud / se

### Community 5 - "📦 Data schema"
Cohesion: 0.05
Nodes (59): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+51 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.06
Nodes (57): get_resource_agent(), _haversine_m(), AsyncSession, Resource Agent — Agent 4.  Responsibilities:   - Maintain live responder registr, Return all responders, optionally filtered by status., Fetch a single responder by id; returns None if not found., Update a responder's GPS position.          Returns the updated Responder, or No, Update a responder's operational status.          When transitioning back to 'av (+49 more)

### Community 7 - "schemas.py"
Cohesion: 0.12
Nodes (24): AuditLog, Base, DispatchRecord, SQLAlchemy ORM models for DisasterMesh.  Tables ------ raw_ingestion_records  —, Immutable record of each assignment made by the Orchestrator Agent.      Created, Persists the raw payload **and** the normalised ProtoIncident produced     by th, Immutable append-only audit trail — captures who/what/when for every     signifi, RawIngestionRecord (+16 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.14
Nodes (11): _haversine_m(), _proto_to_document(), Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Store a ProtoIncident and its pre-computed embedding in Qdrant., Semantic similarity search using LangChain interface.          Returns list of (, Persist a :class:`~app.schemas.VerifiedIncident` back into the Qdrant         co, Great-circle distance in metres between two lat/lon points., Convert a UUID string to an integer suitable as a Qdrant point ID. (+3 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.05
Nodes (69): CommunicationAgent, Communication Agent — Agent 6.  Responsibilities:   - Notify assigned responders, Handles notifications and incident lifecycle transitions., SMS the responder with assignment details.          TODO (Phase 6): Twilio clien, Notify the original reporter of status updates.          TODO (Phase 6): Twilio, Apply a lifecycle transition.          Raises ValueError for invalid transitions, _build_dispatch_graph(), _cap_score() (+61 more)

### Community 10 - "seed_data.py"
Cohesion: 0.20
Nodes (16): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., Generate 8 mock responder teams with diverse capabilities. (+8 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 13 - "CitizenReportInput"
Cohesion: 0.09
Nodes (24): get_intake_parser(), IntakeParserAgent, Intake Parser Agent — LLM Smart Intake Layer (Phase 4.5).  Uses LangChain's Chat, Return the shared IntakeParserAgent singleton., Parses free-text crisis reports into structured ParsedIntake using ChatGroq., Return True if GROQ_API_KEY is configured., Parse raw unstructured text using Groq LLM via LangChain.          Returns, ParsedIntake (+16 more)

### Community 14 - "incidents.py"
Cohesion: 0.09
Nodes (18): EmbeddingService, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Async embedding service built on LangChain's HuggingFaceEmbeddings.      All pub, Encode a single text string into a 384-dim float list.          Uses LangChain's, Embed a ProtoIncident using text + optional location context.          Appending, Main entry point: verify + deduplicate a proto-incident.          Steps, Determine which cluster to join (or create a new one).          Collect cluster_ (+10 more)

### Community 22 - "SatellitePolygonInput"
Cohesion: 0.09
Nodes (20): get_vector_store(), Return the shared VectorStore singleton (initialised in main.py lifespan)., get_verification_agent(), datetime, Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s, Return the shared VerificationAgent singleton., get_incident(), query_incidents() (+12 more)

### Community 23 - "SensorStreamInput"
Cohesion: 0.15
Nodes (18): _assess_body(), Integration tests for the VictimAgent assess endpoint — Phase 4.  Tests the full, Medical + rescue text in Delhi high-density zone → P1 or P2., Empty text → all needs=False, so base_needs_score=0.     Formula: (0 + 1.0 + pop, Response body must include all 6 scoring-factor keys., 3-source cluster should score higher than a 1-source cluster (same text)., Including satellite in provenance triggers the satellite_area factor., Valid request → 200 with well-formed SeverityAssessment JSON. (+10 more)

### Community 24 - "SocialPostInput"
Cohesion: 0.16
Nodes (16): Return the total number of points in the collection., LangChain-based vector store backed by Qdrant.      Wraps QdrantVectorStore for, VectorStore, ProtoIncident, Normalized incident before verification and deduplication., memory_vector_store(), Integration tests for VectorStore with Qdrant — Phase 2.  Uses an in-memory Qdra, Create a fresh in-memory VectorStore for each test. (+8 more)

### Community 25 - "AsyncSession"
Cohesion: 0.12
Nodes (35): Extracts needs and computes severity for verified incidents., VictimAgent, agent(), _incident(), Unit tests for VictimAgent — Phase 4.  All tests are fully isolated: no Qdrant,, Build a minimal VerifiedIncident for testing., test_assess_factors_dict_keys(), test_assess_medical_rescue_delhi_is_high_priority() (+27 more)

### Community 26 - "CommunicationAgent"
Cohesion: 0.20
Nodes (8): get_intake_queue(), IntakeQueue, Any, Intake Queue — Redis-backed retry queue for pending LLM intake parsing tasks (Ph, Return the shared IntakeQueue singleton., Queue for retrying failed LLM intake parsing requests., Enqueue a report item for background LLM parsing retry., Process pending queued intake items.          Attempt to parse each item via Int

### Community 27 - "test_schemas.py"
Cohesion: 0.12
Nodes (15): Convert a NeedsProfile to the capability dict expected by the solver.          `, NeedsProfile, Completely unrelated text → all needs False., Evacuation=True but not (medical AND rescue) → 1.3, not 1.5., Even with extreme inputs the score must never exceed 1.0., test_assess_empty_text_no_needs(), test_base_needs_score_full(), test_base_needs_score_half() (+7 more)

### Community 28 - "AsyncSession"
Cohesion: 0.06
Nodes (54): Step-function penalty based on how old the proto-incident timestamp is., Distance in metres between two lat/lon points (great-circle)., _mock_agent(), _proto(), Unit tests for VerificationAgent — Phase 3.  All tests mock VectorStore and Embe, Delhi (28.6139, 77.2090) → Agra (27.1767, 78.0081) ≈ 178 km ±10%., A point displaced ~140 m north should be within the 150 m window., A point displaced ~200 m north should be outside the 150 m window. (+46 more)

### Community 29 - "test_verification_integration.py"
Cohesion: 0.14
Nodes (24): _ingest(), _now(), _proto(), datetime, Integration tests for VerificationAgent — Phase 3.  Uses an in-memory Qdrant ins, A satellite + 3× SMS cluster should have higher confidence than an     SMS-only, A report 300 m away from an existing cluster should land in a     different clus, An identical report that is 35 minutes old (outside the 30-min window)     shoul (+16 more)

### Community 30 - ".verify"
Cohesion: 0.12
Nodes (8): Assess needs and severity for a verified incident cluster.          Parameters, Fast bilingual keyword-based needs extraction., Fraction of need flags that are True (6 total).          Returns a value in [0.0, Keyword severity multiplier.          Medical + Rescue → 1.5  (life-threatening, Return 0.6 when a satellite source is present in the cluster's         provenanc, Multi-source corroboration bonus: 1.0 + 0.20 × (N − 1).          N=1 → 1.0  (sin, Temporal escalation factor.          An incident still generating active reports, Map a severity score in [0, 1] to a P1–P4 priority label.

### Community 31 - ".upsert"
Cohesion: 0.33
Nodes (8): get_db(), _get_engine(), _get_session_factory(), init_db(), AsyncSession, Database and service client factories.  Qdrant:      local file mode by default, Create all ORM tables on startup (idempotent).      Called once from the FastAPI, FastAPI dependency — yields an async DB session per request.      Usage in a rou

### Community 33 - "vector_store.py"
Cohesion: 0.15
Nodes (11): get_victim_agent(), _in_bbox(), Victim Agent — Agent 3.  Responsibilities:   - Extract needs (medical, shelter,, Return the shared VictimAgent singleton., Return True if (lat, lon) falls inside *bbox*., Population-density weight for the incident location.          High-density urban, assess_incident(), Run the VictimAgent needs-extraction and multi-factor severity scoring     pipel (+3 more)

### Community 34 - "conftest.py"
Cohesion: 0.17
Nodes (10): async_sessionmaker, db_session(), patch_get_db(), patch_init_db(), Root conftest.py for all tests (unit and integration).  Provides an in-memory SQ, Create all tables in an in-memory SQLite DB once per test session., Yield a fresh async session, rolling back after each test., Replace the FastAPI `get_db` dependency with one that returns the     test sessi (+2 more)

### Community 36 - "get_redis_client"
Cohesion: 0.18
Nodes (10): get_settings(), Return cached settings singleton., Settings, get_redis_client(), Return a cached async Redis client.      Uses REDIS_URL from .env (Upstash redis, health(), Returns 200 when the API is up. Used by CI and load balancers., HealthResponse (+2 more)

### Community 37 - "init_vector_store"
Cohesion: 0.20
Nodes (7): init_vector_store(), QdrantClient, Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Initialise the VectorStore singleton and ensure the Qdrant collection exists., memory_vector_store(), Initialize an in-memory VectorStore for tests., QdrantVectorStore

### Community 38 - "get_embedding_service"
Cohesion: 0.33
Nodes (8): get_embedding_service(), Return the shared EmbeddingService singleton., Unit tests for EmbeddingService — Phase 2.  Run:     cd backend     pytest app/t, test_cosine_similarity(), test_embed_batch(), test_embed_incident_with_and_without_coords(), test_embed_text_english_and_hindi(), test_embed_text_returns_384_dims()

### Community 39 - ".search_nearby"
Cohesion: 0.25
Nodes (5): Any, Find ProtoIncident payloads (and optional vectors) within geo radius + optional, Fetch a payload by proto_id., Return the payload dict for the *verified* point with the given cluster_id., Return ``(payload, vector)`` for every point whose ``proto_id`` payload

### Community 40 - "main.py"
Cohesion: 0.38
Nodes (4): DisasterMesh backend — application settings.  Loaded from environment variables, lifespan(), DisasterMesh FastAPI application entrypoint.  Run locally:     cd backend     uv, FastAPI

### Community 41 - "embeddings.py"
Cohesion: 0.33
Nodes (4): get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow, HuggingFaceEmbeddings

### Community 42 - "get_qdrant_client_sync"
Cohesion: 0.67
Nodes (3): get_qdrant_client_sync(), QdrantClient, Return a cached synchronous Qdrant client.      Required by langchain-qdrant's Q

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VerifiedIncident` connect `VerificationAgent` to `vector_store.py`, `📦 Data schema`, `VerifiedIncident`, `CommunicationAgent`, `incidents.py`, `SatellitePolygonInput`, `SocialPostInput`, `AsyncSession`, `.verify`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `ProtoIncident` connect `SocialPostInput` to `📦 Data schema`, `VerifiedIncident`, `schemas.py`, `CommunicationAgent`, `VerificationAgent`, `get_embedding_service`, `incidents.py`, `SatellitePolygonInput`, `AsyncSession`, `test_verification_integration.py`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `SocialPostInput` to `init_vector_store`, `.search_nearby`, `CommunicationAgent`, `VerificationAgent`, `incidents.py`, `SatellitePolygonInput`, `test_verification_integration.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `VictimAgent` (e.g. with `NeedsProfile` and `Priority`) actually correct?**
  _`VictimAgent` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `ResourceAgent` (e.g. with `DispatchState` and `OrchestratorAgent`) actually correct?**
  _`ResourceAgent` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `DispatchState`) actually correct?**
  _`VerifiedIncident` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `NeedsProfile` (e.g. with `DispatchState` and `OrchestratorAgent`) actually correct?**
  _`NeedsProfile` has 30 INFERRED edges - model-reasoned connections that need verification._