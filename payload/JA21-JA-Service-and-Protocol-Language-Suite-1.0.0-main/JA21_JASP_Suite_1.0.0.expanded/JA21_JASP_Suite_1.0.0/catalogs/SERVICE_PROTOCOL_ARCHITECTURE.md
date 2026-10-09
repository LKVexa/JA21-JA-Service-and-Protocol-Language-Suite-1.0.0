# JA Service and Protocol Architecture

```text
Authoritative `.jasp` source
        │
        ├── Service declarations ── endpoints ── methods
        ├── Message contracts ───── request / response / error
        ├── Protocol automata ───── states / commands / events
        ├── Reliability policy ──── retry / backoff / deadline / idempotency
        ├── Flow governance ─────── quota / rate limit / backpressure
        ├── Authority policy ────── authentication / authorization / capabilities
        └── Transport profile ───── local / remote / offline / discovery
        │
        ▼
Parser → Typed AST → Semantic judgment → Policy gate
        │
        ▼
R12 lowering → transport/runtime plan → MCRT evidence receipt
        │
        ▼
Deterministic test runtime / governed service host / compatibility report
```

## Five review lenses

- **SOPHIA:** semantic correctness, contract consistency, and policy reasoning.
- **CHARLOTTE:** reconstruction, compatibility, version migration, and artifact closure.
- **LANDON:** executable workflow, runtime scheduling, transport behavior, and diagnostics.
- **Professor:** pedagogy, definitions, proof obligations, and assessment quality.
- **Podium:** publication hierarchy, navigability, visual discipline, and release evidence.
