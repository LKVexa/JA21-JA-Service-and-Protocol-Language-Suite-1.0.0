# JA21 JA Service and Protocol Language Textbook

**Edition:** 1.0.0  
**Profile:** `ja.service`  
**Extension:** `.jasp`  

This textbook treats service and protocol design as a language-engineering discipline. Each chapter connects source, typed semantics, policy, compiler lowering, runtime behavior, R12 evidence, and MCRT provenance. The examples are drawn from the source corpus and remain labeled as modeled evidence until executed by a native JA implementation.

## How to use the book

Read chapters 1–10 for service-author foundations, 11–16 for governance and transport, 17–20 for compiler/runtime engineering, and 21–22 for certification and capstone integration. Each chapter ends with a laboratory and an evidence checklist.


# Chapter 1: The Service Contract as a Language Suite

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain why service design begins with explicit semantics rather than framework configuration.
2. Read and critique JA Service source involving `service_declaration`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

A service declaration is not merely a list of routes. It is a compact statement about who may communicate, what data may cross a boundary, which orderings are legal, how failures are represented, and which evidence must survive execution. In JA21, that statement is linked to a typed AST, a semantic judgment, an R12 record, and an MCRT receipt. The result is a contract that can be inspected before implementation and audited after deployment.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00032`  
**Feature:** `service_declaration`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00032
use Service
policy explicit_network

service ServiceJASP_00032 {
    message Request34 { prompt: Text }
    message Response34 { token: Text, done: Flag }
    endpoint infer(request: Request34) -> Stream<Response34>
        auth capability model.infer
        deadline 34s
        retry max 2
        idempotency request.prompt
    protocol Session34 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00032.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `902546617871b76b9044fbb5b676493d72c5bfbe33b348d6aed786f8ef3394ce` |
| AST node | `node-ce256e34ac9f10fb85f8` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-ce256e34ac9f10fb85f8 : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-a9273cd37724ea1d4400` / `service_declare` |
| MCRT | `mcrt-debb096491a68deb6471` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `service_declaration`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 2: Program Anatomy, Modules, and Network Policy

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how modules, imports, and network policy establish the authority boundary.
2. Read and critique JA Service source involving `service_declaration`, `network_capability`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

The first lines of a `.jasp` program establish the language version, module identity, imported service domain, and network policy. These lines are part of the security model. An explicit-network policy does not grant access by itself; it permits later declarations to request a named capability. A no-network policy makes remote transport invalid and directs authors toward local or offline transports.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00032`  
**Feature:** `service_declaration`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00032
use Service
policy explicit_network

service ServiceJASP_00032 {
    message Request34 { prompt: Text }
    message Response34 { token: Text, done: Flag }
    endpoint infer(request: Request34) -> Stream<Response34>
        auth capability model.infer
        deadline 34s
        retry max 2
        idempotency request.prompt
    protocol Session34 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00032.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `902546617871b76b9044fbb5b676493d72c5bfbe33b348d6aed786f8ef3394ce` |
| AST node | `node-ce256e34ac9f10fb85f8` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-ce256e34ac9f10fb85f8 : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-a9273cd37724ea1d4400` / `service_declare` |
| MCRT | `mcrt-debb096491a68deb6471` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `service_declaration`, `network_capability`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 3: Messages, Fields, and Schema Identity

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how schema identity protects callers, servers, and archived evidence.
2. Read and critique JA Service source involving `request_schema`, `response_schema`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Messages define the shape of the boundary. Request fields, response fields, stream items, command payloads, events, and error details are all typed objects with stable identities. Validation occurs before dispatch or emission. A schema change therefore affects compatibility, serialization, generated interfaces, test doubles, and archived receipts at once.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00005`  
**Feature:** `request_schema`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00005
use Service
policy explicit_network

service ServiceJASP_00005 {
    message Request7 { prompt: Text }
    message Response7 { token: Text, done: Flag }
    endpoint infer(request: Request7) -> Stream<Response7>
        auth capability model.infer
        deadline 7s
        retry max 2
        idempotency request.prompt
    protocol Session7 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00005.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `9914fa7ae1bd3d078f190fbaf6414d2e0ddaffd0ec3ecdc496f66805e5a7cf39` |
| AST node | `node-3ea6534fd660b0994048` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {stream.open:bounded} ⊢ node-3ea6534fd660b0994048 : ServiceContract ! {network.connect} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-5d10510454103418db9c` / `endpoint_bind` |
| MCRT | `mcrt-7b6c928dae7e33a86e86` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `request_schema`, `response_schema`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 4: Endpoints, Methods, and Error Contracts

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how success and failure share a versioned interface.
2. Read and critique JA Service source involving `endpoint`, `method`, `error_contract`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

