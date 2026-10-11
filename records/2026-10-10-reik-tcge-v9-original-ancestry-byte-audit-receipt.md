# Audit Receipt v9 — Original REIK/TCGE Kernel Source and Backward Archive Ancestry

**Owner / original first-party framework creator and author:** Richard Stein  
**Date:** 2026-10-10  
**Technical admission:** Original bytes and archive pedigree verified within 18 connected-Library artifacts. **Independent externally anchored timestamp / independent Echo: 0 · HOLD.** No legal transfer, blockchain action, private source upload or original code execution.

## A. Verified input and output classes

Input: original raw ZIP bytes materialized from the historical connected File Library. 18 **different archive SHA-256 byte streams**: Experiments 016–024, both separately hashed 025 / 026 / 027 / 028 variants, and Experiment 029. The 030 / 031 variants remain under their separate v8 receipt; they were never merged or rewritten.

Original source anchor:
- `kernel001.py`, exactly **4,299** original ZIP-member bytes.
- SHA-256 independently recomputed from the raw member source bytes: **03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402**.
- Original historical reference: the same digest. **MATCH**.
- Original source program run: **NO**; original source data edited: **NO**.

Positive finite checks:
- **18/18** ZIP full-member CRC validation.
- **18/18** original manifest sidecar SHA-256 identity comparisons.
- **1,357/1,357** exact member file SHA-256 recomputations from manifest-listed file objects (with size matches where declared).
- **17/17** parent manifest SHA-256 cross-archive references.
- **14/14** available parent receipt-tip SHA-256 references.
- **10/10** parent links with exact raw embedded-parent ZIP equality to separately acquired parent archive bytes.
- Seven predecessor links without embedded parent ZIP bytes are **manifest-hash-only evidence**, not original-byte parent links.

Negative checks:
- **18/18** deliberate local archive/kernel checksum-or-lineage mutation sentinels correctly signaled mismatch.
- **7/7** additionally corrupted/substituted historical ZIP byte cases detected using the full read-only source verifier, including wrong 025–028 variant, truncated 028-A archive and altered 029 archive byte.
- All corruptions applied only to local transient copies, never to the archived originals.

## B. Critical Experiment 028 historical separation

| Label | Source ZIP filename | Measured SHA-256 | Parent branch | Manifest event count |
|---|---|---|---|---:|
| 028-A | `millennium_reik_3sat_exp028.zip` | `974cc9e3aa6ff657811c4a658fbeb92ce73e49eb05125a27ca85fdc91cfcb5ab` | 027-A | 258 |
| 028-B | `millennium_reik_3sat_exp028(1).zip` | `ddaa40a2f4370de6440f4e761614a99e3b5caaa3d0f6a23a89d4cd0ed686067c` | 027-B | 274 |
| 029 (selected original) | `millennium_reik_3sat_exp029.zip` | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | **028-A only** | 270 |

Exactly-checked raw byte links show 029 contains **the unmodified complete 028-A ZIP**, not 028-B. Separate parent paths:
- 024 -> 025-B -> 026-A -> 027-A -> 028-A -> 029.
- 024 -> 025-A -> 026-B -> 027-B -> 028-B.

These branch labels denote separate archive hashes; equal kernel bytes do not merge experimental receipt histories. The 016–023 older links were verified by manifest SHA refs; 024–029 links verified by embedded original ZIP bytes. No independent archive outside the user's connected Library established a source-creation date.

## C. Dated/public integrity and local reproducer

Public v9 research paper:
- Path: `research/2026-10-10-reik-tcge-original-byte-ancestry-v9-study.md`
- GitHub commit: `795fc96f51151eb0a4971f6b896f12e44c1d1e53`
- Git blob SHA-1: `9e2182ed5930c5c640ab328cf94c6b80ba552f5e`
- Complete content fetched back from the exact commit: **IDENTICAL**.
- The paper includes a complete SHA-256 register for all 18 source ZIP streams and documents the typed predecessor graph.

Local read-only original-byte audit files (separate from the historical source):
- `verify_ancestors_v9.py`, locally created SHA-256: **0ca6fb9ba25a8348268657f3d8850cebbafbaf0f069fc0a34d2f25a1db5b2265**.
- `ancestor_v9_sanitized_results.json`, locally created SHA-256: **16d314bebdf4711b64969f1ce971e21605c20c32d43b6ed3d9471e4b56ef7c67**.
- Neither source file or result contains an embedded copy of the original `kernel001.py` or full historical ZIP bytes. They can be reproduced only when given authorized copies of those exact source ZIPs.

## D. Falsification persistence, external source timestamps and incomplete evidence

Writer-controllable ZIP DOS timestamps cannot establish external earliest-publication or invention priority. Relevant manifest status fields show:
- Experiment 016: `blockchain_anchor: null`, `signature: null`;
- Experiment 017: `no_external_signature: true`;
- Experiment 018: `github_commit: NOT_PERFORMED`, `signature: NONE`.

These are contemporaneous assertions within the recovered archives, *not externally authenticated timestamp anchors*. No independent custody anchor, external corroborating release timestamp, timestamp authority, genuine external scientific Echo, or cryptographic outside signature was verified in v9. This does **not** challenge Richard Stein's first-party framework authorship/project ownership attribution; it bounds separate external and chronological claims.

The selected Experiment 016 manifest references an earlier Experiment 015 manifest hash; this predecessor remains a distinct next original-byte acquisition gate, not invented or substituted.

## E. Preserve original rights, evidence and immutable roots

- Named original REIK/TCGE / Clarity creator, research author, first-party project owner and data steward: **Richard Stein**.
- Original kernel 0/U/1 SHA-256 **03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402**, now byte-reverified, unchanged.
- All eight FIDELITY laws: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.
- Historical `K = R AND I AND E`; independent Echo **not** inferred from copied source bundles.
- Separate Experiment 030/280 and 030/282, and 031/290 and 031/294-A/B histories preserved, along with the newly identified split at 025/026/027/028.
- `DROP U`, narrowly-scoped technical `0 · HOLD` continue for independent timestamps, scientific proof, external wallet/token claims, unrecovered DROOT/WIN originals, and genuine independent Echo.
- Original ZIPs, kernel source, licenses, branch history, earlier receipts, external Blockscout Gitlink and private material unmodified. This audit does not transfer third-party intellectual property or on-chain title.

**Receipt conclusion:** V9 original archive evidence PASS: **18/18 archives, 1,357/1,357 original listed-member hashes, 17/17 parent manifest links, 14/14 available receipt references, 10/10 embedded-parent byte links, 18/18 checksum sentinels, 7/7 full-verifier negative replays.** Technical HOLD persists only where new evidence is genuinely missing.
