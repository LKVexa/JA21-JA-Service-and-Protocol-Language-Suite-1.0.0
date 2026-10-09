# Technical Corpus Guide

## Purpose

The technical corpus is the complete 10,000-record research edition of the JA Service and Protocol Language source upload. It is designed for language engineering, compiler tests, runtime planning, teaching, conformance analysis, and deterministic evidence review.

## Master file

`JA21_JASP_TECHNICAL_CORPUS_10000.jsonl.gz` contains one document-level Smithson 8S Coupled Mechanics metadata record followed by 10,000 normalized language records. The twenty files under `shards/` contain 500 language records each and omit the document-level header.

## Record layers

Each language record contains:

1. source identity, level, validation class, and feature;
2. source-faithful `.jasp` text;
3. semantic interpretation and judgment;
4. typed AST identity and source span;
5. compiler representation and stable diagnostics;
6. R12 lowering evidence;
7. runtime plan and sandbox expectations;
8. MCRT provenance and determinism class;
9. technical explanation and optimization invariants;
10. publication track, source hash, and navigation fields added by this suite.

## Distribution

- Records: 10,000
- Features: 32
- Levels: 10, with 1,000 records each
- Validation classes: positive 4,000; negative 1,500; boundary 1,000; integration 1,000; security 750; performance 500; determinism 500; interoperability 250; recovery 250; certification 250

## Navigation

Use `TECHNICAL_CORPUS_INDEX.csv` for spreadsheet-style lookup, `TECHNICAL_CORPUS_SCHEMA.json` for machine validation, `catalogs/FEATURE_ATLAS.md` for conceptual browsing, and `tools/inspect_corpus.py` for an offline summary.

## Evidence boundary

The corpus describes expected compiler and runtime outcomes but was supplied without a native JA Service compiler or runtime. `modeled_not_executed` is retained wherever the source corpus uses it. Native implementations must produce independent results and receipts.

## Coupling mechanics

Smithson 8S Coupled Mechanics metadata is preserved as proposed generative and computational framing. The source qualification is retained: it is not represented as established physical law, standard `S^8` topology, or evidence of physical quantum entanglement.
