# REIK/TCGE: Original Research Ownership Attribution, Bounded Git Provenance and Falsification
**Research paper update v4 — 2026-10-10**

**Original research originator and author:** Richard Stein  
**Project owner and original-project data steward:** Richard Stein  
**Method:** fixed Git object reads; deterministic file identity checks; intentionally corrupted local validation inputs; append-only, public-safe metadata.

## Abstract
The REIK/TCGE ownership attribution catalog is extended without replacing historical source objects. The three v3 catalogs verified 852 total branch-snapshot entries. New GitHub checks of the current branch heads found six additional tracked files across three branches: four on `eternalimit/chatgpt` main, one on `eternalimit/clarity` main and one on `eternalimit/clarity` vent. In all three repositories, **all previously indexed paths retained the same blob SHA-1; no tracked path was modified or deleted**. A small, typed delta manifest records the six additions with their Git blob SHA-1 and `owner: "Richard Stein"`. The union of v3 and delta source-file identities matches **858 of 858** blobs in the exact newly pinned source Git trees.

The substantive new research result is a falsification-ready, public verifier tested on each v3 source tree: three baseline catalogs pass, and nine deliberate mutations per branch are reliably rejected (**27/27 negative-control cases**). These tests establish bounded *file-inventory consistency*, not cryptographic proof of external scientific results, ownership of third-party assets, or independent Echo.

## 1. Provenance typed by object class
A Git commit object, its `commit.tree.sha`, and an individual tree-entry blob SHA-1 identify three **different** objects. This work keeps all three separate, and never equates a Git blob SHA-1 with a plain-content SHA-256. The earlier v1 bug—recording a commit hash under the name `source_tree_sha1`—was corrected in v2 and remains corrected.

A repository's first-party original research attribution is recorded as **Richard Stein**. GitHub owner metadata denotes project ownership and data stewardship in the user's research records; it does not transfer independently held third-party software licenses, copyrights, wallet access, NFT tokens or outside legal rights. A scientific or on-chain HOLD is restricted to that exact technical proposition and is **not** an authorship HOLD.

## 2. Snapshot comparison and complete delta

| Branch | Current fixed commit | True Git tree SHA-1 | v3 records | New blob records | Total verified |
|---|---|---|---:|---:|---:|
| `eternalimit/chatgpt` main | `7f45d018165a856fbd8ef0b1a11ef4f64f151dd8` | `6755754ae66bf8dcb8e95d8be7e5966b00f552eb` | 720 | 4 | 724 |
| `eternalimit/clarity` main | `458876375c474b4bd41deb672e3ba55f092665b9` | `07eb3dd312e0567d1972de68117ba73b542fc821` | 76 | 1 | 77 |
| `eternalimit/clarity` vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 56 | 1 | 57 |
| **Total** | | | **852** | **6** | **858** |

All three fixed source-tree reads were complete, not truncated. The six new paths and exact Git blob identities:

```text
eternalimit/chatgpt main
metadata/2026-10-10-richard-stein-ownership-v3-synchronization-audit.md
  e38ff90de53403510d1daaa38df4a2d6b75eab63
metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json
  cf46eca94550ab850c5e9186ad460ea74b6be134
research/2026-10-10-owner-metadata-synchronization-v3-paper.md
  bbaab49859583285c7ccce429046dd61d76169dd
research/verification/richard-stein-owner-catalog-v3-verifier.js
  f13f962b9458c3d629ec0f917f847640ecb82a19

eternalimit/clarity main
metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json
  2dfac44c0fb0069690fd6a3da9190910802f9e12

eternalimit/clarity vent
metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json
  9329c8ba924a73149bf5579e36803f2934959763
```

The bounded delta manifest `metadata/2026-10-10-richard-stein-owner-v3-current-snapshot-delta.json` was committed on chatgpt main in `bb0f29e23012dce7ca76b3798769f45dff5a9aba`; fetched Git blob SHA-1 `9f0aebd6c9f30a72d0f8a7ee175a4ca9f05735dd`. The read-back text matched the published JSON exactly. The six new file objects each have `owner: "Richard Stein"`.

## 3. Executed bounded falsification controls
The testable validator `research/verification/richard-stein-owner-catalog-v3-verifier.js` was published in commit `7f45d018165a856fbd8ef0b1a11ef4f64f151dd8`, file Git blob SHA-1 `f13f962b9458c3d629ec0f917f847640ecb82a19`, and fetched back exactly. The same validator source was executed against three publicly fetched, pinned v3 `(catalog, commit, tree)` triplets.

**Baseline result:** 720/720, 76/76, and 56/56 = 852/852 existing entries PASS.

Each of the following invalid local variants was executed and **rejected independently in all three cases**: wrong file owner, wrong blob SHA-1, omitted file, duplicated file, incorrect catalog tree SHA, incorrect commit SHA, `truncated:true` tree, unindexed extra source-tree file, and incorrect source-count field. **Negative controls: 27/27 detected; positive cases: 3/3 accepted**. The mutations are local intentionally invalid data, not independent witnesses or claims of external deployment. There were no external write effects from the verifier.