An endpoint combines input type, output type, authority, time bounds, retry behavior, and idempotency. A method name alone is insufficient. The error contract must distinguish permanent rejection, transient failure, deadline exhaustion, incompatible version, and protocol violation so that callers do not invent recovery behavior.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00023`  
**Feature:** `endpoint`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00023
use Service
policy explicit_network

service ServiceJASP_00023 {
    message Request25 { prompt: Text }
    message Response25 { token: Text, done: Flag }
    endpoint infer(request: Request25) -> Stream<Response25>
        auth capability model.infer
        deadline 25s
        retry max 0
        idempotency request.prompt
    protocol Session25 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00023.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `20af71a53c2975924507d5834a1e331d4afd58bcfaea043ce369a18e4518c4d8` |
| AST node | `node-001356b577686a039b31` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {ledger.append} ⊢ node-001356b577686a039b31 : ServiceContract ! {network.connect} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-dfb79ed018d180145e4d` / `retry` |
| MCRT | `mcrt-2a3b6e94e6181302d927` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `endpoint`, `method`, `error_contract`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 5: Server Interfaces, Client Stubs, and Test Doubles

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how one contract produces governed server, client, and testing surfaces.
2. Read and critique JA Service source involving `server_interface`, `client_stub`, `test_double`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Server interfaces, client stubs, and test doubles are projections of one authoritative contract. The server receives an implementation obligation, the client receives a typed invocation surface, and the test double receives deterministic behavior and fixtures. Keeping these views derived prevents hand-written divergence.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00004`  
**Feature:** `server_interface`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00004
use Service
policy explicit_network

service ServiceJASP_00004 {
    message Request6 { prompt: Text }
    message Response6 { token: Text, done: Flag }
    endpoint infer(request: Request6) -> Stream<Response6>
        auth capability model.infer
        deadline 6s
        retry max 1
        idempotency request.prompt
    protocol Session6 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00004.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `270c975dc883ea9e9522037b6dfa5af43b47b4af8175d7a43804e152c7018134` |
| AST node | `node-a5f3e5a801a2a16050b1` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {network.listen:declared} ⊢ node-a5f3e5a801a2a16050b1 : ServiceContract ! {network.listen} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-077ba409bf24bca9cc5c` / `stream_open` |
| MCRT | `mcrt-c39c2a4125225afcf466` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `server_interface`, `client_stub`, `test_double`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 6: Serialization and Compatibility Versions

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how canonical serialization and version policy prevent silent drift.
2. Read and critique JA Service source involving `serialization`, `compatibility_version`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Serialization turns typed values into canonical bytes or text. Compatibility versions state which producers and consumers may exchange those representations. Canonical ordering, normalized defaults, stable field identity, and explicit migration rules are necessary because a syntactically readable payload may still have changed meaning.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00024`  
**Feature:** `serialization`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00024
use Service
policy explicit_network

service ServiceJASP_00024 {
    message Request26 { prompt: Text }
    message Response26 { token: Text, done: Flag }
    endpoint infer(request: Request26) -> Stream<Response26>
        auth capability model.infer
        deadline 26s
        retry max 1
        idempotency request.prompt
    protocol Session26 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00024.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `48179932dd6e4b87b44caa229f11439ec7ad962175cd989f12bf2abfa2f9bd02` |
| AST node | `node-c85c3d9a5e06214a4c49` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {network.listen:declared} ⊢ node-c85c3d9a5e06214a4c49 : ServiceContract ! {pure} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-b64a7b22e34afb4f2ee4` / `stream_open` |
| MCRT | `mcrt-7589c9398671d84fa640` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `serialization`, `compatibility_version`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 7: Commands, Events, and Delivery Guarantees

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how imperative and observational messages require different guarantees.
2. Read and critique JA Service source involving `command`, `event`, `delivery_guarantee`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Commands request change; events report facts. Delivery guarantees describe how duplicates, loss, acknowledgement, and replay are handled. Exactly-once claims require stronger identity and persistence evidence than at-least-once delivery, while at-most-once delivery may trade recovery for duplicate avoidance.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00010`  
**Feature:** `command`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00010
use Service
policy explicit_network

service ServiceJASP_00010 {
    message Request12 { prompt: Text }
    message Response12 { token: Text, done: Flag }
    endpoint infer(request: Request12) -> Stream<Response12>
        auth capability model.infer
        deadline 12s
        retry max 3
        idempotency request.prompt
    protocol Session12 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00010.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `6b9a8fd8c7a9520268d25c7dc0bd7bbc38aae844d7b6f1d1f150f85514841315` |
| AST node | `node-50e4f91f2968d51fa064` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {stream.open:bounded} ⊢ node-50e4f91f2968d51fa064 : ServiceContract ! {network.listen} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-95a793660607b1e7e810` / `transition` |
| MCRT | `mcrt-b69ffe1b55073822570e` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `command`, `event`, `delivery_guarantee`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 8: Protocol States and Transition Validation

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how state machines make legal order, reachability, and termination inspectable.
2. Read and critique JA Service source involving `protocol_state`, `protocol_validator`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

