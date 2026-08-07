# Graph Report - DisasterMesh  (2026-08-07)

## Corpus Check
- 4 files · ~2,240 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 33 nodes · 29 edges · 6 communities (2 shown, 4 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1fcc0ead`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 🌐 DisasterMesh
- 🏗️ Architecture
- AGENTS.md
- graphify.md
- graphify.md
- 📦 Data schema

## God Nodes (most connected - your core abstractions)
1. `🌐 DisasterMesh` - 19 edges
2. `🏗️ Architecture` - 7 edges
3. `📦 Data schema` - 2 edges
4. `graphify` - 1 edges
5. `Workflow: graphify` - 1 edges
6. `graphify` - 1 edges
7. `📑 Table of contents` - 1 edges
8. `🧭 Project overview` - 1 edges
9. `1️⃣ Situational Agent — Intake & Fusion` - 1 edges
10. `2️⃣ Verification Agent — Dedup & Confidence` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (6 total, 4 thin omitted)

### Community 0 - "🌐 DisasterMesh"
Cohesion: 0.11
Nodes (17): 🙏 Acknowledgements, 🔌 API reference, 🤝 Contributing, 🔄 Data flow, 🚀 Deployment, 🌐 DisasterMesh, 🔐 Environment variables, 📄 License (+9 more)

### Community 1 - "🏗️ Architecture"
Cohesion: 0.29
Nodes (7): 1️⃣ Situational Agent — Intake & Fusion, 2️⃣ Verification Agent — Dedup & Confidence, 3️⃣ Victim Agent — Needs & Severity, 4️⃣ Resource Agent — Responder State, 5️⃣ Orchestrator Agent — Optimization & Dispatch, 6️⃣ Communication Agent — Notify & Track, 🏗️ Architecture

## Knowledge Gaps
- **26 isolated node(s):** `graphify`, `Workflow: graphify`, `graphify`, `📑 Table of contents`, `🧭 Project overview` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `🌐 DisasterMesh` connect `🌐 DisasterMesh` to `🏗️ Architecture`, `📦 Data schema`?**
  _High betweenness centrality (0.611) - this node is a cross-community bridge._
- **Why does `🏗️ Architecture` connect `🏗️ Architecture` to `🌐 DisasterMesh`?**
  _High betweenness centrality (0.272) - this node is a cross-community bridge._
- **Why does `📦 Data schema` connect `📦 Data schema` to `🌐 DisasterMesh`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **What connects `graphify`, `Workflow: graphify`, `graphify` to the rest of the system?**
  _26 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `🌐 DisasterMesh` be split into smaller, more focused modules?**
  _Cohesion score 0.1111111111111111 - nodes in this community are weakly interconnected._