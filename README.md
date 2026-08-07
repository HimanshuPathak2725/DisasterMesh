# 🌐 DisasterMesh

**A multi-agent disaster response coordination system that fuses multi-source crisis signals into verified, prioritized, and dispatched incidents in real time.**

DisasterMesh ingests reports from satellites, social media, citizens, and IoT sensors, deduplicates and verifies them, scores severity, matches available responders, and closes the loop with real-time notifications — all through a pipeline of six coordinated agents.

---

## 📑 Table of contents

- [🧭 Project overview](#project-overview)
- [🏗️ Architecture](#architecture)
- [🔄 Data flow](#data-flow)
- [🛠️ Tech stack](#tech-stack)
- [📁 Repository layout](#repository-layout)
- [📦 Data schema](#data-schema)
- [🔌 API reference](#api-reference)
- [🔐 Environment variables](#environment-variables)
- [🌱 Seeding demo data](#seeding-demo-data)
- [▶️ Running a demo scenario](#running-a-demo-scenario)
- [✅ Testing](#testing)
- [🚀 Deployment](#deployment)
- [🗺️ Roadmap](#roadmap)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

---

## 🧭 Project overview

During a disaster, the hardest problem isn't a lack of information — it's too much of it, arriving unverified, unstructured, and from too many channels at once. Satellite imagery flags a flooded region hours after it started. Citizens send panicked, inconsistent SMS reports. Social media surfaces real signal buried in noise. Responders operate with partial visibility into where they're needed most.

DisasterMesh is built to solve that fusion problem end-to-end:

- **Ingest** everything (satellite polygons, social posts, citizen reports, IoT sensor streams) into one canonical schema
- **Deduplicate and verify** so five reports of the same fire become one confirmed incident, not five
- **Score severity** using a multi-factor model, so P1 incidents surface before P4s
- **Match and dispatch** responders using constraint-based optimization, not just "nearest available"
- **Close the loop** with real-time status updates to both citizens and responders

The system is designed to be demoable end-to-end on a laptop using mock data, while being architected in a way that scales to real feeds (Sentinel-2, IMD alerts, Twilio/WhatsApp) with minimal rework.

---

## 🏗️ Architecture

DisasterMesh is a six-agent pipeline. Each agent is a modular, independently callable backend component. All agents read/write through a shared vector memory layer (Qdrant) and are orchestrated by a FastAPI backend.

### 1️⃣ Situational Agent — Intake & Fusion
- **Inputs:** satellite polygons, social posts, citizen reports (SMS/WhatsApp/web form), IoT sensor streams
- **Responsibilities:** normalize every inbound message into a canonical incident schema; extract geolocation, timestamp, media links, and source metadata
- **Output:** proto-incident objects persisted into Qdrant with an embedding vector + metadata (`source_provenance`)

### 2️⃣ Verification Agent — Dedup & Confidence
- **Inputs:** proto-incidents from the Situational Agent
- **Responsibilities:** deduplicate via spatial/temporal clustering (150 m / 30 min window as a default) combined with vector similarity for cases where geo-coordinates are noisy or missing; filter stale/noisy reports; run basic image classification checks on attached media; cross-source corroboration (does a satellite polygon back up the citizen reports in the same area?)
- **Output:** verified incident clusters with `cluster_id`, a confidence score (0–1), and a canonical representative record

### 3️⃣ Victim Agent — Needs & Severity
- **Inputs:** verified incident clusters
- **Responsibilities:** extract needs (medical, shelter, evacuation, rescue) from report text/media; compute a severity score using a multi-factor model — keyword multipliers, population density overlay, multi-source corroboration bonus, satellite-derived area proxy, and temporal escalation (an incident that keeps generating new reports over time gets bumped up)
- **Output:** priority label (`P1`–`P4`) and a structured needs profile JSON per cluster

### 4️⃣ Resource Agent — Responder State
- **Inputs:** registered responder resources (registry DB or real-time location feed)
- **Responsibilities:** maintain responder capability tags (medical, rescue, water, logistics), inventory, live status, location, and availability windows
- **Output:** a live, queryable resource pool consumed by the Orchestrator

### 5️⃣ Orchestrator Agent — Optimization & Dispatch
- **Inputs:** prioritized incidents, live resource pool, road/traffic ETA estimates
- **Responsibilities:** compute an assignment matrix that minimizes total ETA subject to capability and capacity constraints, using **Google OR-Tools**; handle dynamic re-routing when traffic conditions change or a responder times out
- **Output:** assignment records, ETA per assignment, route details

### 6️⃣ Communication Agent — Notify & Track
- **Inputs:** lifecycle state changes and assignment results
- **Responsibilities:** send citizen and responder notifications (SMS/WhatsApp); generate situational summaries; drive the incident lifecycle state machine
- **Output:** notification logs, callback webhooks, status updates

**Lifecycle state machine:**

```
REPORTED → VERIFIED → ASSIGNED → EN ROUTE → ON SCENE → RESOLVED
```

---

## 🔄 Data flow

```
 SATELLITE   SOCIAL   CITIZEN   IoT
     │          │        │       │
     └────────┬─┴────────┴───────┘
              ▼
      Situational Agent
     (normalize + embed)
              ▼
      Verification Agent
     (cluster + dedupe + verify)
              ▼
       Victim Agent
   (needs extraction + severity)
              ▼
      ┌───────┴────────┐
      ▼                ▼
Resource Agent   Orchestrator Agent
(live state)    (optimize + assign)
      └───────┬────────┘
              ▼
      Communication Agent
      (notify + lifecycle)
```

---

## 🛠️ Tech stack

| Layer | Choice |
|---|---|
| Backend | Python 3.11+, FastAPI (async) |
| Agent orchestration | Function-call pipeline, optionally CrewAI or LangGraph |
| Vector memory | Qdrant (self-hosted or cloud) |
| LLM | Any bilingual model (Claude, Gemini, etc.) for extraction/translation |
| Satellite data | Pre-downloaded Sentinel-2 GeoJSONs + NASA FIRMS REST for thermal alerts |
| Geocoding | OpenStreetMap / Nominatim + local landmark lookup table for Hindi transliterations |
| Optimization | Google OR-Tools (Python) |
| Realtime | Server-sent events, or Socket.io as an alternative |
| Messaging | Twilio SMS (demo), WhatsApp Business API (optional) |
| Image hosting | Cloudinary or S3 |
| Frontend | React + Mapbox GL JS |

---

## 📁 Repository layout

```
disastermesh/
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI entrypoint
│   │   ├── agents/
│   │   │   ├── situational.py
│   │   │   ├── verification.py
│   │   │   ├── victim.py
│   │   │   ├── resource.py
│   │   │   ├── orchestrator.py
│   │   │   └── communication.py
│   │   ├── schemas.py             # Pydantic models — canonical incident schema
│   │   └── tests/
│   │       ├── unit/
│   │       └── integration/
│   ├── scripts/
│   │   └── seed_data.py
│   └── requirements.txt
├── demo_data/
│   ├── citizen_reports/           # 20–30 mock SMS-style JSON messages (Hindi/English)
│   ├── social_posts/              # 15–20 mock tweets/news items
│   ├── satellite/                 # 3–5 Sentinel-2 flood GeoJSON polygons
│   ├── responder_registry.json    # 5–8 responder teams with capabilities
│   ├── population_density.geojson # Tagged POIs (school, hospital, metro)
│   └── authority_alerts.json      # Mock IMD/authority alerts
├── infra/
│   └── docker-compose.yml         # Qdrant + Redis
└── frontend/                      # React + Mapbox dashboard
```

---

## 📦 Data schema

### Canonical incident record (Qdrant `incidents` collection)

```json
{
  "vector": "[float, float, ...]",
  "payload": {
    "cluster_id": "string",
    "source_provenance": ["sms", "sentinel", "tweet"],
    "lat": 28.6139,
    "lon": 77.2090,
    "timestamp": "2026-08-07T09:15:00Z",
    "confidence": 0.87,
    "severity": "P1",
    "needs": {
      "medical": true,
      "shelter": false,
      "evacuation": true,
      "rescue": true
    },
    "media_urls": ["https://..."]
  }
}
```

**Indexing & retrieval patterns:**
- Nearest incidents by vector similarity (semantic search across differently-worded reports of the same event)
- Geo-filtered nearest incidents by radius (150 m default for dedupe clustering)
- Time-window filtering (e.g., last 6 hours)

> **Note on geo queries:** Prefer Qdrant's native geo filtering where available. If your Qdrant version has limited geo support, fall back to storing `lat`/`lon` in the payload and running a server-side Haversine filter — this is fine for demo-scale datasets (hundreds to low thousands of incidents).

---

## 🔌 API reference

Suggested FastAPI endpoints. Adjust naming to match your actual implementation in `backend/app/main.py`.

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/ingest/report` | Accepts a citizen report JSON (SMS/text/form) |
| `POST` | `/ingest/social` | Accepts a social post JSON |
| `POST` | `/ingest/satellite` | Accepts a GeoJSON polygon or polygon ID |
| `POST` | `/agents/run/{agent_name}` | Manually trigger a specific agent job (debug) |
| `GET` | `/incidents/{cluster_id}` | Fetch incident cluster details |
| `GET` | `/incidents?lat=&lon=&radius=` | Geo query for nearby incidents |
| `POST` | `/dispatch/{cluster_id}` | Force a dispatch (debug endpoint) |
| `WS` | `/ws/updates` | Real-time incident and dispatch updates |

**Example: submitting a citizen report**

```bash
curl -X POST http://localhost:8000/ingest/report \
  -H "Content-Type: application/json" \
  -d '{
    "source": "sms",
    "text": "Water rising fast near Yamuna Bazar, need boats",
    "lat": 28.6667,
    "lon": 77.2333,
    "timestamp": "2026-08-07T09:10:00Z",
    "media_urls": []
  }'
```

Full request/response schemas live in `backend/app/schemas.py`.

---

## 🔐 Environment variables

Create a `.env` file in `backend/` with:

```env
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=

DATABASE_URL=sqlite:///./dev.db

MAPBOX_TOKEN=

TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_FROM_NUMBER=

SENTINEL_DATA_DIR=./demo_data/satellite
S3_BUCKET=

ORTOOLS_SCALAR_WEIGHTS=
```

For a demo, `DATABASE_URL` can stay on SQLite. Switch to Postgres for anything beyond local testing — you'll want relational queries over incident/responder history that Qdrant alone won't give you cleanly.

---

## 🌱 Seeding demo data

`backend/scripts/seed_data.py` should:
1. Create the Qdrant `incidents` collection with the schema above
2. Load demo GeoJSON polygons into it
3. Push mock SMS/tweet JSON through the ingestion pipeline (or directly into Qdrant, if you want to skip agent processing for a quick smoke test)
4. Create responder registry entries in the local DB

Recommended demo dataset sizes (small enough to reason about, large enough to show dedup working):
- 20–30 mock citizen reports (mix of Hindi/English)
- 3–5 satellite flood polygons
- 15–20 mock social posts
- 5–8 responder teams with distinct capability tags

---

## ▶️ Running a demo scenario

A good end-to-end demo flow:

1. Seed the data (above)
2. POST 4–5 citizen reports describing the *same* flooding event with slightly different wording/locations — this is what shows off the Verification Agent's dedup
3. Watch `/ws/updates` or the frontend map as the cluster forms, gets a confidence score, and is assigned a severity label
4. Call `/dispatch/{cluster_id}` (or let the Orchestrator auto-assign) and confirm a responder gets matched with a computed ETA
5. Confirm a notification log appears in the Communication Agent's output and the lifecycle state advances

---

## ✅ Testing

```bash
cd backend
pytest -q
```

- **Unit tests:** `backend/app/tests/unit` — test each agent's logic in isolation with mocked inputs
- **Integration tests:** `backend/app/tests/integration` — run against a small seeded Qdrant instance to validate the full pipeline

---

## 🚀 Deployment

| Component | Recommended target |
|---|---|
| Frontend | Vercel |
| Backend | Render / Fly.io |
| Qdrant | Qdrant Cloud or self-hosted Docker |

Use environment variables to cleanly separate demo mode (mock data, no real SMS sending) from production mode (real Twilio/WhatsApp, real satellite feeds).

---

## 💡 Operational notes

- For live demos, pre-compute satellite flood polygons ahead of time and present them as "real-time" — don't rely on on-the-fly Sentinel downloads during a presentation.
- Maintain a geocoding fallback lookup table of known landmarks to avoid Hindi transliteration failures with Nominatim.
- Start the Orchestrator with a simple OR-Tools objective (minimize total travel time/distance) before layering in multi-objective constraints like capability matching or capacity limits — it's much easier to debug incrementally.

---

## 🗺️ Roadmap

- [ ] Real-time Sentinel-2 ingestion (beyond pre-downloaded polygons)
- [ ] Multi-objective OR-Tools model (ETA + capability + capacity + fairness)
- [ ] WhatsApp Business API integration for two-way citizen communication
- [ ] Admin dashboard for manual override of agent decisions
- [ ] Multi-language support beyond Hindi/English

---

## 🤝 Contributing

Contributions are welcome:
1. Fork the repo
2. Create a feature branch
3. Add tests for new functionality
4. Submit a PR with a clear description and, where relevant, screenshots

---

## 📄 License

MIT — see `LICENSE` at the repo root.

## 🙏 Acknowledgements

DisasterMesh is an engineering reference for multi-source disaster detection and coordination. Keep demo data and any production data ethically sourced and privacy-aware — especially where citizen reports include location and personal details.