A protocol state machine makes order a first-class part of the contract. States must be declared, transitions must reference reachable states, and terminal behavior must be understood. A validator can then reject reversed, impossible, cyclic, or unauthorized transitions before any network or storage effect occurs.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00030`  
**Feature:** `protocol_state`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00030
use Service
policy explicit_network

service ServiceJASP_00030 {
    message Request32 { prompt: Text }
    message Response32 { token: Text, done: Flag }
    endpoint infer(request: Request32) -> Stream<Response32>
        auth capability model.infer
        deadline 32s
        retry max 3
        idempotency request.prompt
    protocol Session32 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00030.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `ebd9724ca24cd09f92bb26521fa612fe99723f198d962fe330881ef7797f261c` |
| AST node | `node-12f6e1990edb53de0d78` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {stream.open:bounded} ⊢ node-12f6e1990edb53de0d78 : ServiceContract ! {pure} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-c86d98d44d0d841dfb71` / `transition` |
| MCRT | `mcrt-4f5cd38bc2d6395dbb37` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `protocol_state`, `protocol_validator`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 9: Bidirectional Streams and Backpressure

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how producers and consumers coordinate without unbounded queues.
2. Read and critique JA Service source involving `bidirectional_stream`, `backpressure`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Bidirectional streams combine two independently progressing sequences. Correctness depends on message ordering, half-close behavior, cancellation, terminal frames, and backpressure. The consumer must be able to slow the producer without losing protocol identity or allowing unbounded memory growth.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00001`  
**Feature:** `bidirectional_stream`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00001
use Service
policy explicit_network

service ServiceJASP_00001 {
    message Request3 { prompt: Text }
    message Response3 { token: Text, done: Flag }
    endpoint infer(request: Request3) -> Stream<Response3>
        auth capability model.infer
        deadline 3s
        retry max 2
        idempotency request.prompt
    protocol Session3 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00001.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `8de1ba5fe47d1aefbe434c94519a4cb416a37f17e40de58b38697f3ed7fa4a3c` |
| AST node | `node-8ef1b3bfda8b17916636` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {network.connect:declared} ⊢ node-8ef1b3bfda8b17916636 : ServiceContract ! {ledger.append} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-5fdf98785bc5d0406d32` / `respond` |
| MCRT | `mcrt-b00446b69482f4999405` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `bidirectional_stream`, `backpressure`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 10: Retry, Backoff, Deadlines, and Idempotency

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how retry safety emerges from a coupled reliability contract.
2. Read and critique JA Service source involving `retry`, `backoff`, `deadline`, `idempotency`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Retry is safe only when the operation is eligible, the idempotency key is stable, the delivery guarantee is compatible, the deadline leaves time for another attempt, and backoff is bounded. Treating these clauses separately creates hidden failure modes; JA Service analyzes them as one coupled policy.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00002`  
**Feature:** `retry`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00002
use Service
policy explicit_network

service ServiceJASP_00002 {
    message Request4 { prompt: Text }
    message Response4 { token: Text, done: Flag }
    endpoint infer(request: Request4) -> Stream<Response4>
        auth capability model.infer
        deadline 4s
        retry max 3
        idempotency request.prompt
    protocol Session4 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00002.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `64076e90f6d0e96ba69d8eac4afcfbfbb92c57135dc242003741b455fe2be04e` |
| AST node | `node-90612ef33deebb58189f` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-90612ef33deebb58189f : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-a2c8eec8dc4876cfdcb7` / `service_declare` |
| MCRT | `mcrt-9439740f8d4fdf6fdd75` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `retry`, `backoff`, `deadline`, `idempotency`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 11: Quota and Rate-Limit Governance

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how aggregate limits and time-window limits differ and compose.
2. Read and critique JA Service source involving `quota`, `rate_limit`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Quota limits total consumption over a scope, whereas rate limits constrain frequency over a time window. Both need stable principal identity, deterministic accounting, and explicit behavior at the boundary. Backpressure handles immediate flow; quotas and rates handle governance over time.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00020`  
**Feature:** `quota`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00020
use Service
policy explicit_network

service ServiceJASP_00020 {
    message Request22 { prompt: Text }
    message Response22 { token: Text, done: Flag }
    endpoint infer(request: Request22) -> Stream<Response22>
        auth capability model.infer
        deadline 22s
        retry max 1
        idempotency request.prompt
    protocol Session22 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00020.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `4d808099afc0d721121ac3e9ed9ff2a8356c9a55add06e08e2f7ea6b005495de` |
| AST node | `node-3e5451389ffa9a2f2d7f` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {stream.open:bounded} ⊢ node-3e5451389ffa9a2f2d7f : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-fb69c6709c651f116f4a` / `transition` |
| MCRT | `mcrt-ec730c8ef2f88e96ecbd` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `quota`, `rate_limit`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 12: Authentication and Authorization

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how proof of identity is separated from permission to act.
2. Read and critique JA Service source involving `authentication`, `authorization`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Authentication answers who the caller is. Authorization answers whether that caller may perform this operation on this resource under current policy. Conflating the two leads to services that treat any valid identity as fully trusted. JA Service records both proof and decision evidence.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00015`  
**Feature:** `authentication`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00015
use Service
policy explicit_network

service ServiceJASP_00015 {
    message Request17 { prompt: Text }
    message Response17 { token: Text, done: Flag }
    endpoint infer(request: Request17) -> Stream<Response17>
        auth capability model.infer
        deadline 17s
        retry max 0
        idempotency request.prompt
    protocol Session17 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00015.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `e3280b98bf6e8e10d254cdfa95b008a16fd42f302400aa87a930621c32e269a2` |
| AST node | `node-c73d90fbacc76c65e615` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {stream.open:bounded} ⊢ node-c73d90fbacc76c65e615 : ServiceContract ! {state.read} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-f8fa2e87d87d7d4da064` / `endpoint_bind` |
| MCRT | `mcrt-1ac45c09b224c28b4bd5` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `authentication`, `authorization`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 13: Capabilities and Explicit Network Effects

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how network effects become reviewable inputs to policy.
2. Read and critique JA Service source involving `network_capability`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Network access is an effect and a capability requirement. A remote transport cannot be activated merely because an endpoint exists. The compiler and runtime must see an explicit capability path, a compatible policy, and a receipt showing whether authority was consumed.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00008`  
**Feature:** `network_capability`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00008
use Service
policy explicit_network

service ServiceJASP_00008 {
    message Request10 { prompt: Text }
    message Response10 { token: Text, done: Flag }
    endpoint infer(request: Request10) -> Stream<Response10>
        auth capability model.infer
        deadline 10s
        retry max 1
        idempotency request.prompt
    protocol Session10 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00008.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `93780fa7db9d700a035bf430c0092c8de592c3d2eb06d4dbbb3d44b9f290824c` |
| AST node | `node-ed6b2e4ae0636b1c9250` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {ledger.append} ⊢ node-ed6b2e4ae0636b1c9250 : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-d98d1343aae100cab9a9` / `request` |
| MCRT | `mcrt-c10fee166c4fd2901a03` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `network_capability`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 14: Local, Remote, and Offline Transports

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how the same service contract survives local, networked, and air-gapped operation.
2. Read and critique JA Service source involving `local_transport`, `remote_transport`, `offline_transport`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Local transport supports in-process or IPC operation, remote transport supports governed network exchange, and offline transport supports queues, files, bundles, or couriers. A well-designed contract keeps message and protocol meaning stable across these modes while making their effects and delivery properties explicit.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00003`  
**Feature:** `local_transport`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00003
use Service
policy explicit_network

service ServiceJASP_00003 {
    message Request5 { prompt: Text }
    message Response5 { token: Text, done: Flag }
    endpoint infer(request: Request5) -> Stream<Response5>
        auth capability model.infer
        deadline 5s
        retry max 0
        idempotency request.prompt
    protocol Session5 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00003.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `46004197990763cef8ec7c63d8b929d5dd14edf61df415cd7cab5f0350fe3782` |
| AST node | `node-0d0933380988ff1c7966` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {ledger.append} ⊢ node-0d0933380988ff1c7966 : ServiceContract ! {state.read} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-73a8c56ae1eb2a0241b1` / `retry` |
| MCRT | `mcrt-d3eb2475c6c01c215b13` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `local_transport`, `remote_transport`, `offline_transport`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 15: Service Discovery and Compatibility Resolution

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how discovery must preserve authority and version compatibility.
2. Read and critique JA Service source involving `service_discovery`, `compatibility_version`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Discovery maps a logical service identity to a candidate implementation. Resolution must filter by version, transport, authority, environment, and certification status. Discovery that returns a reachable endpoint but ignores compatibility is not successful resolution.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00012`  
**Feature:** `service_discovery`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00012
use Service
policy explicit_network

service ServiceJASP_00012 {
    message Request14 { prompt: Text }
    message Response14 { token: Text, done: Flag }
    endpoint infer(request: Request14) -> Stream<Response14>
        auth capability model.infer
        deadline 14s
        retry max 1
        idempotency request.prompt
    protocol Session14 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00012.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `c1c77e47543aa92c06039cc89d432ee6713b6ff2d37362648f70d031f0d8e0d4` |
| AST node | `node-29dc1bd17c9d9ed84d4d` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-29dc1bd17c9d9ed84d4d : ServiceContract ! {pure} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-7ee3ffae9babf491d519` / `service_declare` |
| MCRT | `mcrt-7a205d2004c17a33973d` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `service_discovery`, `compatibility_version`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 16: Schema and Protocol Validators

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how validators stop malformed data and illegal conversations before side effects.
2. Read and critique JA Service source involving `schema_validator`, `protocol_validator`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Schema validators reject malformed messages; protocol validators reject illegal conversations. Running these checks before dispatch reduces side effects and produces deterministic diagnostics. Validators themselves must be versioned and included in evidence because changing a validator can change which programs are accepted.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00027`  
**Feature:** `schema_validator`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00027
use Service
policy explicit_network

service ServiceJASP_00027 {
    message Request29 { prompt: Text }
    message Response29 { token: Text, done: Flag }
    endpoint infer(request: Request29) -> Stream<Response29>
        auth capability model.infer
        deadline 29s
        retry max 0
        idempotency request.prompt
    protocol Session29 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00027.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `8a1873bb2248e38a3a78401ddbe13888d40cd10abceb7099b0ef03c05d8afa15` |
| AST node | `node-083fd2f656917adce515` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-083fd2f656917adce515 : ServiceContract ! {state.read} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-c418edbda5dcdad1b11c` / `event_publish` |
| MCRT | `mcrt-eee606ead53720b6867c` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `schema_validator`, `protocol_validator`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 17: Typed ASTs and Semantic Judgments

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how source becomes stable nodes, inferred effects, and policy decisions.
2. Read and critique JA Service source involving `service_declaration`, `endpoint`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

