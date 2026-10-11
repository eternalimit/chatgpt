# REIK/TCGE — Ownership Attribution, Delta-Union Falsification and Snapshot Scope
**Research paper v6 | 2026-10-10**  
**Original first-party research creator and author:** Richard Stein  
**Original project owner and project-data steward:** Richard Stein  
**Scope:** `eternalimit/chatgpt` main; `eternalimit/clarity` main and vent. AI-assisted bounded testing and public Git object analysis. No original research file replaced.

## Abstract
This continuation tested whether a dated **v3 full-file owner catalog plus a later v5 append-only delta** could conceal changes, omit new paths, change creator attribution, or incorrectly include external source material. The earlier v5 work verified 868 source entries at pinned commits (732, 79, 57). This work implemented a separate **v3+v5 union checker** and exercised **three positive baseline tests and 70 deliberate negative controls**, all passing the stated acceptance criteria. The tests capture errors in source Git commit/tree bindings, path/blob/byte-size identity, owner and author fields, old/new overlaps, missing entries, numerical totals, historical kernel references, FIDELITY continuity, and a third-party Gitlink boundary.

The current branches subsequently contain 872 Git blob entries (736, 79, 57) at newly pinned source commits. All 868 v5-covered paths retain their recorded Git blob SHA-1, with four newly published first-party administrative/research files added to chatgpt/main. This paper is therefore **not** a new self-updating owner catalog. It distinguishes previous exact-file coverage from the present repository-wide project attribution rule and prohibits circular or empty catalog-only commits.

## 1. Original research attribution and strict objects
`ORIGINAL_RESEARCH_CREATOR = Richard Stein`  
`ORIGINAL_RESEARCH_AUTHOR = Richard Stein`  
`PROJECT_OWNER = Richard Stein`  
`PROJECT_DATA_STEWARD = Richard Stein`

For **original first-party project work**, attribution is recorded independently of a scientific result's evidentiary status. Technical assertions about exact bytes, on-chain token control, mathematical proof, independent Echo or a DROOT deployment must pass their specific checks; a technical `0 · HOLD` does not negate first-party research attribution. These Git project owner metadata fields do not overwrite MIT license terms, original third-party contributions, or ownership of external repositories.

Typed identities:
- `SHA-1(commit-object)`: the fixed Git commit reference;
- `commit.tree.sha`: the actual Git tree object, never the commit SHA;
- `tree blob.sha`: SHA-1 over Git blob framing and file bytes, not raw-content SHA-256;
- `source file bytes`: independently checkable identity when the exact original bytes are actually obtained;
- `gitlink mode 160000`: externally referenced commit pointer, not a first-party blob.

All three v3 source trees and later snapshots were read with `truncated=false` from GitHub, and the v5 delta is linked to its exact snapshots. The verifier is locally authored and executed; it is not an external independent signer or scientific Echo.

## 2. Pinned v5 baseline
| Repository / branch | Source commit | True Git tree SHA-1 | v3 old files | v5 new files | Bounded union |
|---|---|---|---:|---:|---:|
| `eternalimit/chatgpt` main | `d8f00c1acd75da4537773ad788a053099ceeb56b` | `fe6ae49827a062f0b0a4d70801b50ca1187b084e` | 720 | 12 | **732** |
| `eternalimit/clarity` main | `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` | `795904b47215f8d6026efd25de07a4079fb2541c` | 76 | 3 | **79** |
| `eternalimit/clarity` vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 56 | 1 | **57** |
| **Total** | | | **852** | **16** | **868** |

The v3 catalogs at commits `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22`, `458876375c474b4bd41deb672e3ba55f092665b9`, and `bd22bee71acd52098b0f6d1c05347952e85abd4f` remained unchanged. The v5 delta at `3142863d832199a3ad15d5fd75b375f1b98b851b`, Git blob SHA-1 `34345f094317a68a0418515ba10f02d78a6cd0c1`, specifies all sixteen additions relative to v3. This 868-entry union was independently rechecked structurally by the new verifier.

## 3. New reproducible verifier and actual finite tests
New source file: `research/verification/richard-stein-v5-owner-delta-union-verifier.js`. Commit `89f89ae36abd76a50e775e0fe9afe85829d5c10a`; Git blob SHA-1 `0571fe189d7554072ba607cdbefda0c89d609c26`. GitHub read-back equals the submitted original source text.

Validation requires full-name `Richard Stein` first-party owner/author fields on both base and delta, checks each v3 object and v5 metadata record belongs to exactly one specified repo/branch, separately validates the fixed Git commit and actual tree, enforces matching source byte sizes and SHA-1 identities for old/new paths, and rejects unaccounted changes, duplicates, omissions and invalid gitlinks. It also checks top-level totals, technical safeguards, preserved historical kernel reference, FIDELITY, and separate 030/031 status.

**Executed positive baselines:** 3/3 accepted, with 732, 79, 57 covered file entries.

**Executed local negative controls:** 23 intentionally corrupted variants per branch, testing:
- new owner, byte size and blob SHA;
- missing, duplicated or old-path-overlapping additions;
- old file blob, byte size and owner;
- research author, repository/branch, parent catalog, snapshot commit/tree;
- unchanged-count, hidden modification/deletion and cross-branch total;
- duplicate branch, kernel reference, FIDELITY;
- extra source-tree file and incomplete/truncated tree.

