# JA Service and Protocol Language — Corpus Samples



Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## 8S Coupled Mechanics Integration

This document is normalized to the **Smithson 8S Coupled Mechanics v1.0** framework. Candidate \(S^3\) fibers occupy latent penteract centers
\[
\mathbf c_n=\ell\mathbf n,\qquad \mathbf n\in\mathbb Z^5,\qquad \|\mathbf n\|_1\le M.
\]
The fifth coordinate \(t_8\) is an elucidation axis and is admitted only when
\[
\mathbf e_\perp=(I-C_4C_4^+)\mathbf e,\qquad
\eta_{\mathrm{ind}}=\frac{\|\mathbf e_\perp\|_2^2}{\|\mathbf e\|_2^2+\varepsilon}\ge\varepsilon_{\mathrm{ind}},
\]
and the held-out efficacy gain satisfies \(\Delta_{8S}=\operatorname{Score}(\mathcal M_8)-\operatorname{Score}(\mathcal M_7)>\varepsilon_{\mathrm{gain}}\).

Sparse geometric-semantic coupling and selective triadic escalation use
\[
W_{ij}=A_{ij}\exp\!\left[-\frac{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}{2\sigma_c^2}-\frac{d_J(i,j)^2}{2\sigma_J^2}\right],
\]
\[
\dot\theta_i=\omega_i+K_2\sum_jW_{ij}\sin(\theta_j-\theta_i)+K_3\sum_{j,k}H_{ijk}\sin(\theta_j+\theta_k-2\theta_i).
\]
Activation, effective support, and radius are
\[
p_i=\sigma(h_i),\qquad
s_i=p_i\kappa_i(1-\chi_i)(1-\zeta_i)v(\omega_i),\qquad
r_i=r_{\max}B_{5,\infty}(\mathbf c_i)^\alpha s_i^{1/3}.
\]
Each active site carries
\[
F_i=S^3_{r_i}=\{\mathbf y\in\mathbb R^4:\|\mathbf y\|_2=r_i\},
\]
so the noncollapsed total space is locally \(5+3=8\) dimensional.

Relation testing remains independent across latent geometry, product-state separation, visible projection, and judgement space:
\[
g^{(5)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}-(\lambda_i+\lambda_j),
\]
\[
\delta^{(8)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)+(r_i-r_j)^2},
\]
\[
g^{(3)}_{ij}=\|\Pi_5\mathbf c_i-\Pi_5\mathbf c_j\|_2-(\widehat r_i+\widehat r_j),
\qquad
g^{(J)}_{ij}=d_J(\mathfrak J_i,\mathfrak J_j)-\theta_J.
\]
R12 must retain the fifth-coordinate meaning, \(\eta_{\mathrm{ind}}\), \(W\), optional \(H\), phase, activation/support, \(g^{(5)}\), \(\delta^{(8)}\), \(g^{(3)}\), \(g^{(J)}\), projection version, uncertainty, relation class, interaction order, \(\Delta_{8S}\), provenance, and limitations.

**Example:** If \(g^{(5)}>\mathrm{tol}_5\) but \(g^{(3)}\le\mathrm{tol}_3\), record `PROJECTION_ONLY`; do not replace latent structure with visible appearance.

