# Graph Report - .  (2026-08-07)

## Corpus Check
- Corpus is ~1,697 words - fits in a single context window. You may not need a graph.

## Summary
- 25 nodes · 31 edges · 5 communities (4 shown, 1 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- DisasterMesh Project
- AGENTS.md Graphify Agent Rule
- Situational Agent (Intake + Fusion)
- Qdrant Vector Database
- Graphify Skill (SKILL.md)

## God Nodes (most connected - your core abstractions)
1. `DisasterMesh Project` - 9 edges
2. `Orchestrator Agent` - 5 edges
3. `Qdrant Vector Database` - 5 edges
4. `AGENTS.md Graphify Agent Rule` - 4 edges
5. `Situational Agent (Intake + Fusion)` - 4 edges
6. `Verification Agent` - 4 edges
7. `Victim Agent (Needs & Severity)` - 4 edges
8. `Graphify Knowledge Graph` - 3 edges
9. `Communication Agent` - 3 edges
10. `Graphify Query-First Rule` - 2 edges

## Surprising Connections (you probably didn't know these)
- `AGENTS.md Graphify Agent Rule` --semantically_similar_to--> `Graphify Query-First Rule`  [INFERRED] [semantically similar]
  /Users/rishu/Desktop/DisasterMesh/AGENTS.md → /Users/rishu/Desktop/DisasterMesh/.agents/rules/graphify.md
- `AGENTS.md Graphify Agent Rule` --references--> `Graphify Knowledge Graph`  [EXTRACTED]
  /Users/rishu/Desktop/DisasterMesh/AGENTS.md → /Users/rishu/Desktop/DisasterMesh/.agents/rules/graphify.md

## Hyperedges (group relationships)
- **DisasterMesh 6-Agent Pipeline** — readme_situational_agent, readme_verification_agent, readme_victim_agent, readme_resource_agent, readme_orchestrator_agent, readme_communication_agent [EXTRACTED 1.00]
- **Graphify Agent Rules Consistency (AGENTS.md + .agents/rules)** — agents_md_graphify_agent_rule, _agents_rules_graphify_graphify_query_rule, _agents_rules_graphify_graphify_update_rule [INFERRED 0.85]
- **DisasterMesh Core Tech Stack** — readme_fastapi_backend, readme_qdrant_vector_db, readme_or_tools_optimizer, readme_react_mapbox_frontend [EXTRACTED 1.00]

## Communities (5 total, 1 thin omitted)

### Community 0 - "DisasterMesh Project"
Cohesion: 0.31
Nodes (9): Communication Agent, DisasterMesh Project, Incident Lifecycle State Machine, OR-Tools Optimizer, Orchestrator Agent, React + Mapbox GL JS Frontend, Resource Agent, Severity Scoring and Prioritization (+1 more)

### Community 1 - "AGENTS.md Graphify Agent Rule"
Cohesion: 0.40
Nodes (6): Graphify Knowledge Graph, Graphify Query-First Rule, Graphify Update After Code Change, Cross-File Relationships, God Nodes and Community Structure, AGENTS.md Graphify Agent Rule

### Community 2 - "Situational Agent (Intake + Fusion)"
Cohesion: 0.50
Nodes (4): Confidence Scoring, Multi-Source Crisis Signal Fusion, Situational Agent (Intake + Fusion), Verification Agent

### Community 3 - "Qdrant Vector Database"
Cohesion: 0.67
Nodes (4): FastAPI Backend, Incidents Qdrant Collection, Qdrant Vector Database, Seed Data Script (seed_data.py)

## Knowledge Gaps
- **10 isolated node(s):** `Graphify Workflow`, `Graphify Skill (SKILL.md)`, `God Nodes and Community Structure`, `Cross-File Relationships`, `OR-Tools Optimizer` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DisasterMesh Project` connect `DisasterMesh Project` to `Situational Agent (Intake + Fusion)`, `Qdrant Vector Database`?**
  _High betweenness centrality (0.264) - this node is a cross-community bridge._
- **Why does `Qdrant Vector Database` connect `Qdrant Vector Database` to `DisasterMesh Project`, `Situational Agent (Intake + Fusion)`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **What connects `Graphify Update After Code Change`, `Graphify Workflow`, `Graphify Skill (SKILL.md)` to the rest of the system?**
  _11 weakly-connected nodes found - possible documentation gaps or missing edges._