The typed AST records source location, declared and inferred types, effects, capabilities, semantic status, and stable references. The semantic judgment explains why a node is accepted or rejected. This structure turns compiler behavior into inspectable evidence rather than an opaque yes-or-no result.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00032`  
**Feature:** `service_declaration`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00032
use Service
policy explicit_network

service ServiceJASP_00032 {
    message Request34 { prompt: Text }
    message Response34 { token: Text, done: Flag }
    endpoint infer(request: Request34) -> Stream<Response34>
        auth capability model.infer
        deadline 34s
        retry max 2
        idempotency request.prompt
    protocol Session34 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00032.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `902546617871b76b9044fbb5b676493d72c5bfbe33b348d6aed786f8ef3394ce` |
| AST node | `node-ce256e34ac9f10fb85f8` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-ce256e34ac9f10fb85f8 : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-a9273cd37724ea1d4400` / `service_declare` |
| MCRT | `mcrt-debb096491a68deb6471` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `service_declaration`, `endpoint`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 18: Compiler Pipeline and Deterministic Diagnostics

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how stable diagnostics support repair, testing, and certification.
2. Read and critique JA Service source involving `error_contract`, `schema_validator`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Stable diagnostic codes let tests and repair tools distinguish error families without depending on prose. Deterministic compilation means the same source, specification, and profile yield the same AST identities, judgments, diagnostics, R12 tuples, and artifact hashes.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00007`  
**Feature:** `error_contract`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00007
use Service
policy explicit_network

service ServiceJASP_00007 {
    message Request9 { prompt: Text }
    message Response9 { token: Text, done: Flag }
    endpoint infer(request: Request9) -> Stream<Response9>
        auth capability model.infer
        deadline 9s
        retry max 0
        idempotency request.prompt
    protocol Session9 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00007.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `634e3ecc7fd9785a81b0b72e2f5c538ef453d3e845c210a6505bbba6f1dbc511` |
| AST node | `node-b08b877ac4c0aba3316c` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-b08b877ac4c0aba3316c : ServiceContract ! {ledger.append} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-dd6005fddb62ab1041eb` / `event_publish` |
| MCRT | `mcrt-42e7708341f1b1d2d6c4` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `error_contract`, `schema_validator`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 19: JA Service Runtime and Deterministic Replay

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how scheduling, dispatch, sandboxing, and receipts preserve contract meaning.
2. Read and critique JA Service source involving `server_interface`, `local_transport`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