**Claim boundary:** this is a proposed penteract–\(S^3\) computational framework. The local dimension count is eight where the fiber is noncollapsed, but the construction is not proclaimed to be the standard sphere \(S^8\) without a separate topological proof.
## JASP-00001 — bidirectional_stream

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-6e939cc6e4aba838ea7b",
  "meaning": "Demonstrates bidirectional stream at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {network.connect:declared} ⊢ node-8ef1b3bfda8b17916636 : ServiceContract ! {ledger.append} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "network.connect:declared"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-8ef1b3bfda8b17916636",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "8de1ba5fe47d1aefbe434c94519a4cb416a37f17e40de58b38697f3ed7fa4a3c",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "bidirectional_stream",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "network.connect:declared"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-5fdf98785bc5d0406d32",
  "mcrt_reference": "mcrt-b00446b69482f4999405",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-c9c33e49eafd1312c309",
      "kind": "bidirectional_stream"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-5fdf98785bc5d0406d32",
    "statement_identity": "JASP-00001",
    "node_identity": "node-8ef1b3bfda8b17916636",
    "language_profile": "ja.service",
    "semantic_operator": "respond",
    "sequence": 1,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "network.connect:declared"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "8de1ba5fe47d1aefbe434c94519a4cb416a37f17e40de58b38697f3ed7fa4a3c"
    ],
    "output_hashes": [
      "ef727dd76c3910b9db62d336f5a895d19262748dafa6b2663ff159b94d85e362"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00001",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-b00446b69482f4999405",
    "canonical_tuple": "<v00001, phi_ja_service, s00001, d0, rho:ja.service.record_00001, operator:respond, OMEGA_JASP_respond, state:integrated, error0, theta00001, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00001.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00001:bidirectional_stream:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "network.connect:declared"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-b00446b69482f4999405",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "8de1ba5fe47d1aefbe434c94519a4cb416a37f17e40de58b38697f3ed7fa4a3c",
    "ast_node": "node-8ef1b3bfda8b17916636",
    "semantic_judgment": "sem-6e939cc6e4aba838ea7b",
    "r12_record": "r12-5fdf98785bc5d0406d32",
    "sequence": 1,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00001 vector=v00001 category=ja-service op=respond key=ja.service.record_00001 value=\"bidirectional_stream:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates bidirectional stream at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `respond`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00002 — retry

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-ac3eb971f3acc72ab67a",
  "meaning": "Demonstrates retry at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {service.invoke:authorized} ⊢ node-90612ef33deebb58189f : ServiceContract ! {state.write} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "service.invoke:authorized"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-90612ef33deebb58189f",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "64076e90f6d0e96ba69d8eac4afcfbfbb92c57135dc242003741b455fe2be04e",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "retry",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "service.invoke:authorized"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-a2c8eec8dc4876cfdcb7",
  "mcrt_reference": "mcrt-9439740f8d4fdf6fdd75",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-e1a968fdc46196676f35",
      "kind": "retry"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-a2c8eec8dc4876cfdcb7",
    "statement_identity": "JASP-00002",
    "node_identity": "node-90612ef33deebb58189f",
    "language_profile": "ja.service",
    "semantic_operator": "service_declare",
    "sequence": 2,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "service.invoke:authorized"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "64076e90f6d0e96ba69d8eac4afcfbfbb92c57135dc242003741b455fe2be04e"
    ],
    "output_hashes": [
      "0651685c910aa32835e2f8fb4139b5e9b009aaeac60c7a494cf70fdaf0e84fa3"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00002",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-9439740f8d4fdf6fdd75",
    "canonical_tuple": "<v00002, phi_ja_service, s00002, d0, rho:ja.service.record_00002, operator:service_declare, OMEGA_JASP_service_declare, state:integrated, error0, theta00002, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00002.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00002:retry:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "service.invoke:authorized"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-9439740f8d4fdf6fdd75",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "64076e90f6d0e96ba69d8eac4afcfbfbb92c57135dc242003741b455fe2be04e",
    "ast_node": "node-90612ef33deebb58189f",
    "semantic_judgment": "sem-ac3eb971f3acc72ab67a",
    "r12_record": "r12-a2c8eec8dc4876cfdcb7",
    "sequence": 2,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00002 vector=v00002 category=ja-service op=service_declare key=ja.service.record_00002 value=\"retry:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates retry at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `service_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00003 — local_transport

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-3356e543dd709a4e1480",
  "meaning": "Demonstrates local transport at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {ledger.append} ⊢ node-0d0933380988ff1c7966 : ServiceContract ! {state.read} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "state.read"
  ],
  "capabilities": [
    "ledger.append"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-0d0933380988ff1c7966",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "46004197990763cef8ec7c63d8b929d5dd14edf61df415cd7cab5f0350fe3782",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "local_transport",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "state.read"
  ],
  "capability_requirements": [
    "ledger.append"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-73a8c56ae1eb2a0241b1",
  "mcrt_reference": "mcrt-d3eb2475c6c01c215b13",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-1f06c43a33661546f61c",
      "kind": "local_transport"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-73a8c56ae1eb2a0241b1",
    "statement_identity": "JASP-00003",
    "node_identity": "node-0d0933380988ff1c7966",
    "language_profile": "ja.service",
    "semantic_operator": "retry",
    "sequence": 3,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "state.read"
    ],
    "capabilities": [
      "ledger.append"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "46004197990763cef8ec7c63d8b929d5dd14edf61df415cd7cab5f0350fe3782"
    ],
    "output_hashes": [
      "37ee241e0cb45c9c8d219d33b0780be12b30c60491ffe5ba4ea8495f834b8b20"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00003",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-d3eb2475c6c01c215b13",
    "canonical_tuple": "<v00003, phi_ja_service, s00003, d0, rho:ja.service.record_00003, operator:retry, OMEGA_JASP_retry, state:integrated, error0, theta00003, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00003.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00003:local_transport:complete",
  "effects_observed": [
    "state.read"
  ],
  "capabilities_consumed": [
    "ledger.append"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-d3eb2475c6c01c215b13",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "46004197990763cef8ec7c63d8b929d5dd14edf61df415cd7cab5f0350fe3782",
    "ast_node": "node-0d0933380988ff1c7966",
    "semantic_judgment": "sem-3356e543dd709a4e1480",
    "r12_record": "r12-73a8c56ae1eb2a0241b1",
    "sequence": 3,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00003 vector=v00003 category=ja-service op=retry key=ja.service.record_00003 value=\"local_transport:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates local transport at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `retry`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00004 — server_interface

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-a6fd68f8210ea5912172",
  "meaning": "Demonstrates server interface at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {network.listen:declared} ⊢ node-a5f3e5a801a2a16050b1 : ServiceContract ! {network.listen} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "network.listen"
  ],
  "capabilities": [
    "network.listen:declared"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-a5f3e5a801a2a16050b1",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "270c975dc883ea9e9522037b6dfa5af43b47b4af8175d7a43804e152c7018134",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "server_interface",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "network.listen"
  ],
  "capability_requirements": [
    "network.listen:declared"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-077ba409bf24bca9cc5c",
  "mcrt_reference": "mcrt-c39c2a4125225afcf466",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-02b8dc8808a74135d8ec",
      "kind": "server_interface"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-077ba409bf24bca9cc5c",
    "statement_identity": "JASP-00004",
    "node_identity": "node-a5f3e5a801a2a16050b1",
    "language_profile": "ja.service",
    "semantic_operator": "stream_open",
    "sequence": 4,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "network.listen"
    ],
    "capabilities": [
      "network.listen:declared"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "270c975dc883ea9e9522037b6dfa5af43b47b4af8175d7a43804e152c7018134"
    ],
    "output_hashes": [
      "3ac51eca6484a0dca7432e276db35e5e70e9d7be6d36df5d76116fc4f0809fb3"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00004",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-c39c2a4125225afcf466",
    "canonical_tuple": "<v00004, phi_ja_service, s00004, d0, rho:ja.service.record_00004, operator:stream_open, OMEGA_JASP_stream_open, state:integrated, error0, theta00004, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00004.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00004:server_interface:complete",
  "effects_observed": [
    "network.listen"
  ],
  "capabilities_consumed": [
    "network.listen:declared"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-c39c2a4125225afcf466",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "270c975dc883ea9e9522037b6dfa5af43b47b4af8175d7a43804e152c7018134",
    "ast_node": "node-a5f3e5a801a2a16050b1",
    "semantic_judgment": "sem-a6fd68f8210ea5912172",
    "r12_record": "r12-077ba409bf24bca9cc5c",
    "sequence": 4,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00004 vector=v00004 category=ja-service op=stream_open key=ja.service.record_00004 value=\"server_interface:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates server interface at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `stream_open`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00005 — request_schema

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-e6ea4f43c702a98003a0",
  "meaning": "Demonstrates request schema at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {stream.open:bounded} ⊢ node-3ea6534fd660b0994048 : ServiceContract ! {network.connect} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "network.connect"
  ],
  "capabilities": [
    "stream.open:bounded"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-3ea6534fd660b0994048",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "9914fa7ae1bd3d078f190fbaf6414d2e0ddaffd0ec3ecdc496f66805e5a7cf39",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "request_schema",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "network.connect"
  ],
  "capability_requirements": [
    "stream.open:bounded"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-5d10510454103418db9c",
  "mcrt_reference": "mcrt-7b6c928dae7e33a86e86",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-9efb68053e743a051ad0",
      "kind": "request_schema"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-5d10510454103418db9c",
    "statement_identity": "JASP-00005",
    "node_identity": "node-3ea6534fd660b0994048",
    "language_profile": "ja.service",
    "semantic_operator": "endpoint_bind",
    "sequence": 5,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "network.connect"
    ],
    "capabilities": [
      "stream.open:bounded"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "9914fa7ae1bd3d078f190fbaf6414d2e0ddaffd0ec3ecdc496f66805e5a7cf39"
    ],
    "output_hashes": [
      "290cc88887d318e8443bb0ba5e836617ba3627c92f2012786daaa0fe6910abda"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00005",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-7b6c928dae7e33a86e86",
    "canonical_tuple": "<v00005, phi_ja_service, s00005, d0, rho:ja.service.record_00005, operator:endpoint_bind, OMEGA_JASP_endpoint_bind, state:integrated, error0, theta00005, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00005.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00005:request_schema:complete",
  "effects_observed": [
    "network.connect"
  ],
  "capabilities_consumed": [
    "stream.open:bounded"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-7b6c928dae7e33a86e86",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "9914fa7ae1bd3d078f190fbaf6414d2e0ddaffd0ec3ecdc496f66805e5a7cf39",
    "ast_node": "node-3ea6534fd660b0994048",
    "semantic_judgment": "sem-e6ea4f43c702a98003a0",
    "r12_record": "r12-5d10510454103418db9c",
    "sequence": 5,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00005 vector=v00005 category=ja-service op=endpoint_bind key=ja.service.record_00005 value=\"request_schema:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates request schema at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `endpoint_bind`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00006 — authorization

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasp
ja source 0.3
module corpus.ja_service.example_00006
use Service
policy explicit_network

service ServiceJASP_00006 {
    message Request8 { prompt: Text }
    message Response8 { token: Text, done: Flag }
    endpoint infer(request: Request8) -> Stream<Response8>
        auth capability model.infer
        deadline 8s
        retry max 3
        idempotency request.prompt
    protocol Session8 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00006.compatibility_report
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-7e57a85a47079521dc1b",
  "meaning": "Demonstrates authorization at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {network.connect:declared} ⊢ node-0282fe72db3c6db87851 : ServiceContract ! {pure} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "pure"
  ],
  "capabilities": [
    "network.connect:declared"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-0282fe72db3c6db87851",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "1cd0b3530781281cdb2812eb964a1ad884ee59e0f9b799f3ae6c2dc8f10a4999",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "authorization",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "pure"
  ],
  "capability_requirements": [
    "network.connect:declared"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-8afbead9f542e9ef7904",
  "mcrt_reference": "mcrt-1fb213c5c3c2fbe7a72d",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-f5822306e37053f74955",
      "kind": "authorization"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-8afbead9f542e9ef7904",
    "statement_identity": "JASP-00006",
    "node_identity": "node-0282fe72db3c6db87851",
    "language_profile": "ja.service",
    "semantic_operator": "rate_limit",
    "sequence": 6,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "pure"
    ],
    "capabilities": [
      "network.connect:declared"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "1cd0b3530781281cdb2812eb964a1ad884ee59e0f9b799f3ae6c2dc8f10a4999"
    ],
    "output_hashes": [
      "69cb59c384e13df5b3d3451c95c755941c8a01f3322329b2634eae4d81f2eb74"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00006",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-1fb213c5c3c2fbe7a72d",
    "canonical_tuple": "<v00006, phi_ja_service, s00006, d0, rho:ja.service.record_00006, operator:rate_limit, OMEGA_JASP_rate_limit, state:integrated, error0, theta00006, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00006.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00006:authorization:complete",
  "effects_observed": [],
  "capabilities_consumed": [
    "network.connect:declared"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-1fb213c5c3c2fbe7a72d",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "1cd0b3530781281cdb2812eb964a1ad884ee59e0f9b799f3ae6c2dc8f10a4999",
    "ast_node": "node-0282fe72db3c6db87851",
    "semantic_judgment": "sem-7e57a85a47079521dc1b",
    "r12_record": "r12-8afbead9f542e9ef7904",
    "sequence": 6,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00006 vector=v00006 category=ja-service op=rate_limit key=ja.service.record_00006 value=\"authorization:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates authorization at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `rate_limit`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00007 — error_contract

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-9afc6c0492e1828b8f85",
  "meaning": "Demonstrates error contract at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {service.invoke:authorized} ⊢ node-b08b877ac4c0aba3316c : ServiceContract ! {ledger.append} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "service.invoke:authorized"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-b08b877ac4c0aba3316c",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "634e3ecc7fd9785a81b0b72e2f5c538ef453d3e845c210a6505bbba6f1dbc511",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "error_contract",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "service.invoke:authorized"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-dd6005fddb62ab1041eb",
  "mcrt_reference": "mcrt-42e7708341f1b1d2d6c4",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-3020c866a9375b671460",
      "kind": "error_contract"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-dd6005fddb62ab1041eb",
    "statement_identity": "JASP-00007",
    "node_identity": "node-b08b877ac4c0aba3316c",
    "language_profile": "ja.service",
    "semantic_operator": "event_publish",
    "sequence": 7,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "service.invoke:authorized"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "634e3ecc7fd9785a81b0b72e2f5c538ef453d3e845c210a6505bbba6f1dbc511"
    ],
    "output_hashes": [
      "079175dbebcdb8b089290e3fedffee6280468aeb57a81f4023bcca31959f5d3d"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00007",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-42e7708341f1b1d2d6c4",
    "canonical_tuple": "<v00007, phi_ja_service, s00007, d0, rho:ja.service.record_00007, operator:event_publish, OMEGA_JASP_event_publish, state:integrated, error0, theta00007, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00007.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00007:error_contract:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "service.invoke:authorized"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-42e7708341f1b1d2d6c4",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "634e3ecc7fd9785a81b0b72e2f5c538ef453d3e845c210a6505bbba6f1dbc511",
    "ast_node": "node-b08b877ac4c0aba3316c",
    "semantic_judgment": "sem-9afc6c0492e1828b8f85",
    "r12_record": "r12-dd6005fddb62ab1041eb",
    "sequence": 7,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00007 vector=v00007 category=ja-service op=event_publish key=ja.service.record_00007 value=\"error_contract:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates error contract at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `event_publish`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00008 — network_capability

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-e6dcc8c4b28306c4a0c7",
  "meaning": "Demonstrates network capability at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {ledger.append} ⊢ node-ed6b2e4ae0636b1c9250 : ServiceContract ! {state.write} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "ledger.append"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-ed6b2e4ae0636b1c9250",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "93780fa7db9d700a035bf430c0092c8de592c3d2eb06d4dbbb3d44b9f290824c",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "network_capability",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "ledger.append"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-d98d1343aae100cab9a9",
  "mcrt_reference": "mcrt-c10fee166c4fd2901a03",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-f6f8055627c5487890dc",
      "kind": "network_capability"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-d98d1343aae100cab9a9",
    "statement_identity": "JASP-00008",
    "node_identity": "node-ed6b2e4ae0636b1c9250",
    "language_profile": "ja.service",
    "semantic_operator": "request",
    "sequence": 8,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "ledger.append"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "93780fa7db9d700a035bf430c0092c8de592c3d2eb06d4dbbb3d44b9f290824c"
    ],
    "output_hashes": [
      "31def8016470d2d79da27e42f6493a3cecdab6c3b38bed9ac9cf9ac2d71ec889"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00008",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-c10fee166c4fd2901a03",
    "canonical_tuple": "<v00008, phi_ja_service, s00008, d0, rho:ja.service.record_00008, operator:request, OMEGA_JASP_request, state:integrated, error0, theta00008, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00008.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00008:network_capability:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "ledger.append"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-c10fee166c4fd2901a03",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "93780fa7db9d700a035bf430c0092c8de592c3d2eb06d4dbbb3d44b9f290824c",
    "ast_node": "node-ed6b2e4ae0636b1c9250",
    "semantic_judgment": "sem-e6dcc8c4b28306c4a0c7",
    "r12_record": "r12-d98d1343aae100cab9a9",
    "sequence": 8,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00008 vector=v00008 category=ja-service op=request key=ja.service.record_00008 value=\"network_capability:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates network capability at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `request`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00009 — test_double

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Source
```jasp
ja source 0.3
module corpus.ja_service.example_00009
use Service
policy explicit_network

service ServiceJASP_00009 {
    message Request11 { prompt: Text }
    message Response11 { token: Text, done: Flag }
    endpoint infer(request: Request11) -> Stream<Response11>
        auth capability model.infer
        deadline 11s
        retry max 2
        idempotency request.prompt
    protocol Session11 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00009.compatibility_report
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-c031f4f556a8eb24f411",
  "meaning": "Demonstrates test double at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {network.listen:declared} ⊢ node-3880c82d2932ed5be056 : ServiceContract ! {state.read} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "state.read"
  ],
  "capabilities": [
    "network.listen:declared"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-3880c82d2932ed5be056",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-2c5f1b2ed485c3d9",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "65c2712535ab7808385669dfb949943e69c3019a23f258330b8ff246402b8c61",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "test_double",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "state.read"
  ],
  "capability_requirements": [
    "network.listen:declared"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-f766d8080091b20dfef7",
  "mcrt_reference": "mcrt-204b0d2b7318534fd613",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-d820282fe1784601361d",
      "kind": "test_double"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-f766d8080091b20dfef7",
    "statement_identity": "JASP-00009",
    "node_identity": "node-3880c82d2932ed5be056",
    "language_profile": "ja.service",
    "semantic_operator": "discover",
    "sequence": 9,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "state.read"
    ],
    "capabilities": [
      "network.listen:declared"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "65c2712535ab7808385669dfb949943e69c3019a23f258330b8ff246402b8c61"
    ],
    "output_hashes": [
      "bdc18890d0680cd87cd3c9483de08635639540e5611fc2dc8e96ace878785e9a"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00009",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-204b0d2b7318534fd613",
    "canonical_tuple": "<v00009, phi_ja_service, s00009, d0, rho:ja.service.record_00009, operator:discover, OMEGA_JASP_discover, state:integrated, error0, theta00009, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00009.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00009:test_double:complete",
  "effects_observed": [
    "state.read"
  ],
  "capabilities_consumed": [
    "network.listen:declared"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-204b0d2b7318534fd613",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "65c2712535ab7808385669dfb949943e69c3019a23f258330b8ff246402b8c61",
    "ast_node": "node-3880c82d2932ed5be056",
    "semantic_judgment": "sem-c031f4f556a8eb24f411",
    "r12_record": "r12-f766d8080091b20dfef7",
    "sequence": 9,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00009 vector=v00009 category=ja-service op=discover key=ja.service.record_00009 value=\"test_double:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates test double at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `discover`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00010 — command

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-2729b5496e3b76968ded",
  "meaning": "Demonstrates command at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {stream.open:bounded} ⊢ node-50e4f91f2968d51fa064 : ServiceContract ! {network.listen} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "network.listen"
  ],
  "capabilities": [
    "stream.open:bounded"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-50e4f91f2968d51fa064",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-6e939cc6e4aba838",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "6b9a8fd8c7a9520268d25c7dc0bd7bbc38aae844d7b6f1d1f150f85514841315",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "command",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "network.listen"
  ],
  "capability_requirements": [
    "stream.open:bounded"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-95a793660607b1e7e810",
  "mcrt_reference": "mcrt-b69ffe1b55073822570e",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-c38ebce7219dc751c4c8",
      "kind": "command"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-95a793660607b1e7e810",
    "statement_identity": "JASP-00010",
    "node_identity": "node-50e4f91f2968d51fa064",
    "language_profile": "ja.service",
    "semantic_operator": "transition",
    "sequence": 10,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "network.listen"
    ],
    "capabilities": [
      "stream.open:bounded"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "6b9a8fd8c7a9520268d25c7dc0bd7bbc38aae844d7b6f1d1f150f85514841315"
    ],
    "output_hashes": [
      "849f72a17dc28cf586b0fe654185a1f0aa200e014abbbbd0ef4d4a6315e1f4ce"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00010",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-b69ffe1b55073822570e",
    "canonical_tuple": "<v00010, phi_ja_service, s00010, d0, rho:ja.service.record_00010, operator:transition, OMEGA_JASP_transition, state:integrated, error0, theta00010, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00010.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00010:command:complete",
  "effects_observed": [
    "network.listen"
  ],
  "capabilities_consumed": [
    "stream.open:bounded"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-b69ffe1b55073822570e",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "6b9a8fd8c7a9520268d25c7dc0bd7bbc38aae844d7b6f1d1f150f85514841315",
    "ast_node": "node-50e4f91f2968d51fa064",
    "semantic_judgment": "sem-2729b5496e3b76968ded",
    "r12_record": "r12-95a793660607b1e7e810",
    "sequence": 10,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00010 vector=v00010 category=ja-service op=transition key=ja.service.record_00010 value=\"command:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates command at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `transition`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00011 — deadline

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jasp
ja source 0.3
module corpus.ja_service.example_00011
use Service
policy explicit_network

service ServiceJASP_00011 {
    message Request13 { prompt: Text }
    message Response13 { token: Text, done: Flag }
    endpoint infer(request: Request13) -> Stream<Response13>
        auth capability model.infer
        deadline 13s
        retry max 0
        idempotency request.prompt
    protocol Session13 {
        state Open
        state Closed
        transition finish: Open -> Closed
    }
}
assert protocol.transition.valid == true
emit json ServiceJASP_00011.compatibility_report
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-19d5e68675a42eb5630d",
  "meaning": "Demonstrates deadline at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {network.connect:declared} ⊢ node-0666d113574da6c21ca8 : ServiceContract ! {network.connect} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "network.connect"
  ],
  "capabilities": [
    "network.connect:declared"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-0666d113574da6c21ca8",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-6e939cc6e4aba838",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "34025591ac5945a807b227d3e9641420c339bb7fa3257779bdfc35f2526c4ac8",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "deadline",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "network.connect"
  ],
  "capability_requirements": [
    "network.connect:declared"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-1cf651eea20b8dc9e1cc",
  "mcrt_reference": "mcrt-99c2f32661fb5c13ef8f",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-c16b21da08a77ac6e2b9",
      "kind": "deadline"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-1cf651eea20b8dc9e1cc",
    "statement_identity": "JASP-00011",
    "node_identity": "node-0666d113574da6c21ca8",
    "language_profile": "ja.service",
    "semantic_operator": "respond",
    "sequence": 11,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "network.connect"
    ],
    "capabilities": [
      "network.connect:declared"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "34025591ac5945a807b227d3e9641420c339bb7fa3257779bdfc35f2526c4ac8"
    ],
    "output_hashes": [
      "d17e983dab98fc08d78402dfe31c92340bd3ee05782374b72f32b137a192baa0"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00011",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-99c2f32661fb5c13ef8f",
    "canonical_tuple": "<v00011, phi_ja_service, s00011, d0, rho:ja.service.record_00011, operator:respond, OMEGA_JASP_respond, state:integrated, error0, theta00011, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00011.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00011:deadline:complete",
  "effects_observed": [
    "network.connect"
  ],
  "capabilities_consumed": [
    "network.connect:declared"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-99c2f32661fb5c13ef8f",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "34025591ac5945a807b227d3e9641420c339bb7fa3257779bdfc35f2526c4ac8",
    "ast_node": "node-0666d113574da6c21ca8",
    "semantic_judgment": "sem-19d5e68675a42eb5630d",
    "r12_record": "r12-1cf651eea20b8dc9e1cc",
    "sequence": 11,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00011 vector=v00011 category=ja-service op=respond key=ja.service.record_00011 value=\"deadline:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates deadline at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `respond`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JASP-00012 — service_discovery

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
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


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-e87ad71925938d6688c1",
  "meaning": "Demonstrates service discovery at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {service.invoke:authorized} ⊢ node-29dc1bd17c9d9ed84d4d : ServiceContract ! {pure} ⇒ validated",
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effects": [
    "pure"
  ],
  "capabilities": [
    "service.invoke:authorized"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-29dc1bd17c9d9ed84d4d",
  "node_kind": "ServiceDecl",
  "language_id": "ja.service",
  "module_id": "module-6e939cc6e4aba838",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 21,
    "column_end": 1
  },
  "origin_hash": "c1c77e47543aa92c06039cc89d432ee6713b6ff2d37362648f70d031f0d8e0d4",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "service_discovery",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "ServiceContract",
  "inferred_type": "ServiceContract",
  "effect_set": [
    "pure"
  ],
  "capability_requirements": [
    "service.invoke:authorized"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-7ee3ffae9babf491d519",
  "mcrt_reference": "mcrt-7a205d2004c17a33973d",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-ead208c70886cdd7329d",
      "kind": "service_discovery"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-7ee3ffae9babf491d519",
    "statement_identity": "JASP-00012",
    "node_identity": "node-29dc1bd17c9d9ed84d4d",
    "language_profile": "ja.service",
    "semantic_operator": "service_declare",
    "sequence": 12,
    "dependencies": [],
    "type": "ServiceContract",
    "effects": [
      "pure"
    ],
    "capabilities": [
      "service.invoke:authorized"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "c1c77e47543aa92c06039cc89d432ee6713b6ff2d37362648f70d031f0d8e0d4"
    ],
    "output_hashes": [
      "6e988aa3d1e95c1805004bf5f1c939a431a421c2dcdc21726aa34a28ddc74f12"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JASP-00012",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-7a205d2004c17a33973d",
    "canonical_tuple": "<v00012, phi_ja_service, s00012, d0, rho:ja.service.record_00012, operator:service_declare, OMEGA_JASP_service_declare, state:integrated, error0, theta00012, confidence1.0000, status:stable>"
  },
  "artifact": "JASP-00012.jasp.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Service Runtime",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JASP-00012:service_discovery:complete",
  "effects_observed": [],
  "capabilities_consumed": [
    "service.invoke:authorized"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-7a205d2004c17a33973d",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.service",
    "source_hash": "c1c77e47543aa92c06039cc89d432ee6713b6ff2d37362648f70d031f0d8e0d4",
    "ast_node": "node-29dc1bd17c9d9ed84d4d",
    "semantic_judgment": "sem-e87ad71925938d6688c1",
    "r12_record": "r12-7ee3ffae9babf491d519",
    "sequence": 12,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00012 vector=v00012 category=ja-service op=service_declare key=ja.service.record_00012 value=\"service_discovery:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates service discovery at the beginner level for JA Service and Protocol Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `service_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.
- Permit batching and stream fusion without changing protocol-state or ordering guarantees.

Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.