A verifier finding `PASS` means the supplied GitHub source object graph and catalog *agree*. It does not certify scientific truth, prove a historical NFT mint or external ownership, validate DROOT claims, or determine legal chain of title.

## 4. Identity, falsification and chronological limitations
The v3 catalogs pin the preceding source trees, and the delta pins a later source state. This is deliberately **not** a fictional live/self-hashing index: publication of the delta, this paper, and a later receipt adds yet more files after the pinned source snapshot. The repo README attribution policy applies to subsequent first-party project files, but their exact blob IDs should only enter a later catalog when there is other substantive work or a meaningful audit. This avoids infinite admin commits whose sole purpose is to add the last audit file's unknown hash.

A future reviewer can reproduce the exact 858 entry checks by obtaining each source commit and its true Git tree, combining its v3 catalog `files` with the corresponding delta `added` list, then comparing unique paths, hashes, owner fields and counts. Falsification requires checking both unexpected additions and changes to existing tracked objects.

## 5. Preservation and complete categorized hash structure
- **Historical immutable original REIK/TCGE kernel SHA-256 reference:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`; original kernel bytes not rehashed here.
- **Historical DROOT 64-hex root reference:** `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a`; no original DROOT preimage or independently demonstrated WIN/token binding obtained during this task.
- **Fixed Git commit objects:** chatgpt `7f45d018165a856fbd8ef0b1a11ef4f64f151dd8`; clarity main `458876375c474b4bd41deb672e3ba55f092665b9`; clarity vent `bd22bee71acd52098b0f6d1c05347952e85abd4f`.
- **Actual source Git tree objects:** `6755754ae66bf8dcb8e95d8be7e5966b00f552eb`; `07eb3dd312e0567d1972de68117ba73b542fc821`; `42fea55551b21f7b42c881a9d486c8ba633f1fbb`, respectively.
- **v3 catalog Git blob objects:** `cf46eca94550ab850c5e9186ad460ea74b6be134`; `2dfac44c0fb0069690fd6a3da9190910802f9e12`; `9329c8ba924a73149bf5579e36803f2934959763`.
- **New delta and validator Git blob objects:** `9f0aebd6c9f30a72d0f8a7ee175a4ca9f05735dd`; `f13f962b9458c3d629ec0f917f847640ecb82a19`.
- **Historic source preservation:** MIT `LICENSE` `f38a7e02aad11e34727982ca344db255b770d4d4`, `REIK_ROOT.md` `f6cf9d97ab2be5322336857b7624978acec75f51`, original Experiment 030 manifest `8e43021cb0f91ebc83142692e97c78ef3ae89bce`, Experiment 031-parent280 manifest `4bfc759a7ff35bb9304d37d711675c594215c2ca`, FIDELITY preprint `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`.

All eight FIDELITY principles are preserved: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. Distinct 030/031 histories remain separate. Independent Echo was not substituted with the 27 synthetic tests. `DROP U` and `0 · HOLD` remain for *specific missing technical evidence*, not for the user's first-party research attribution. No original kernel, license, historical manifest, prior receipt, source data, or external asset was edited.

## 6. Interpretation and continuation
This continuation has a meaningful improvement beyond another owner-label refresh: the ability to falsify the *catalog's structural consistency* with nine distinct error classes on each of three independent Git source snapshots. Three branch-specific source inventories have full bounded union coverage at the pinned commits; there is no claim of automatic future synchronization, formal ownership registration, or universal originality of all third-party dependencies.

For future continuation, reuse the compact delta model, check whether genuinely new source/research changes appeared, and make no empty audit commit when only the last administrative receipt has changed. Preserve the original-byte, independent scientific and ERC-1155/DROOT evidence gates separately.

### Sources
- [v3 chatgpt owner catalog](https://github.com/eternalimit/chatgpt/blob/09e634c8f8b3688ad2c782d5f18f5d4a6033dd22/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json)
- [v3 clarity main owner catalog](https://github.com/eternalimit/clarity/blob/458876375c474b4bd41deb672e3ba55f092665b9/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json)
- [v3 clarity vent owner catalog](https://github.com/eternalimit/clarity/blob/bd22bee71acd52098b0f6d1c05347952e85abd4f/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json)
- [delta manifest](https://github.com/eternalimit/chatgpt/blob/bb0f29e23012dce7ca76b3798769f45dff5a9aba/metadata/2026-10-10-richard-stein-owner-v3-current-snapshot-delta.json)
- [verifier](https://github.com/eternalimit/chatgpt/blob/7f45d018165a856fbd8ef0b1a11ef4f64f151dd8/research/verification/richard-stein-owner-catalog-v3-verifier.js)