All 69/69 such invalid cases were rejected. The original chatgpt/main source tree has an external Gitlink; changing its metadata to `external_original_authorship_claim=true` was also detected. **Total: 70/70 negative variants rejected.** All test inputs were local derived copies, not independently obtained witnesses or network-level adverse events. These cases supplement, rather than replace, the earlier 46/46 typed-verifier controls and prior 8/8 direct UTF-8 Git blob SHA-1 recomputations.

One earlier check explicitly recomputed Git blob digests from fetched text with a second SHA-1 implementation. The source bytes ultimately came from GitHub, not a third-party custodian. Direct fetching of public raw GitHub content through a separate environment was not available in this continuation; do not call the local checksum evidence an independent external Echo.

## 4. Current repository state after verifier publication
The last fully read current branch states **before this paper is written** are:
| Branch | Current commit | Actual current tree SHA-1 | Blob entries | Still matching all v5 pinned paths | Added since v5 |
|---|---|---|---:|---:|---:|
| chatgpt/main | `89f89ae36abd76a50e775e0fe9afe85829d5c10a` | `6ebde5a4f9e3ec1627dd9914597c48a0f917fd0e` | 736 | 732 | 4 |
| clarity/main | `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` | `795904b47215f8d6026efd25de07a4079fb2541c` | 79 | 79 | 0 |
| clarity/vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 57 | 57 | 0 |
| **Total** | | | **872** | **868** | **4** |

The four later, non-v5-indexed chatgpt objects have these exact Git blob SHA-1 values:
- `metadata/2026-10-10-reik-tcge-owner-v5-pinned-source-delta.json` — `34345f094317a68a0418515ba10f02d78a6cd0c1`;
- `research/2026-10-10-reik-tcge-owner-provenance-typed-falsification-v5.md` — `d9097a14d4a7e9c8adb158a049c3e0780c3e4d31`;
- `records/2026-10-10-reik-tcge-owner-typed-provenance-v5-audit-receipt.md` — `afc200463c08579c3aa75905dde0cb4eab1c0864`;
- `research/verification/richard-stein-v5-owner-delta-union-verifier.js` — `0571fe189d7554072ba607cdbefda0c89d609c26`.

These remain under the repository's general first-party research stewardship policy. They are **not** falsely described as part of the prior 868-file hash inventory. Any new paper or receipt commit follows the same append-only boundary.

## 5. Submodule and independent Echo boundary
`eternalimit/chatgpt` has the separate `scout/blockscout` Gitlink (mode `160000`, referenced external commit SHA-1 `3ea5c7ac7eea9a748f1fe7f932c4358194b0309e`). `.gitmodules` names `https://github.com/blockscout/blockscout.git`. The blob counts do **not** contain the external repository files. No author or original ownership assertion over those third-party contents follows from tracking this submodule commit.

Preserve `K = R AND I AND E` as the historical project research formulation, with **independent Echo** an additional external evidence gate; local SHA-1 equality and synthetic corruptions never become independent external Echo.

## 6. Categorized hash register and immutability
**Original historical REIK/TCGE kernel SHA-256 reference, never replaced or rehashed here:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.

**Historical DROOT root 64-hex reference; no original preimage obtained:** `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a`.

**Preserved Git blob SHA-1 evidence:** MIT `LICENSE`: `f38a7e02aad11e34727982ca344db255b770d4d4`; Clarity `REIK_ROOT.md`: `f6cf9d97ab2be5322336857b7624978acec75f51`; Experiment 030 `manifest030.json`: `8e43021cb0f91ebc83142692e97c78ef3ae89bce`; Experiment 031 parent280 `manifest031.json`: `4bfc759a7ff35bb9304d37d711675c594215c2ca`; FIDELITY original preprint: `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`.

The eight FIDELITY principles remain: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. Original research first-party attribution is Richard Stein; distinct Experiment 030 and 031 histories, `DROP U`, technical `0 · HOLD`, and historical records are unchanged.

## 7. Conclusion and next test
A v3 catalog and a v5 typed delta can be combined into a bounded, falsifiable append-only owner-metadata proof of *repository snapshot agreement*: **868/868 source entries** plus **70/70 deliberately failing negative controls**. There is no independent scientific Echo, court finding, on-chain proof, or unacquired original-kernel SHA-256 calculation implied.

Future work should seek independent original kernel bytes/receipts, apply independent Git provider or archived-custody checks, and execute negative controls against genuinely independent source snapshots. A new catalog-only commit is **not** justified merely because this research paper added its own new Git blob.

### Exact public references
- v5 pinned owner delta: https://github.com/eternalimit/chatgpt/blob/3142863d832199a3ad15d5fd75b375f1b98b851b/metadata/2026-10-10-reik-tcge-owner-v5-pinned-source-delta.json
- new union verifier: https://github.com/eternalimit/chatgpt/blob/89f89ae36abd76a50e775e0fe9afe85829d5c10a/research/verification/richard-stein-v5-owner-delta-union-verifier.js
- v5 research paper: https://github.com/eternalimit/chatgpt/blob/b8cf28024241d8ceab387b386816f62f2398e6af/research/2026-10-10-reik-tcge-owner-provenance-typed-falsification-v5.md