The runtime schedules dispatch, validates protocol state, enforces deadlines and limits, activates only authorized transports, redacts secrets, and records significant events. Replay uses stable inputs and receipts to reconstruct behavior without inventing hidden network access.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00004`  
**Feature:** `server_interface`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00004
use Service
policy explicit_network

service ServiceJASP_00004 {
    message Request6 { prompt: Text }
    message Response6 { token: Text, done: Flag }
    endpoint infer(request: Request6) -> Stream<Response6>
        auth capability model.infer
        deadline 6s
        retry max 1
        idempotency request.prompt
    protocol Session6 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00004.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `270c975dc883ea9e9522037b6dfa5af43b47b4af8175d7a43804e152c7018134` |
| AST node | `node-a5f3e5a801a2a16050b1` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {network.listen:declared} ⊢ node-a5f3e5a801a2a16050b1 : ServiceContract ! {network.listen} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-077ba409bf24bca9cc5c` / `stream_open` |
| MCRT | `mcrt-c39c2a4125225afcf466` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `server_interface`, `local_transport`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 20: Optimization Without Protocol Drift

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how fusion, batching, and table compression preserve ordering and evidence.
2. Read and critique JA Service source involving `serialization`, `backpressure`, `protocol_state`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

Optimization may deduplicate schemas, precompute validators, compress state tables, fuse stream stages, or batch messages. Each transform must preserve type meaning, policy decisions, ordering, delivery semantics, compatibility identities, and R12/MCRT links. Faster but unauditable is not equivalent.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00024`  
**Feature:** `serialization`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00024
use Service
policy explicit_network

service ServiceJASP_00024 {
    message Request26 { prompt: Text }
    message Response26 { token: Text, done: Flag }
    endpoint infer(request: Request26) -> Stream<Response26>
        auth capability model.infer
        deadline 26s
        retry max 1
        idempotency request.prompt
    protocol Session26 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00024.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `48179932dd6e4b87b44caa229f11439ec7ad962175cd989f12bf2abfa2f9bd02` |
| AST node | `node-c85c3d9a5e06214a4c49` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {network.listen:declared} ⊢ node-c85c3d9a5e06214a4c49 : ServiceContract ! {pure} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-b64a7b22e34afb4f2ee4` / `stream_open` |
| MCRT | `mcrt-7589c9398671d84fa640` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `serialization`, `backpressure`, `protocol_state`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 21: R12, MCRT, Certification, and Smithson 8S

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how provenance connects source, judgment, lowering, runtime, and certification.
2. Read and critique JA Service source involving `compatibility_version`, `delivery_guarantee`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

