# Audit Receipt v6 — Richard Stein REIK/TCGE Ownership Attribution and Delta-Union Verification

**Date:** 2026-10-10  
**Original research author/creator:** Richard Stein  
**First-party project owner and project-data steward:** Richard Stein  
**Status:** PASS for 868/868 pinned v5 union entries, 3/3 positives and 70/70 deliberately invalid controls; other technical proof gates remain claim-specific HOLD.

## 1. Parent and public source identifiers
- Original v3 catalog commits: chatgpt/main `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22`; clarity/main `458876375c474b4bd41deb672e3ba55f092665b9`; clarity/vent `bd22bee71acd52098b0f6d1c05347952e85abd4f`.
- V5 append-only delta `metadata/2026-10-10-reik-tcge-owner-v5-pinned-source-delta.json` committed `3142863d832199a3ad15d5fd75b375f1b98b851b`; Git blob SHA-1 `34345f094317a68a0418515ba10f02d78a6cd0c1`.
- Prior v5 research paper `b8cf28024241d8ceab387b386816f62f2398e6af` and receipt `f2182239f457b44f20a2b9bf57ca7a386c59d0d6` fetched and checked for their source paths.
- New union verifier `research/verification/richard-stein-v5-owner-delta-union-verifier.js`: commit `89f89ae36abd76a50e775e0fe9afe85829d5c10a`; Git blob SHA-1 `0571fe189d7554072ba607cdbefda0c89d609c26`; published code exact GitHub read-back PASS.
- New v6 research paper `research/2026-10-10-reik-tcge-owner-delta-union-v6-research-paper.md`: commit `b79d51edb6008d51ea445d4ee7fa9f7c22fb958e`; Git blob SHA-1 `37ffb5bbc7d8bb0945f4461e7ad53efb0767d751`; exact GitHub read-back PASS.

## 2. Source objects and verification counts
| Branch | Fixed source commit | True Git tree SHA-1 | Catalog | Delta | Union |
|---|---|---|---:|---:|---:|
| chatgpt/main | `d8f00c1acd75da4537773ad788a053099ceeb56b` | `fe6ae49827a062f0b0a4d70801b50ca1187b084e` | 720 | 12 | **732** |
| clarity/main | `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` | `795904b47215f8d6026efd25de07a4079fb2541c` | 76 | 3 | **79** |
| clarity/vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 56 | 1 | **57** |
| **Total** | | | **852** | **16** | **868** |

The separate, user-originated first-party project owner/author attribution is `Richard Stein` in each old record and new delta. Every pinned file path, Git blob SHA-1 and original size matched the source tree under an explicitly typed commit/tree check; all three recursive trees were complete. Historical experimental/source blobs, the MIT LICENSE and the original Clarity REIK root remain unchanged.

## 3. New falsifiable tests, actually executed
**3 positive original baselines accepted:** source counts 732, 79, 57.

**23 negative controls × 3 branches = 69/69 invalid samples rejected:** wrong owner, file length or SHA in added and original entries; missing, repeated, overlapping or unaccounted files; changed author; wrong repository, branch, parent catalog, source commit and source tree; incorrect unchanged/aggregate counts; false no-change/deletion records; duplicated branch, changed historical kernel reference, missing FIDELITY principle, injected source file and truncated tree.

**External Gitlink negative control +1 = 70/70 detected:** the chatgpt source tree's `scout/blockscout` gitlink points to `3ea5c7ac7eea9a748f1fe7f932c4358194b0309e` with mode `160000`. Intentionally asserting `external_original_authorship_claim=true` was detected and rejected. The Gitlink does not include external submodule source files within the 868 Git blobs.

All corruptions were **in-memory local synthetic variants**. They are evidence of classifier acceptance/rejection behavior, *not* independently anchored cryptographic witnesses, factual owner/title adjudication, or scientific replication of the REIK/TCGE system. Prior pure-JavaScript raw Git blob SHA-1 source rehashes (8/8) remain separately cited historical results, not rerun externally here.

## 4. Current branch snapshot and chronological limits
After publishing the union verifier, the fixed current heads were:
- chatgpt/main `89f89ae36abd76a50e775e0fe9afe85829d5c10a`, true Git tree `6ebde5a4f9e3ec1627dd9914597c48a0f917fd0e`, 736 files.
- clarity/main `99439a1b1e0a12c3a9ac087a0aeff869c466edc5`, true tree `795904b47215f8d6026efd25de07a4079fb2541c`, 79 files.
- clarity/vent `bd22bee71acd52098b0f6d1c05347952e85abd4f`, true tree `42fea55551b21f7b42c881a9d486c8ba633f1fbb`, 57 files.

Total current snapshot: **872** Git blob entries; all 868 earlier v5-union entries unchanged. The four later chatgpt files are the v5 delta, paper, receipt and new union verifier; the 872 snapshot was pinned *before* publication of this v6 paper and audit receipt. Therefore later branch HEADs necessarily contain additional non-indexed new administrative files, not modifications to the 868 source entries. No self-referential full-catalog claim or empty audit-only commit to index its own digest.

## 5. Immutable hashes and separate evidence status
- Original historical immutable REIK/TCGE kernel SHA-256 reference: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Exact original kernel bytes were *not rehashed*.
- Original historical DROOT 64-hex root reference: `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a`. Not derived from new source bytes.
- Shared MIT LICENSE Git blob SHA-1: `f38a7e02aad11e34727982ca344db255b770d4d4`.
- Clarity REIK_ROOT.md Git blob SHA-1: `f6cf9d97ab2be5322336857b7624978acec75f51`.
- Experiment 030 manifest SHA-1 `8e43021cb0f91ebc83142692e97c78ef3ae89bce`; distinct Experiment 031 parent280 manifest SHA-1 `4bfc759a7ff35bb9304d37d711675c594215c2ca`.
- Original FIDELITY preprint Git blob SHA-1 `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`.

All eight FIDELITY principles preserved: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. The historical `K = R AND I AND E`, independent Echo, `DROP U`, distinct 030/031 histories and claim-specific technical `0 HOLD` are preserved. No kernel, LICENSE, signed/frozen original, private wallet asset or separate experiment data changed in this audit.

## 6. Next verification gate
For the next substantive continuation, compare *current HEAD* and the exact 868-source baseline, preserve Gitlink boundaries, and seek an **independent archived source/custodian** or actual original-byte objects if external SHA-256 and independent Echo are to advance. Do not infer external ownership or title from repository metadata; do not make redundant catalog-only commits. This receipt establishes only what the pinned GitHub objects and finite corrupted test vectors can support.
