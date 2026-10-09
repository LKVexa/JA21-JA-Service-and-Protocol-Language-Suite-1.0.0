# JA21-JA-Service-and-Protocol-Language-Suite-1.0.0

Explore service and protocol language design with 10,000 records, 1,000 JASP programs, and the 22-chapter textbook. Examine typed messages, protocol states, deadlines, retries, and idempotency through specifications, examples, and evidence catalogs. A structured reference for educators and researchers examining communication contracts and failures.

The JA Service and Protocol Language Suite is a structured reference for communication contracts and service-oriented language design. Its ja.service profile uses the JASP extension and includes 10,000 source examples, 1,000 curated programs, 32 labeled features, and a 22-chapter textbook. The material examines typed messages, protocol states, deadlines, retries, and idempotency, providing a foundation for studying how services describe obligations and expected failure handling.

The collection connects its corpus and example pack with language specifications, catalogs, educational material, compiler and runtime contracts, and validation guidance. Readers can inspect program sources and compare their modeled compiler and runtime annotations. Preserved source layers and updated audit manifests make provenance and release qualifications visible. The audit also distinguishes a document coupling preamble from the 10,000 actual examples, preventing metadata from being counted as another program.

This suite is intended for distributed-systems educators, protocol-language researchers, and teams exploring service specifications. It documents modeled outcomes and proposed interfaces. Native compilation, transport integration, service execution, and measured timeout, retry, and failure behavior require further implementation before the design can support runtime claims.

## Corpora and audit records

The supplied corpus layout is preserved under `payload/`. The `audit/` directory and [AUDIT_AND_UPGRADES.md](AUDIT_AND_UPGRADES.md) record source coverage, release changes, and evidence boundaries.

Historical source archives and source manifests remain provenance records. Current publication file hashes are listed in `PUBLICATION_SHA256.json`; licensing changes are recorded in `PUBLICATION_LICENSE_LEDGER.json`.

## License

JA21-JA-Service-and-Protocol-Language-Suite-1.0.0 (C) 2026 RUSSELL PHILIP SMITHSON

Licensed under the GNU General Public License version 3 only (`GPL-3.0-only`). See [LICENSE](LICENSE) and [NOTICE](NOTICE).