R12 gives a stable lowering record for a source statement; MCRT links source hash, AST node, semantic judgment, lowering, policy status, determinism class, and certification status. Smithson 8S annotations are retained as proposed coupling metadata, clearly separated from established physical law claims.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00021`  
**Feature:** `compatibility_version`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00021
use Service
policy explicit_network

service ServiceJASP_00021 {
    message Request23 { prompt: Text }
    message Response23 { token: Text, done: Flag }
    endpoint infer(request: Request23) -> Stream<Response23>
        auth capability model.infer
        deadline 23s
        retry max 2
        idempotency request.prompt
    protocol Session23 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00021.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `0d503542bdf212f4591eb3b0e2dbbf2539319751cda92d28d3ea0528f61b6f04` |
| AST node | `node-f97e16eb550c3ce2700e` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {network.connect:declared} ⊢ node-f97e16eb550c3ce2700e : ServiceContract ! {state.read} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-0cba845d1adf6d0d6760` / `respond` |
| MCRT | `mcrt-d9fcc36a0d77adbdb8c3` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `compatibility_version`, `delivery_guarantee`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?


# Chapter 22: Standalone Service and Protocol Toolchain Capstone

## Learning objectives

By the end of this chapter, you should be able to:

1. Explain how to build and audit a complete air-gap-capable service toolchain.
2. Read and critique JA Service source involving `service_declaration`, `endpoint`, `authentication`, `retry`, `offline_transport`.
3. Trace one declaration through AST, semantic judgment, R12, runtime, and MCRT evidence.
4. Identify at least one fail-closed diagnostic and one safe implementation strategy.

