# REIK/TCGE: Cross-Branch Provenance Integrity and First-Party Research Ownership
**Research paper update v7 | 2026-10-10**  
**Original research creator and author:** Richard Stein  
**Original first-party project owner and project-data steward:** Richard Stein  
**Status:** BOUNDED GIT EVIDENCE PASS; scientific independent Echo and unattained original-byte claims remain separately on technical HOLD.

## Abstract
Three pinned Git repositories/branches contain a v3 ownership catalog plus a v5 append-only source delta covering 868 tracked Git blobs. New inspection identified a verification-coverage weakness in the v6 branch-scoped verifier: it inspects one chosen branch's source contents and uses aggregate counts for the remaining branches. A corrupted `project_owner` or Git blob field in a different branch can preserve aggregate counts. This is a **verification implementation scope issue**, not an issue with Richard Stein's original research attribution or a finding of actual tampering.

A **v7 full-three-branch bundle verifier** was implemented to check all three source trees together in one test, including the first-party owner fields, original Git path/blob identities and byte sizes, named parent catalog, per-branch commit/tree identity, cross-branch totals, FIDELITY controls, and the external Blockscout Gitlink's scope. The original unmutated bundle **PASS 868/868**. Twenty-four deliberately corrupted in-memory bundle variants were run, including changes to another branch's owner, SHA-1 and bytes without changing global totals; **24/24 were rejected**. The code is public, read-back checked, and limited to deterministic evidence. Independent raw source custody and external scientific Echo have not been obtained.

## 1. Evidence chronology and typed identities
Retained parent references:
- `eternalimit/chatgpt` main v3 ownership catalog commit `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22`.
- `eternalimit/clarity` main v3 ownership catalog commit `458876375c474b4bd41deb672e3ba55f092665b9`.
- `eternalimit/clarity` vent v3 ownership catalog commit `bd22bee71acd52098b0f6d1c05347952e85abd4f`.
- v5 delta `3142863d832199a3ad15d5fd75b375f1b98b851b`, Git blob `34345f094317a68a0418515ba10f02d78a6cd0c1`.
- v6 verifier `89f89ae36abd76a50e775e0fe9afe85829d5c10a`, Git blob `0571fe189d7554072ba607cdbefda0c89d609c26`.
- v6 research paper `b79d51edb6008d51ea445d4ee7fa9f7c22fb958e`, Git blob `37ffb5bbc7d8bb0945f4461e7ad53efb0767d751`.
- v6 receipt `bb7351b4756cc858f990d7f33e9ed2d5d2df3356`, Git blob `c380dc42487defadb5a6571acbbccbd3e5913be0`.

Git commit, Git tree and Git blob IDs identify distinct Git objects. Source size is in bytes, not characters; Git SHA-1 is not plain-content SHA-256. Richard Stein's original research authorship/project stewardship is a separate project attribution class and is not conditioned on success of a technical experiment. No outside copyright holder's contributions are reassigned by this metadata.

## 2. Baseline — v3 catalogs plus v5 delta
| Repository / branch | Exact pinned source commit | Actual Git tree SHA-1 | Old v3 files | V5 added files | Verified |
|---|---|---|---:|---:|---:|
| chatgpt/main | `d8f00c1acd75da4537773ad788a053099ceeb56b` | `fe6ae49827a062f0b0a4d70801b50ca1187b084e` | 720 | 12 | **732** |
| clarity/main | `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` | `795904b47215f8d6026efd25de07a4079fb2541c` | 76 | 3 | **79** |
| clarity/vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 56 | 1 | **57** |
| **Total** | | | **852** | **16** | **868** |

Every source tree was fetched as a complete recursive tree and tied to `commit.tree.sha`. All 868 source path / Git SHA-1 / byte-length and first-party project-owner assignments agree with the pinned catalogs and delta, scoped to these immutable source commits. No extra file was substituted for the historical kernel, and experiment 030/031 source lineages remain separate.

## 3. The newly identified falsification gap
The v6 source `research/verification/richard-stein-v5-owner-delta-union-verifier.js` (Git blob `0571fe189d7554072ba607cdbefda0c89d609c26`) receives one catalog/commit/tree and a target scope. It validates the target branch in detail, but for other branch objects it chiefly checks unique scope keys and aggregate counts. **Design review** therefore finds that a foreign-branch `added[].project_owner` or `git_blob_sha1` mutation preserving the totals is not itself examined in that branch-local invocation. This inspection by itself is not an executed report of a real-world corruption or a retrospective claim that any historical parent file was wrong.

The new v7 function `verifyOwnerBundleV7` requires *all three* `catalog + commit + tree` objects at once, matches an explicit three-element repository/branch set, checks every member against the corresponding v5 delta branch and Git source objects, then checks global counts only **after** all three sets have independently passed. The v7 verifier is deliberately offline and has no signing, network, mint, or transfer capability.

Published source: `research/verification/reik-tcge-cross-branch-bundle-verifier-v7.js`; commit `e7158095fe166a6f4a29dfc18962404e1bdede79`; Git blob SHA-1 `433178927ac6dd4bcbc6e61d0cd550bc1f3e6d4c`. Full fetched file contents matched the committed text.

