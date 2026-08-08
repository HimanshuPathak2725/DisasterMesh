# Graph Report - DisasterMesh  (2026-08-08)

## Corpus Check
- 62 files · ~38,581 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 921 nodes · 1778 edges · 53 communities (43 shown, 10 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 360 edges (avg confidence: 0.7)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `28bae028`
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
- get_resource_agent
- vector_store.py
- TestNotificationMockMode
- _record_to_schema
- get_settings
- init_vector_store
- TestStateMachine
- .search_nearby
- main.py
- embeddings.py
- get_qdrant_client_sync
- .assess
- assess_incident
- conftest.py
- get_embedding_service
- SourceType
- conftest.py
- test_ingest.py
- main.py
- test_health.py
- get_qdrant_client

## God Nodes (most connected - your core abstractions)
1. `VictimAgent` - 57 edges
2. `VerifiedIncident` - 51 edges
3. `NeedsProfile` - 45 edges
4. `ResourceAgent` - 42 edges
5. `VectorStore` - 32 edges
6. `ProtoIncident` - 31 edges
7. `Responder` - 29 edges
8. `CommunicationAgent` - 28 edges
9. `SituationalAgent` - 26 edges
10. `OrchestratorAgent` - 25 edges

## Surprising Connections (you probably didn't know these)
- `test_confidence_bounds()` --calls--> `VerifiedIncident`  [INFERRED]
  backend/app/tests/unit/test_schemas.py → backend/app/schemas.py
- `CommunicationAgent` --uses--> `CommunicationLog`  [INFERRED]
  backend/app/agents/communication.py → backend/app/models.py
- `CommunicationAgent` --uses--> `DispatchRecord`  [INFERRED]
  backend/app/agents/communication.py → backend/app/models.py
- `CommunicationAgent` --uses--> `ResponderRecord`  [INFERRED]
  backend/app/agents/communication.py → backend/app/models.py
- `CommunicationAgent` --uses--> `AssignedResponderSummary`  [INFERRED]
  backend/app/agents/communication.py → backend/app/schemas.py

## Import Cycles
- None detected.

## Communities (53 total, 10 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.07
Nodes (26): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🙏 Acknowledgements, 🔌 API reference (+18 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.05
Nodes (56): Any, AsyncClient, async_client(), async_client(), async_client(), End-to-End Pipeline Integration Tests — Phase 7.  Validates the complete Disaste, 5 overlapping SMS reports about the Yamuna Bazar flood are ingested via     POST, A Sentinel-2 GeoJSON polygon and 3 SMS reports are ingested.     All 4 should la (+48 more)

### Community 5 - "📦 Data schema"
Cohesion: 0.05
Nodes (59): _detect_language(), _extract_geometry(), _lookup_landmark(), _polygon_centroid(), Any, Situational Agent — Agent 1.  Responsibilities:   - Accept raw inputs from all f, Case-insensitive prefix scan of the landmark table., Compute the centroid of the outer ring of a GeoJSON Polygon.      GeoJSON coordi (+51 more)

### Community 6 - "VerifiedIncident"
Cohesion: 0.21
Nodes (19): Tracks and queries the live responder registry.      All mutations are committed, ResourceAgent, Request body for ``POST /responders``., Request body for ``PUT /responders/{id}/status``., ResponderCreate, StatusUpdate, Unit tests for ResourceAgent (Agent 4) — Phase 5.  Tests responder registration,, test_capability_score_no_required() (+11 more)

### Community 7 - "schemas.py"
Cohesion: 0.08
Nodes (30): get_intake_queue(), IntakeQueue, Any, Intake Queue — Redis-backed retry queue for pending LLM intake parsing tasks (Ph, Return the shared IntakeQueue singleton., Queue for retrying failed LLM intake parsing requests., Enqueue a report item for background LLM parsing retry., Process pending queued intake items.          Attempt to parse each item via Int (+22 more)

### Community 8 - "CommunicationAgent"
Cohesion: 0.14
Nodes (11): _haversine_m(), _proto_to_document(), Vector Store — Phase 2.  Uses LangChain's QdrantVectorStore wrapper so both the, Store a ProtoIncident and its pre-computed embedding in Qdrant., Semantic similarity search using LangChain interface.          Returns list of (, Persist a :class:`~app.schemas.VerifiedIncident` back into the Qdrant         co, Great-circle distance in metres between two lat/lon points., Convert a UUID string to an integer suitable as a Qdrant point ID. (+3 more)

### Community 9 - "VerificationAgent"
Cohesion: 0.25
Nodes (13): OrchestratorAgent, Dispatch optimizer.      Uses a LangGraph StateGraph to manage the dispatch work, Run the LangGraph dispatch pipeline for *incident*.          Parameters, Batch multi-incident dispatch.          Runs the full LangGraph pipeline for eac, VerifiedIncident, Unit tests for OrchestratorAgent (Agent 5) — Phase 5.  Tests dispatch optimizati, test_build_cost_matrix_shape(), test_capability_constraint_medical() (+5 more)

### Community 10 - "seed_data.py"
Cohesion: 0.20
Nodes (16): _jitter(), Seed script — populates demo_data/ with realistic mock records.  Usage:     cd b, Add small random noise to a coordinate so nearby reports aren't identical., Generate 25 realistic Hindi/English SMS-style citizen reports., Generate 20 realistic tweet-style social media posts., Generate 5 Sentinel-2 flood GeoJSON polygons., Generate 10 IoT sensor readings (water level + air quality)., Generate 8 mock responder teams with diverse capabilities. (+8 more)

### Community 12 - "test_ingest.py"
Cohesion: 0.13
Nodes (25): _build_dispatch_graph(), _cap_score(), commit_assignments(), DispatchState, _eta_seconds(), fetch_responders(), _haversine_m(), heuristic_assign() (+17 more)

### Community 13 - "CitizenReportInput"
Cohesion: 0.09
Nodes (24): get_intake_parser(), IntakeParserAgent, Intake Parser Agent — LLM Smart Intake Layer (Phase 4.5).  Uses LangChain's Chat, Return the shared IntakeParserAgent singleton., Parses free-text crisis reports into structured ParsedIntake using ChatGroq., Return True if GROQ_API_KEY is configured., Parse raw unstructured text using Groq LLM via LangChain.          Returns, ParsedIntake (+16 more)

### Community 14 - "incidents.py"
Cohesion: 0.09
Nodes (18): EmbeddingService, Embed multiple texts in a single batch call (more efficient than         calling, Cosine similarity between two vectors.          Since normalize_embeddings=True,, Async embedding service built on LangChain's HuggingFaceEmbeddings.      All pub, Encode a single text string into a 384-dim float list.          Uses LangChain's, Embed a ProtoIncident using text + optional location context.          Appending, Main entry point: verify + deduplicate a proto-incident.          Steps, Determine which cluster to join (or create a new one).          Collect cluster_ (+10 more)

### Community 22 - "SatellitePolygonInput"
Cohesion: 0.07
Nodes (33): get_orchestrator_agent(), AsyncSession, Return an OrchestratorAgent bound to *db* (a per-request AsyncSession)., get_vector_store(), Return the shared VectorStore singleton (initialised in main.py lifespan)., get_verification_agent(), datetime, Verification Agent — Agent 2.  Responsibilities:   - Deduplicate reports using s (+25 more)

### Community 23 - "SensorStreamInput"
Cohesion: 0.15
Nodes (18): _assess_body(), Integration tests for the VictimAgent assess endpoint — Phase 4.  Tests the full, Medical + rescue text in Delhi high-density zone → P1 or P2., Empty text → all needs=False, so base_needs_score=0.     Formula: (0 + 1.0 + pop, Response body must include all 6 scoring-factor keys., 3-source cluster should score higher than a 1-source cluster (same text)., Including satellite in provenance triggers the satellite_area factor., Valid request → 200 with well-formed SeverityAssessment JSON. (+10 more)

### Community 24 - "SocialPostInput"
Cohesion: 0.16
Nodes (16): Return the total number of points in the collection., LangChain-based vector store backed by Qdrant.      Wraps QdrantVectorStore for, VectorStore, ProtoIncident, Normalized incident before verification and deduplication., memory_vector_store(), Integration tests for VectorStore with Qdrant — Phase 2.  Uses an in-memory Qdra, Create a fresh in-memory VectorStore for each test. (+8 more)

### Community 25 - "AsyncSession"
Cohesion: 0.05
Nodes (66): Convert a NeedsProfile to the capability dict expected by the solver.          `, get_victim_agent(), _in_bbox(), Victim Agent — Agent 3.  Responsibilities:   - Extract needs (medical, shelter,, Return the shared VictimAgent singleton., Return True if (lat, lon) falls inside *bbox*., Extracts needs and computes severity for verified incidents., Assess needs and severity for a verified incident cluster.          Parameters (+58 more)

### Community 26 - "CommunicationAgent"
Cohesion: 0.09
Nodes (25): Integration tests for the Communication Agent REST & WebSocket APIs — Phase 6., REPORTED → RESOLVED (skipping states) must return 422., Status transition for a non-existent cluster must return 404., When citizen_phone is provided, a CommunicationLog row must be written., GET /incidents/{id}/summary must return a valid SituationalSummary., human_summary must be a non-empty string containing key identifiers., GET /communications/logs?incident_id=unused should return []., After a citizen SMS is triggered, the log entry must be queryable. (+17 more)

### Community 27 - "test_schemas.py"
Cohesion: 0.20
Nodes (6): DispatchRecord, Immutable record of each assignment made by the Orchestrator Agent.      Created, Verify the structured summary generator., When dispatch records exist, they should appear in the summary., Needs flags should appear in the human summary text., TestSituationalSummary

### Community 28 - "AsyncSession"
Cohesion: 0.06
Nodes (54): Step-function penalty based on how old the proto-incident timestamp is., Distance in metres between two lat/lon points (great-circle)., _mock_agent(), _proto(), Unit tests for VerificationAgent — Phase 3.  All tests mock VectorStore and Embe, Delhi (28.6139, 77.2090) → Agra (27.1767, 78.0081) ≈ 178 km ±10%., A point displaced ~140 m north should be within the 150 m window., A point displaced ~200 m north should be outside the 150 m window. (+46 more)

### Community 29 - "test_verification_integration.py"
Cohesion: 0.14
Nodes (24): _ingest(), _now(), _proto(), datetime, Integration tests for VerificationAgent — Phase 3.  Uses an in-memory Qdrant ins, A satellite + 3× SMS cluster should have higher confidence than an     SMS-only, A report 300 m away from an existing cluster should land in a     different clus, An identical report that is 35 minutes old (outside the 30-min window)     shoul (+16 more)

### Community 30 - ".verify"
Cohesion: 0.24
Nodes (7): ConnectionManager, Any, Real-time WebSocket endpoint for incident lifecycle updates.      Clients connec, Tracks all live WebSocket connections.      Thread-safety note: FastAPI runs in, Send *payload* as JSON to every connected client, evicting dead sockets., websocket_updates(), WebSocket

### Community 31 - ".upsert"
Cohesion: 0.11
Nodes (23): Generate a structured, human-readable situational summary for incident         c, assess_incident(), Run the VictimAgent needs-extraction and multi-factor severity scoring     pipel, AssessRequest, AssignedResponderSummary, CommLogEntry, DispatchResult, DispatchStatus (+15 more)

### Community 32 - "get_resource_agent"
Cohesion: 0.18
Nodes (15): get_resource_agent(), AsyncSession, Return a ResourceAgent bound to *db* (a per-request AsyncSession)., create_responder(), get_responder(), list_responders(), AsyncSession, Responders router — CRUD for the live responder registry (Phase 5). (+7 more)

### Community 33 - "vector_store.py"
Cohesion: 0.20
Nodes (7): init_vector_store(), QdrantClient, Create the Qdrant collection if it doesn't exist, then bind         the LangChai, Initialise the VectorStore singleton and ensure the Qdrant collection exists., memory_vector_store(), Initialize an in-memory VectorStore for tests., QdrantVectorStore

### Community 34 - "TestNotificationMockMode"
Cohesion: 0.12
Nodes (13): CommunicationLog, Audit log of every outbound message dispatched by the CommunicationAgent.      A, Assignment, Single responder-to-incident assignment produced by the Orchestrator., _make_assignment(), Unit tests for CommunicationAgent — Phase 6.  All tests are fully mocked — no da, Verify notification dispatch works in demo mode (no Twilio credentials)., notify_responder_assignment returns True in mock mode. (+5 more)

### Community 35 - "_record_to_schema"
Cohesion: 0.13
Nodes (16): Return all responders, optionally filtered by status., Fetch a single responder by id; returns None if not found., Update a responder's GPS position.          Returns the updated Responder, or No, Update a responder's operational status.          When transitioning back to 'av, Return responders that are available and within *radius_m* metres of         the, Score how well *responder* matches the incident's required capabilities., Convert an ORM row to the Pydantic Responder schema., Create a new responder entry in the registry.          Returns the full Responde (+8 more)

### Community 36 - "get_settings"
Cohesion: 0.16
Nodes (11): get_settings(), DisasterMesh backend — application settings.  Loaded from environment variables, Return cached settings singleton., Settings, get_redis_client(), Return a cached async Redis client.      Uses REDIS_URL from .env (Upstash redis, health(), Returns 200 when the API is up. Used by CI and load balancers. (+3 more)

### Community 37 - "init_vector_store"
Cohesion: 0.18
Nodes (7): Any, Find ProtoIncident payloads (and optional vectors) within geo radius + optional, Fetch a payload by proto_id., Return the payload dict for the *verified* point with the given cluster_id., Return ``(payload, vector)`` for every point whose ``proto_id`` payload, Return the payload dict for a verified incident cluster.          Thin alias for, Patch only the ``status`` field of an existing verified incident point.

### Community 38 - "TestStateMachine"
Cohesion: 0.14
Nodes (8): _make_incident(), Walk the entire happy path in one test., Skipping states must raise ValueError., RESOLVED → anything must raise ValueError., Every IncidentStatus must have an entry in VALID_TRANSITIONS., transition() must return the same object (mutated), not a copy., Verify the lifecycle transition guard., TestStateMachine

### Community 39 - ".search_nearby"
Cohesion: 0.16
Nodes (8): _make_ws(), Unit tests for the WebSocket ConnectionManager — Phase 6.  Tests cover:   - conn, Repeated connect/disconnect cycles must keep the set consistent., Return a mock WebSocket with async accept / send_json / receive_text., Disconnecting a socket that was never connected must not raise., A client that raises on send_json must be removed from the active set., Broadcasting with no clients must not raise., TestConnectionManager

### Community 40 - "main.py"
Cohesion: 0.22
Nodes (9): CommunicationAgent, Any, AsyncSession, Notify a responder that they have been assigned to *incident*.          Sends an, Send a status-update SMS to the citizen who filed the report.          Parameter, Send *body* to *to_number* via Twilio (real or WhatsApp) or mock mode., Return a comma-separated human-readable needs string., Persist a ``CommunicationLog`` row and flush (but not commit). (+1 more)

### Community 41 - "embeddings.py"
Cohesion: 0.33
Nodes (4): get_langchain_embeddings(), Embedding Service — Phase 2.  Uses LangChain's HuggingFaceEmbeddings wrapper aro, Return the shared LangChain HuggingFaceEmbeddings singleton.      First call dow, HuggingFaceEmbeddings

### Community 42 - "get_qdrant_client_sync"
Cohesion: 0.18
Nodes (12): get_communication_agent(), Communication Agent — Agent 6.  Responsibilities:   - Enforce the incident lifec, Return the shared ``CommunicationAgent`` singleton., get_communication_logs(), get_situational_summary(), AsyncSession, Communication router — Phase 6.  Endpoints --------- POST /incidents/{cluster_id, Advance the incident lifecycle state machine.      Valid transitions:     ``REPO (+4 more)

### Community 43 - ".assess"
Cohesion: 0.50
Nodes (3): _haversine_m(), Resource Agent — Agent 4.  Responsibilities:   - Maintain live responder registr, Great-circle distance in metres between two lat/lon points.

### Community 45 - "conftest.py"
Cohesion: 0.22
Nodes (12): get_db(), _get_engine(), get_qdrant_client_sync(), _get_session_factory(), init_db(), AsyncSession, QdrantClient, Database and service client factories.  Qdrant:      local file mode by default (+4 more)

### Community 46 - "get_embedding_service"
Cohesion: 0.33
Nodes (8): get_embedding_service(), Return the shared EmbeddingService singleton., Unit tests for EmbeddingService — Phase 2.  Run:     cd backend     pytest app/t, test_cosine_similarity(), test_embed_batch(), test_embed_incident_with_and_without_coords(), test_embed_text_english_and_hindi(), test_embed_text_returns_384_dims()

### Community 47 - "SourceType"
Cohesion: 0.32
Nodes (7): Apply a lifecycle state transition to *incident* (in-place).          Parameters, _get_verified_incident(), Fetch a ``VerifiedIncident`` from the Qdrant vector store.      Raises     -----, IncidentStatus, Priority, SourceType, StrEnum

### Community 48 - "conftest.py"
Cohesion: 0.17
Nodes (10): async_sessionmaker, db_session(), patch_get_db(), patch_init_db(), Root conftest.py for all tests (unit and integration).  Provides an in-memory SQ, Create all tables in an in-memory SQLite DB once per test session., Yield a fresh async session, rolling back after each test., Replace the FastAPI `get_db` dependency with one that returns the     test sessi (+2 more)

### Community 49 - "test_ingest.py"
Cohesion: 0.25
Nodes (3): Unit tests for the ingest endpoints.  Run:     cd backend     pytest app/tests/u, Accepts report with address but no lat/lon., test_ingest_citizen_report_address_only()

### Community 52 - "get_qdrant_client"
Cohesion: 0.67
Nodes (3): AsyncQdrantClient, get_qdrant_client(), Return a cached Qdrant client.      - QDRANT_URL is set  → connect to cloud / se

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `VerifiedIncident` connect `VerificationAgent` to `TestNotificationMockMode`, `_record_to_schema`, `📦 Data schema`, `VerifiedIncident`, `TestStateMachine`, `main.py`, `CommunicationAgent`, `test_ingest.py`, `incidents.py`, `SourceType`, `SatellitePolygonInput`, `SocialPostInput`, `AsyncSession`, `CommunicationAgent`, `test_schemas.py`, `.verify`, `.upsert`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Why does `NeedsProfile` connect `AsyncSession` to `TestNotificationMockMode`, `📦 Data schema`, `VerifiedIncident`, `TestStateMachine`, `VerificationAgent`, `test_ingest.py`, `CitizenReportInput`, `incidents.py`, `SourceType`, `SatellitePolygonInput`, `CommunicationAgent`, `test_schemas.py`, `.verify`, `.upsert`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Why does `VectorStore` connect `SocialPostInput` to `vector_store.py`, `init_vector_store`, `CommunicationAgent`, `VerificationAgent`, `incidents.py`, `SatellitePolygonInput`, `test_verification_integration.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `VictimAgent` (e.g. with `NeedsProfile` and `Priority`) actually correct?**
  _`VictimAgent` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `VerifiedIncident` (e.g. with `CommunicationAgent` and `DispatchState`) actually correct?**
  _`VerifiedIncident` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Are the 39 inferred relationships involving `NeedsProfile` (e.g. with `DispatchState` and `OrchestratorAgent`) actually correct?**
  _`NeedsProfile` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `ResourceAgent` (e.g. with `DispatchState` and `OrchestratorAgent`) actually correct?**
  _`ResourceAgent` has 29 INFERRED edges - model-reasoned connections that need verification._