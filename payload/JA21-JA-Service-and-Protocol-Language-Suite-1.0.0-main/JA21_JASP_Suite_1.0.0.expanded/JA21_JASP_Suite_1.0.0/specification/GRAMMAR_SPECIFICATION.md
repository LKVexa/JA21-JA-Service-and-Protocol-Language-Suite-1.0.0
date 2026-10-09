# Grammar Specification

The provisional grammar describes the source patterns represented by the corpus. It is a publication and implementation aid, not a claim of compatibility with an unavailable production compiler. The grammar makes service boundaries, messages, endpoints, policies, protocol states, transitions, transport effects, assertions, and emissions visible in source.

## Required design properties

1. Network effects are explicit and capability-controlled.
2. Request, response, and error envelopes are typed.
3. Retry is interpreted with idempotency and delivery guarantees.
4. Protocol transitions are statically analyzable.
5. Compatibility versions and serialization identities remain stable evidence.
6. Runtime lowering emits R12 and MCRT identities without erasing policy decisions.
