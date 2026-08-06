# DisasterMesh

DisasterMesh is a technical reference implementation of a unified, multi-agent disaster response architecture. This README focuses on the system design, required data, developer setup, runtime components, and operational notes needed to run and extend the project.

Table of contents
- Project overview
- Architecture (6 agents)
- Data flow
- Tech stack
- Data & demo assets
- Qdrant schema & vector design
- API surface (backend)
- Local development (prerequisites & steps)
- Deployment notes
- Testing & validation
- Contributing
- License

## Project overview
DisasterMesh implements a 6-agent pipeline for fusing multi-source crisis signals (satellite, social, citizen reports, IoT) into verified incidents, scoring severity, matching responders, and closing the communication loop with affected citizens and responders. It is designed as a modular backend (FastAPI), vector memory (Qdrant), and optional frontend (React + Mapbox) demo.

Goals:
- Demonstrate multi-source fusion and confidence scoring
- Provide an explainable severity/prioritization layer for incidents
- Provide a working optimizer for responder dispatch (OR-Tools)
- Provide demonstrable, repeatable local dev workflow using mock data

## Architecture (6 agents)
Each agent is a modular microservice or callable backend component. The architecture assumes shared vector memory (Qdrant) and a FastAPI orchestration layer calling agent functions.

1) Situational Agent (Intake + Fusion)
- Inputs: satellite polygons, social posts, citizen reports (SMS/WhatsApp/web form), IoT sensor streams
- Responsibilities: normalize all inbound messages into a canonical incident schema, extract geolocation, timestamp, media links, and source metadata
- Output: proto-incident objects persisted into Qdrant with vector embedding + metadata (source_provenance)

2) Verification Agent
- Inputs: proto-incidents from Situational Agent
- Responsibilities: deduplicate by spatial/temporal clustering (e.g., 150 m / 30 min window), filter noise (age thresholds), image classification checks, cross-source corroboration
- Output: verified incident clusters with cluster_id, confidence score, and canonical representative record

3) Victim Agent (Needs & Severity)
- Inputs: verified clusters
- Responsibilities: extract needs (medical, shelter, evacuation, rescue), compute severity score (multi-factor: keyword multipliers, population density overlay, multi-source bonuses, satellite area proxies, temporal escalation rules)
- Output: priority label (P1..P4), needs profile JSON for each cluster

4) Resource Agent
- Inputs: registered responder resources (registry DB / real-time locations)
- Responsibilities: maintain responder capability tags, inventory, status, location, availability windows
- Output: live resource pool used by Orchestrator

5) Orchestrator Agent
- Inputs: prioritized incidents, resource pool, road/traffic ETAs
- Responsibilities: compute assignment matrix (minimize ETA with capability constraints), produce dispatch orders, handle dynamic re-routing (traffic/timeouts). Uses OR-Tools for constraint solving.
- Output: assignment records, ETA, route details

6) Communication Agent
- Inputs: lifecycle state changes and assignment results
- Responsibilities: send citizen/responder notifications (SMS/WhatsApp), produce situational summaries, manage lifecycle state machine (REPORTED → VERIFIED → ASSIGNED → EN ROUTE → ON SCENE → RESOLVED)
- Output: notification logs, callback webhooks, status updates

## Data flow (high level)
SATELLITE + SOCIAL + CITIZEN + IoT
  → Situational Agent (normalize + embed)
  → Verification Agent (cluster + dedupe + verify)
  → Victim Agent (needs extraction + severity)
  → Resource Agent (live resource state)
  → Orchestrator Agent (optimize + assign)
  → Communication Agent (notify + lifecycle)

## Tech stack
- Backend: Python 3.11+, FastAPI (async)
- Orchestration: lightweight function calls or CrewAI / LangGraph (optional)
- Vector DB: Qdrant (self-host or cloud)
- LLM: any bilingual model (Gemini/LLM of choice) for extraction/translation tasks
- Satellite data: pre-downloaded Sentinel-2 GeoJSONs + NASA FIRMS REST for thermal alerts
- Geocoding: OpenStreetMap / Nominatim + local landmark lookup table for Hindi transliterations
- Maps / frontend: React + Mapbox GL JS
- Optimization: Google OR-Tools (Python)
- Realtime: Socket.io (websocket gateway) or server-sent events
- Messaging: Twilio SMS (demo), WhatsApp Business API (optional)
- Image hosting: Cloudinary (or S3)

## Data & demo assets
Prepare and pre-load the following demo assets before running a live demo:
- Mock citizen reports: 20–30 SMS-style JSON messages (Hindi/English)
- Satellite polygons: 3–5 pre-computed Sentinel-2 flood GeoJSON polygons
- Mock social posts: 15–20 tweets/news items with timestamps and geo hints
- Responder registry: 5–8 teams with capabilities and home bases
- Population density overlay: small JSON grid or geojson with tagged POIs (school, hospital, metro)
- IMD/authority alerts: mock JSON file(s)

