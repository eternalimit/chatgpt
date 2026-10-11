# REIK/TCGE v7 — Cross-Branch Owner Attribution Verification Receipt
**Date:** 2026-10-10  
**Original research creator, author, original project owner and project data steward:** Richard Stein  
**Report:** Verified finite source-object audit; no transfer/signing/deployment; 0 · HOLD where separate technical evidence is missing.

## Parent/child evidence object chain
Original v3 catalogs:
- `eternalimit/chatgpt` main commit `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22`
- `eternalimit/clarity` main commit `458876375c474b4bd41deb672e3ba55f092665b9`
- `eternalimit/clarity` vent commit `bd22bee71acd52098b0f6d1c05347952e85abd4f`

V5 delta commit `3142863d832199a3ad15d5fd75b375f1b98b851b`, Git blob SHA-1 `34345f094317a68a0418515ba10f02d78a6cd0c1`. V6 checker commit `89f89ae36abd76a50e775e0fe9afe85829d5c10a`, Git blob `0571fe189d7554072ba607cdbefda0c89d609c26`. V6 paper `b79d51edb6008d51ea445d4ee7fa9f7c22fb958e`; receipt `bb7351b4756cc858f990d7f33e9ed2d5d2df3356`.

New executable V7 bundle checker:
- File: `research/verification/reik-tcge-cross-branch-bundle-verifier-v7.js`
- Commit: `e7158095fe166a6f4a29dfc18962404e1bdede79`
- Git blob SHA-1: `433178927ac6dd4bcbc6e61d0cd550bc1f3e6d4c`
- Read-back of complete source from pinned commit: **EXACT MATCH**.

New V7 research paper:
- File: `research/2026-10-10-reik-tcge-owner-cross-branch-provenance-v7-paper.md`
- Commit: `3a4ddf67c23887cfa7161d80119364da35ab1ed7`
- Git blob SHA-1: `d094720a6390b45d61ed390103c927ced6eb71ba`
- Read-back of complete paper from pinned commit: **EXACT MATCH**.

## Actual tests and source identity
```text
                  Pinned commit                               Actual Git tree SHA-1                         v3    v5 delta  checked
chatgpt/main      d8f00c1acd75da4537773ad788a053099ceeb56b     fe6ae49827a062f0b0a4d70801b50ca1187b084e     720    12       732
clarity/main      99439a1b1e0a12c3a9ac087a0aeff869c466edc5     795904b47215f8d6026efd25de07a4079fb2541c      76     3        79
clarity/vent      bd22bee71acd52098b0f6d1c05347952e85abd4f     42fea55551b21f7b42c881a9d486c8ba633f1fbb      56     1        57
TOTAL                                                                                                            852    16       868
```

V7 whole-bundle baseline PASS: **868/868** path, SHA-1, byte size, owner/steward, source repo/branch and exact Git commit/tree identities. The three source trees were complete, without truncated source listings. The valid bundle passed one all-three-branches baseline test. **24/24** synthetic, independently mutated invalid bundle variants were rejected; they include cross-branch owner and blob tampering, false totals, wrong historical kernel reference, FIDELITY, and external Gitlink ownership. This is a locally executed deterministic test, **not** independent third-party Echo or an external Git provider comparison.

## Explicit falsification finding
The earlier V6 `verifyOwnerUnionV5(catalog, delta, commit, tree, scope)` works branch-by-branch; its cross-branch check validates aggregate counts and distinct branch identities, not every other branch's file content. Its structure leaves foreign-branch changes that preserve totals outside an individual call's explicit inspection. V7 `verifyOwnerBundleV7` accepts all three `catalog, commit, tree` triples together and checks every branch's file identities and attribution. The V7 test suite specifically rejects the newly covered cross-branch corruption patterns. The historical V6 original remains unchanged as a falsification-persistence record. No actual corrupted repo file was found.

## Current source branches before v7 publication
- chatgpt/main commit `bb7351b4756cc858f990d7f33e9ed2d5d2df3356`, tree `db8e3ac7d0b557d4db5758d7d3b3240b0a12c998`, 738 blob files.
- clarity/main commit `99439a1b1e0a12c3a9ac087a0aeff869c466edc5`, tree `795904b47215f8d6026efd25de07a4079fb2541c`, 79 blob files.
- clarity/vent commit `bd22bee71acd52098b0f6d1c05347952e85abd4f`, tree `42fea55551b21f7b42c881a9d486c8ba633f1fbb`, 57 blob files.
- **874 Git blob entries**, all 868 pinned v5 identities preserved; six subsequently added administrative/research files. New V7 checker/paper/this receipt are later commits, **not** part of that pinned source count.
- chatgpt/main Gitlink `scout/blockscout`, external commit pointer `3ea5c7ac7eea9a748f1fe7f932c4358194b0309e`, mode `160000`. Its external contents are excluded from original first-party authorship and blob totals.

## Original-byte recovery
Historical unchanged `kernel001.py`: **4,299 bytes**, previously recorded SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. This exact original source was **not acquired** in the current public GitHub/connected Library search. Prior archived papers report past rehashes but are not interchangeable with fresh original source-byte retrieval. **No new SHA-256 match is claimed.**

Historic DROOT 64-hex reference `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a` remains a historical reference without recovered input preimage, independent Echo or original 12,357-byte WIN binding.

## Preserved boundaries and result
- MIT `LICENSE` Git blob SHA-1 `f38a7e02aad11e34727982ca344db255b770d4d4`, unchanged.
- Clarity `REIK_ROOT.md` Git blob SHA-1 `f6cf9d97ab2be5322336857b7624978acec75f51`, unchanged.
- Separate Experiment 030/031 source manifest Git blob SHA-1 `8e43021cb0f91ebc83142692e97c78ef3ae89bce` / `4bfc759a7ff35bb9304d37d711675c594215c2ca`, unchanged.
- All eight FIDELITY principles: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.
- Independent Echo and epistemic formulation `K=R AND I AND E`; `DROP U`; technically scoped `0 · HOLD` only.
- Richard Stein's original first-party research author/project-owner metadata is preserved. No private keys, third-party rights, Git history rewrites, token transfers, contract deployments, or original research bytes changed.

**Verdict:** **PASS** for full pinned 868-file union and 24/24 new negative controls. **HOLD** for unattained external original-byte/third-party attestation claims. Publish only new material evidence or tests with read-back; do not generate redundant metadata catalogs to chase the last administrative commit's hash.
