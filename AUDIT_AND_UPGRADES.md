# JA21 JA Service and Protocol Language Suite 1 0 0 main Updated Corpus Audit

This updated copy supplies typed messages, protocol states, deadlines, retries and idempotency. Its import boundary is: Metadata header is not an extra program; prove actual transport failure behavior.

## Source and coverage

Original input: `JA21-JA-Service-and-Protocol-Language-Suite-1.0.0-main.zip`. Source SHA 256: `a29639245b9fd11639622abfe179f7b690093ff44aa4b102fb8e73de14a9f375`. The source archive is preserved in the parent folder. All 1,071 original leaf files were read and hashed; 31,009 stored JSONL rows were structurally parsed, including historical/reconstructed copies. Nested ZIPs are materialized in `.expanded` directories. Dataset row counts include duplicate representations and metadata headers; they are not unique executable programs.

Original checks and locations are in [the source manifest](audit/source_manifest.json). Current payload bytes are in [the updated manifest](audit/updated_manifest.json), and changes are in [the ledger](audit/change_ledger.json). Embedded source layers have [separate coverage](audit/embedded_layer_coverage.json). Historical hashes and modeled labels retain their historical meaning. The updated manifest and qualification sidecars govern this release.

## Upgrades and open implementation work

### JA-10 Medium priority

The original master contains 10,001 JSON lines: 10,000 source examples and a document coupling preamble. Preamble metadata must not enter example-schema validation or source compilation.

Status: **mitigated_by_explicit_evidence_qualification**. Current records are qualified as modeled expectations; source hash and lexical requirement consistency recorded.

Evidence: `JA21_JASP_Suite_1.0.0/corpus/technical/JA21_JASP_TECHNICAL_CORPUS_10000.jsonl.gz | JA21_JASP_Suite_1.0.0/specification/LANGUAGE_SPECIFICATION.md`.

Remaining gate: A complete versioned profile parser, semantic inference and target/runtime conformance are needed before native admission.

### BASE-17 Medium priority

Nested packaging, raw modeled labels and historical copies need explicit current provenance and reuse boundaries.

Status: **APPLIED**. Expanded materialized payload; source and updated manifests; change ledger; dataset-bound qualification; individual audit and fabric role.

Evidence: `audit/source_manifest.json | audit/updated_manifest.json | audit/dataset_qualification.json`.

Remaining gate: Metadata header is not an extra program; prove actual transport failure behavior.

## Contribution to the new fabric language

Profile owner: `ja.service`. Typed messages, protocol states, deadlines, retries and idempotency. Metadata header is not an extra program; prove actual transport failure behavior.

The [adapter contract](audit/fabric_adapter_contract.json) is a proposed interface with executable_adapter_implemented=false. It preserves source authority rather than using a feature label as inferred semantics. See [the collection architecture](../../fabric_language/ARCHITECTURE.md) and the [8S foundation](../../fabric_language/profiles/coupling8s/PROFILE.md).

## Qualification and verification

Use [dataset qualifications](audit/dataset_qualification.json) before training, importing or treating a record as evidence. A modeled pass or a structural validator pass is not native execution, authenticated federation, race proof, or physical device evidence. Current JA and DeepML technical records carry additional qualifications; deliberate negative examples remain negative examples.

The release provides an offline integrity checker: run `python tools/verify_release.py --deep` from the collection root. Per-profile test reports and validators qualify the exact behavior they checked. Complete grammars, native adapters, authenticated transports and a bootable unikernel remain separately tracked implementation gates.