## Core idea

The capstone joins grammar, parser, type checker, policy analysis, protocol validation, artifact generation, deterministic runtime, offline transport, test doubles, evidence receipts, and certification. A complete toolchain is judged by reproducibility and explainability as much as by successful dispatch.

The practical consequence is that a service feature cannot be reviewed in isolation. Its type, effect, authority, ordering, compatibility, runtime behavior, and evidence identity form a coupled engineering object. SOPHIA checks semantic consistency; CHARLOTTE checks reconstructability and compatibility; LANDON checks executable workflow and operational diagnostics; Professor checks definitions and proof obligations; Podium checks whether the resulting publication can be navigated and audited.

## Corpus-derived example

**Record:** `JASP-00032`  
**Feature:** `service_declaration`  
**Level:** `beginner`  
**Validation class:** `positive`

```jasp
ja source 0.3
module corpus.ja_service.example_00032
use Service
policy explicit_network

service ServiceJASP_00032 {
    message Request34 { prompt: Text }
    message Response34 { token: Text, done: Flag }
    endpoint infer(request: Request34) -> Stream<Response34>
        auth capability model.infer
        deadline 34s
        retry max 2
        idempotency request.prompt
    protocol Session34 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00032.compatibility_report
```

## Evidence trace

| Layer | Identity or finding |
|---|---|
| Source hash | `902546617871b76b9044fbb5b676493d72c5bfbe33b348d6aed786f8ef3394ce` |
| AST node | `node-ce256e34ac9f10fb85f8` / `ServiceDecl` |
| Semantic judgment | `Environment; Policy; {service.invoke:authorized} ⊢ node-ce256e34ac9f10fb85f8 : ServiceContract ! {state.write} ⇒ validated` |
| Policy decision | `allow` |
| R12 | `r12-a9273cd37724ea1d4400` / `service_declare` |
| MCRT | `mcrt-debb096491a68deb6471` / `R3-Deterministic` |
| Expected result | `pass` |

This trace is modeled corpus evidence. A native compiler may confirm or challenge it, but must produce its own reproducible evidence rather than silently inheriting the expected result.

## Engineering checklist

- [ ] Types and schemas are explicit and closed.
- [ ] Effects and network capability requirements are visible.
- [ ] Authentication and authorization are not conflated.
- [ ] Ordering, retry, deadlines, delivery, and idempotency are jointly reviewed.
- [ ] Compatibility and serialization identities are stable.
- [ ] Diagnostics fail closed and retain repair context.
- [ ] R12 and MCRT links survive optimization and runtime dispatch.

## Laboratory

1. Copy the example into a local work directory.
2. Change one declaration related to `service_declaration`, `endpoint`, `authentication`, `retry`, `offline_transport`.
3. Predict the AST, semantic, policy, and diagnostic differences.
4. Produce a small evidence table with source hash, expected type, effects, capabilities, policy decision, and proposed R12/MCRT identities.
5. Write a deterministic test or static checker that distinguishes the original and modified programs without network access.

## Review questions

1. What contract property is most likely to be lost if this feature is implemented only in runtime code?
2. Which failure should be detected before transport activation?
3. What evidence proves that an optimization preserved behavior?
4. How would the design change for an offline transport?
