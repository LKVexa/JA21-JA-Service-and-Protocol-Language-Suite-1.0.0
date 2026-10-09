# Conformance Cases

A conforming implementation should test at least these families:

1. Typed request/response service declaration.
2. Unknown request field and incompatible response type.
3. Legal and illegal protocol transitions.
4. Retry without idempotency.
5. Deadline exhaustion with bounded recovery.
6. Quota and rate-limit boundary behavior.
7. Backpressure under slow consumers.
8. Missing authentication or authorization.
9. Hidden remote transport under no-network policy.
10. Offline transport package replay.
11. Serialization and compatibility-version mismatch.
12. Deterministic client stub, server interface, and test double.
13. R12/MCRT identity retention through optimization.
14. Certification holdout with complete evidence receipt.