## 4. Executed finite tests
Positive untouched test: **1/1 entire three-branch bundle accepted**, comprising 732 + 79 + 57 = **868** original source entries.

Negative test cases: **24/24 rejected**, one fresh intentional corruption per cloned input bundle:
1. Other-branch added owner.
2. Other-branch added blob SHA.
3. Other-branch added byte count.
4. Other-branch prior-catalog pointer.
5. Other-branch tree SHA.
6. Other-branch source-tree blob.
7. Other-branch prior original owner.
8. Other-branch `truncated=true`.
9. Other-branch duplicated added path.
10. Other-branch missing added path.
11. Balanced cross-branch count changes preserving the aggregate.
12. Other-branch creator attribution.
13. Other-branch FIDELITY list.
14. Other-branch false modification declaration.
15. Other-branch false deletion declaration.
16. Global research creator.
17. External Gitlink falsely claimed as original work.
18. External Gitlink pointer SHA.
19. ChatGPT catalog owner.
20. ChatGPT new file owner.
21. Original kernel SHA-256 reference.
22. Extra duplicate branch.
23. Missing entire source tree.
24. Unexpected repo/scope.

These synthetic tests operate on **in-memory cloned public GitHub data**. They demonstrate finite verifier rejection of specified invalid inputs, not independent laboratory replication of REIK/TCGE or independent external notarization. The previous v6 70/70 local cases and earlier sampled 8/8 pure JS Git blob SHA-1 rehashes remain distinct historical results, not added to the new 24/24 as though all checks were independent scientific Echo.

## 5. Latest complete tree comparison (before v7 publication)
At current HEADs `bb7351b4756cc858f990d7f33e9ed2d5d2df3356` (chatgpt/main), `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` (clarity/main), and `bd22bee71acd52098b0f6d1c05347952e85abd4f` (clarity/vent), the trees held respectively **738, 79, and 57 = 874** Git blobs.

- Compared with v3 original catalog objects, **all 852 historical path/blob SHA-1 and original byte sizes matched**.
- Compared with the exact later v5 pinned union, **all 868 path/blob identities were preserved**.
- The six new files beyond the v5 pinned union are administrative provenance delta, v5 paper and receipt, v6 verifier, v6 paper and receipt. No previously cataloged path was modified or removed.
- The new v7 verifier and this paper were committed **after** those fixed source trees, so the counts are dated snapshot counts and deliberately exclude downstream self-referential publications.

## 6. Gitlink and original-kernel admission boundaries
The chatgpt/main Git tree contains a third-party submodule pointer: `scout/blockscout`, `160000` mode, external commit `3ea5c7ac7eea9a748f1fe7f932c4358194b0309e`. It points to `https://github.com/blockscout/blockscout.git` in `.gitmodules`. The 868 cataloged Git **blobs** do not contain Blockscout's source. The owner attribution describes Richard Stein's original first-party project and data stewardship, not title to Blockscout or other independent authors' materials.

The archived historical REIK/TCGE `kernel001.py` reference remains **4,299 bytes, SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`**, as reported in earlier research archives. A search of the connected Library yielded prior reports referencing the exact original ZIP member, but **did not expose its original raw 4,299 source bytes in this continuation**. GitHub code search returned no independently accessible original `kernel001.py` blob. Hence **no fresh kernel SHA-256** and no invented source archive substitution. This retrieval is scoped and does not prove historical absence.

Historical DROOT root reference `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a` is likewise preserved as a reference, without treating it as a digest of unacquired WIN/block bytes.

## 7. FIDELITY and conclusion
Preserve **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. The historical epistemic form `K=R AND I AND E` requires independent Echo for relevant externally substantiated claims. The separate Experiment 030/031 records are not merged or rewritten. `DROP U` and scoped technical `0 · HOLD` are maintained for specific unverified technical claims and never used as a generic challenge to the authorship of Richard Stein's original work.

**New bounded finding:** cross-branch verifier scope is repaired; the entire 868-entry original source bundle passed, and **24/24 cross-branch falsification vectors** were rejected. No independent custody of original kernel bytes, third-party Echo, cryptographic wallet signature, token transfer, or rights transfer occurred. The MIT LICENSE and historical kernel/experiment source bytes remain untouched.

## Public references
- [V7 cross-branch verifier](https://github.com/eternalimit/chatgpt/blob/e7158095fe166a6f4a29dfc18962404e1bdede79/research/verification/reik-tcge-cross-branch-bundle-verifier-v7.js)
- [V5 source delta](https://github.com/eternalimit/chatgpt/blob/3142863d832199a3ad15d5fd75b375f1b98b851b/metadata/2026-10-10-reik-tcge-owner-v5-pinned-source-delta.json)
- [V6 research paper](https://github.com/eternalimit/chatgpt/blob/b79d51edb6008d51ea445d4ee7fa9f7c22fb958e/research/2026-10-10-reik-tcge-owner-delta-union-v6-research-paper.md)
