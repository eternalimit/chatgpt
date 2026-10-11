# Verified Audit Receipt — Richard Stein REIK/TCGE Owner-Attribution Delta v4

**Date:** 2026-10-10  
**Named original research creator, author and original project/data owner:** Richard Stein  
**Repo scope:** `eternalimit/chatgpt` main, `eternalimit/clarity` main and `eternalimit/clarity` vent.  
**Receipt status:** PASS for complete finite **858-entry fixed-source union coverage**, three positive verifier tests, and **27 negative controls**. Not an external legal-title, signer, blockchain or scientific attestation.

## 1. Evidence parents
- V3 chatgpt catalog commit `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22`; Git blob SHA-1 `cf46eca94550ab850c5e9186ad460ea74b6be134`; 720 entries.
- V3 clarity main catalog commit `458876375c474b4bd41deb672e3ba55f092665b9`; Git blob SHA-1 `2dfac44c0fb0069690fd6a3da9190910802f9e12`; 76 entries.
- V3 clarity vent catalog commit `bd22bee71acd52098b0f6d1c05347952e85abd4f`; Git blob SHA-1 `9329c8ba924a73149bf5579e36803f2934959763`; 56 entries.
- Previous research paper commit `aa00e6b7d0813ec936e17e5f82f643caa4fe1bb9`; Git blob SHA-1 `bbaab49859583285c7ccce429046dd61d76169dd`.
- Previous audit receipt commit `d0c94fcbf5a75a5d399a702e3d2dac20e3605e96`; Git blob SHA-1 `e38ff90de53403510d1daaa38df4a2d6b75eab63`.

## 2. Full fixed-source comparison
| Repo / branch | Pinned current source commit | Actual source tree Git SHA-1 | v3 unchanged | Delta additions | Union verified |
|---|---|---|---:|---:|---:|
| chatgpt/main | `7f45d018165a856fbd8ef0b1a11ef4f64f151dd8` | `6755754ae66bf8dcb8e95d8be7e5966b00f552eb` | 720 | 4 | 724 |
| clarity/main | `458876375c474b4bd41deb672e3ba55f092665b9` | `07eb3dd312e0567d1972de68117ba73b542fc821` | 76 | 1 | 77 |
| clarity/vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 56 | 1 | 57 |
| **Total** | | | **852** | **6** | **858** |

Each source tree was resolved from a real Git commit object, fetched by its actual tree SHA and fully enumerated with `truncated=false`. The union of historical v3 `(path, Git blob SHA-1, owner)` entries and six new delta entries equals the complete pinned source tree. **No changed or deleted paths.** These are branch-local entries, not necessarily unique source works.

## 3. New public-safe published artifacts
1. **Executable verifier:** `research/verification/richard-stein-owner-catalog-v3-verifier.js`. Commit `7f45d018165a856fbd8ef0b1a11ef4f64f151dd8`; Git blob SHA-1 `f13f962b9458c3d629ec0f917f847640ecb82a19`. Exact code readback PASS.
2. **Cross-branch owner-attribution delta:** `metadata/2026-10-10-richard-stein-owner-v3-current-snapshot-delta.json`. Commit `bb0f29e23012dce7ca76b3798769f45dff5a9aba`; Git blob SHA-1 `9f0aebd6c9f30a72d0f8a7ee175a4ca9f05735dd`. Exact text/JSON readback PASS; six new file additions, zero modified and deleted.
3. **Research paper v4:** `research/2026-10-10-owner-attribution-snapshot-delta-and-falsification-v4.md`. Commit `2bc1c7439452b075720361a37acb77efdc5951b9`; Git blob SHA-1 `e5445271b898548e19a7cbb953bcbebdb2d8b3d4`. Exact paper content readback PASS.

## 4. Falsification outcomes — actual bounded runs
Tests executed on each of three original v3 catalog, commit and source-tree triples:
- Positive unaltered catalogs accepted: **3/3**, 720/720, 76/76, 56/56.
- Intentionally invalid data rejected for each branch: wrong owner; mismatched blob; omitted file; duplicate file; wrong tree; wrong commit; truncated tree; extra unindexed file; wrong count. **9 × 3 = 27/27 rejections.**
- All negative variants were synthetic local inputs derived from the read-only source copies. They are not independent witnesses, outside attestations, chain proofs, or evidence of a real-world asset transaction.

## 5. Hash structure and immutability
**Historical original kernel SHA-256:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` (preserved **as historical reference**, original bytes not rehashed).
**Historical DROOT root hash reference:** `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a` (source preimage/link to original 12,357-byte WIN object not produced).
**Original source MIT LICENSE Git blob SHA-1:** `f38a7e02aad11e34727982ca344db255b770d4d4`.
**Clarity REIK_ROOT.md Git blob SHA-1:** `f6cf9d97ab2be5322336857b7624978acec75f51`.
**Experiment 030 manifest Git blob SHA-1:** `8e43021cb0f91ebc83142692e97c78ef3ae89bce`.
**Experiment 031-parent280 manifest Git blob SHA-1:** `4bfc759a7ff35bb9304d37d711675c594215c2ca`.
**FIDELITY preprint Git blob SHA-1:** `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`.

No source/receipt/license/history overwrite; no main/vent merge; no external signing, mint, transfer, or user-private material release. All eight FIDELITY principles preserved: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. Independent Echo is still a separate evidence gate. `DROP U`, `0 · HOLD` are restricted to unresolved **technical** propositions.

## 6. Bounded result and next action
**PASS 858/858 at exactly the three pinned source commits**, via v3+delta union. Publication of the new delta, v4 paper and this receipt necessarily creates additional tracked files **after** the bounded snapshot. Do not claim real-time self-reference or endlessly create empty commits simply to index each index file; next verification should advance when actual substantive changes or meaningful tests appear. The permanent project attribution rule remains Richard Stein for his original work. Indexing is distinct from asserting third-party authorship or legal title.