Suggested file layout inside repo (examples):
- /backend/ (FastAPI app)
- /backend/app/main.py
- /backend/app/agents/ (agent modules for situational, verification, victim, resource, orchestrator, comms)
- /backend/scripts/seed_data.py
- /demo_data/ (mock SMS, tweets, geojson polygons)
- /infra/docker-compose.yml (qdrant, redis)
- /frontend/ (React + Mapbox)

## Qdrant schema & vector design (recommended)
Collection: incidents
- vector: float[dim] (embedding vector from extractor)
- payload (metadata):
  - cluster_id: string
  - source_provenance: array[string] (e.g. ["sms", "sentinel", "tweet"])
  - lat: float
  - lon: float
  - timestamp: ISO8601
  - confidence: float (0..1)
  - severity: integer or string (P1..P4)
  - needs: JSON (medical, shelter, water, evacuation)
  - media_urls: array[string]

Geospatial queries: Prefer Qdrant's geo filtering where possible. If Qdrant geo features are limited in your chosen version, fallback to storing lat/lon in metadata and using a server-side Haversine filter for small datasets.

Indexing & retrieval patterns:
- Nearest incidents by vector similarity for semantic search
- Geo-filtered nearest incidents by radius (150m default for dedupe clustering)
- Time window filtering (e.g., last 6 hours)

## Backend API surface (suggested endpoints)
These are suggested endpoints for the FastAPI backend. Implementations may vary.
- POST /ingest/report  → accepts citizen report JSON (sms/text/form)
- POST /ingest/social  → accepts social post JSON
- POST /ingest/satellite → accepts GeoJSON polygon or polygon id
- POST /agents/run/{agent_name} → run a specific agent job (debug)
- GET /incidents/{cluster_id} → incident cluster details
- GET /incidents?lat=&lon=&radius= → geo query
- POST /dispatch/{cluster_id} → force dispatch (debug endpoint)
- Websocket /ws/updates → socket.io or websocket endpoint for real-time updates

Payloads should use a canonical schema (see /docs or /backend/app/schemas.py)

## Environment variables (example)
- QDRANT_URL=http://localhost:6333
- QDRANT_API_KEY=
- DATABASE_URL=sqlite:///./dev.db (or postgres://...)
- MAPBOX_TOKEN=<token>
- TWILIO_ACCOUNT_SID=<sid>
- TWILIO_AUTH_TOKEN=<token>
- TWILIO_FROM_NUMBER=<+1...>
- SENTINEL_DATA_DIR=./demo_data/sentinel
- S3_BUCKET= (if using S3 for images)
- ORTOOLS_SCALAR_WEIGHTS= (optional tuning string for optimizer)

## Local development (quickstart)
Prerequisites:
- Python 3.11+
- Node 18+ (for frontend)
- Docker (recommended for Qdrant)
- Poetry / pip for dependency management

Steps:
1. Clone the repo
   git clone https://github.com/vib3withsimran/DisasterMesh.git
2. Start Qdrant (docker-compose in /infra/docker-compose.yml):
   cd infra && docker compose up -d
   (or use Qdrant Cloud and set QDRANT_URL)
3. Create a virtualenv and install backend deps:
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
4. Seed demo data (adjust path if needed):
   python backend/scripts/seed_data.py --dir ../demo_data
   This script populates Qdrant with mock incident vectors and demo responder registry.
5. Run the backend:
   uvicorn backend.app.main:app --reload --port 8000
6. Run the frontend (optional):
   cd frontend && npm install && npm run dev
7. Open the dashboard (default): http://localhost:3000 or http://localhost:8000/docs for OpenAPI

## Seeding & demo scripts
- /backend/scripts/seed_data.py should:
  - create the Qdrant collection with the recommended schema
  - load demo GeoJSON polygons into the incidents collection
  - load mock SMS/tweet JSON into an ingestion queue or directly into Qdrant
  - create responder registry entries in the local DB

## Operational notes & performance caveats
- For demos, pre-compute satellite flood polygons and treat them as "real-time" alerts; do not rely on on-the-fly sentinel downloads.
- Keep the geocoding fallback lookup table of known landmarks to avoid Hindi transliteration failures.
- Start with simple OR-Tools objective (minimize travel time/distance) before adding multi-objective constraints.

## Testing & validation
- Unit tests: backend/app/tests/unit
- Integration tests: backend/app/tests/integration (include a small seeded Qdrant run)
- Run tests via pytest in the backend virtualenv: pytest -q

## Deployment
- Frontend: Vercel (recommended)
- Backend: Render / Fly / Render Web Service
- Qdrant: Qdrant Cloud or self-hosted via Docker
- Use environment variables to separate demo mode from production mode

## Contributing
Contributions are welcome. Please open issues for bugs or feature requests. Follow the standard GitHub workflow:
- Fork the repo
- Create a feature branch
- Add tests for new features
- Submit a PR with descriptions and screenshots where applicable

## License
Specify a license file in the repo (e.g., MIT). Add LICENSE at repo root.

## Acknowledgements
This project is an engineering reference for multi-source disaster detection and coordination; please keep demo data and production data ethically sourced and privacy-aware.
