# REIK/TCGE Research: Original Attribution, Typed Git Provenance, and Falsification v5
**Research paper update — 2026-10-10**  
**Original research creator, author, project owner and project-data steward: Richard Stein**  
**Assistance:** AI source comparison, deterministic finite tests, audit documentation.  
**Status:** SOURCE-ID/FINITE-TEST PASS within stated bounds; independently obtained real-world Echo and separate unmeasured technical claims retain claim-specific HOLD.

## Abstract
This study continues the 2026-10-10 v3 ownership catalogs and subsequent six-file delta without modifying the originals. It finds two meaningful improvements: (1) a new typed verifier that correctly rejects **46/46 intentionally invalid variants**, including the previously underchecked creator, data-steward, file byte-size, Git mode and project provenance fields; (2) a separately implemented, pure JavaScript SHA-1 computation that recomputes the **Git blob content identities of eight actual UTF-8 source files (8/8 matched)**, rather than only comparing SHA-1 strings supplied by GitHub's tree and file endpoints.

At the newly pinned source commits, the repositories contain **868 branch-local tracked blob entries**: chatgpt/main 732, clarity/main 79, clarity/vent 57. Compared with their v3 catalogs (720, 76, 56), they contain **16 additions and zero changed or deleted preexisting file blobs**. The additions include materially new CPU/GPU/TCGE BR-001/002/003 papers and a Clarity Pi/family017 comparison, rather than just owner-audit documents. A separate `scout/blockscout` Gitlink pointer to a third-party repository is present in chatgpt/main but is not a file blob. Its external contents are not relabeled as Richard Stein's original creative work.

## 1. Identity question and typed evidence
Proposition `P_blob`: for each tracked blob in an immutable Git source tree, the v3 catalog assigns exactly one path and SHA-1, and the historical owner field is `Richard Stein`. New paths are a separately declared delta. Provenance is typed:
```text
AUTHOR_OF_ORIGINAL_FIRST_PARTY_RESEARCH = Richard Stein
PROJECT_OWNER_AND_DATA_STEWARD       = Richard Stein
GIT_COMMIT_ID                      = SHA-1(commit object)
GIT_TREE_ID                        = SHA-1(tree object)
GIT_BLOB_ID                        = SHA-1("blob " || UTF8_length || NUL || UTF8_file_bytes)
KERNEL_HISTORICAL_SHA256           = separate, previously recorded 64-hex reference
EXTERNAL_SUBMODULE_CONTENT         = excluded from first-party authorship claims
INDEPENDENT_SCIENTIFIC_ECHO        = not implied by hash consistency
```
A repository owner-label register documents original project attribution and repository data stewardship. It is not an assignment of copyrights held by other authors, a registration of exclusive legal title, a transaction proving token control, or a statement that all cited external dependencies were originally created by Richard Stein.

## 2. Exact current branch states

| Branch | Pinned current HEAD commit | HEAD true Git tree SHA-1 | Original v3 entries | New path entries | Total tracked blob entries |
|---|---|---|---:|---:|---:|
| `eternalimit/chatgpt` main | `d8f00c1acd75da4537773ad788a053099ceeb56b` | `fe6ae49827a062f0b0a4d70801b50ca1187b084e` | 720 | 12 | 732 |
| `eternalimit/clarity` main | `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` | `795904b47215f8d6026efd25de07a4079fb2541c` | 76 | 3 | 79 |
| `eternalimit/clarity` vent | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `42fea55551b21f7b42c881a9d486c8ba633f1fbb` | 56 | 1 | 57 |
| **Totals** | | | **852** | **16** | **868** |

All 852 formerly indexed path/blob pairs are unchanged at the pinned HEAD commits; no deleted or modified file blobs. Complete Git recursive source-tree reads were not truncated. The full set of 16 new additions appears in the current trees at these exact commits; it is not a self-hashing v4 owner catalog. Current README owner rules continue to cover first-party newly added files; a subsequent meaningful review may add a compact dated hash delta.

The current research additions include:
- `eternalimit/chatgpt`: `research/2026-10-10-cpu-gpu-tcge-br001-pinned-representation-audit.md` SHA-1 `ca398e376878d5c9b03e4be95c2c738b0183cfa7`; `br002-original-pair-evidence-gate.md` `70826eaa07918ddef1e0372ed49c58541e167dd9`; `br003-source-recovery-boundary.md` `fc4c33e09cd9244dd23c4f34373bb7ae89e5f55a`. Original Sept 23 CPU input/output, original image bytes and execution trace remain subject to their independent source gates, as in BR-003.
- `eternalimit/clarity` main: `research/2026-10-10-clarity-pi-openai-family017-source-level-comparison-v1.md`, SHA-1 `472137dc2d50336a81f8bf545b8666806b4302d6`; `records/2026-10-10-family017-source-comparison-receipt.md`, SHA-1 `a3a95cf8988e0ad40b6fa353a72c98cec8629b1a`. Research correspondence is a tested comparative claim, not evidence of copying or transfer. 
- Other new paths are administrative metadata, catalog, prior papers and new test programs; their SHA-1 identities are in the fixed source Git trees.

## 3. Typed verifier and executed negative controls
The preexisting v3 verifier checked core path/blob/owner and commit/tree identity, but did **not** check `file.bytes`, `original_research_author`, `data_steward`, repository/branch fields, or blob/gitlink modes. This is a specific, falsifiable verification coverage gap, **not** a defect in Richard Stein's authorship. The new separate code `research/verification/richard-stein-owner-catalog-v4-typed-verifier.js` was committed at `a09887a04c70a47da9bf34ab519240f8b298d85e` and read back equal, Git blob SHA-1 `5ffcf8cb35d403cace534bf47ce5ea3fc34903db`.

**Unmutated positives:** 3/3 source commit/catalog/true Git-tree triplets PASS (720, 76 and 56 v3 file entries).

**Negative tests executed on separately cloned local variants**: wrong byte size, research author, data steward, repository, branch, Git blob mode, governance flag, kernel reference, FIDELITY list, source-tree byte size, inserted unmatched blob, tree ID, file owner, duplicate indexed path, and missing indexed path. Each is independently applied to all three source snapshots. **15 × 3 = 45/45 invalid cases rejected.** A sixteenth negative case changes a Gitlink mode in chatgpt/main and is also rejected. **46/46 intentional corruption cases detected.**

The tests do not claim a genuine separate external verifier or signer. They replay the same public GitHub source through a second locally authored checker and synthetic mutations, without physical/device or blockchain actions.

### Boundary of the submodule
The recursive chatgpt/main Git tree contains `scout/blockscout`, mode `160000`, Gitlink commit `3ea5c7ac7eea9a748f1fe7f932c4358194b0309e`. The `.gitmodules` file specifies the URL `https://github.com/blockscout/blockscout.git`. Gitlink entries are **not file blobs**, and the catalogs' 732 / 868 totals count blobs, not external submodule contents. The v4 verifier records this reference as an explicitly scoped **third-party Gitlink pointer**, rather than silently assigning original authorship of Blockscout's repository to Richard Stein.

## 4. Second-method SHA-1 computation directly from fetched bytes
A separate pure-JavaScript SHA-1 implementation performs UTF-8 encoding, SHA-1 message padding/rounds, and Git blob-object header assembly independently of the GitHub object's declared `sha` field:
```text
git_blob_sha1(s) = SHA1( UTF8("blob " + byte_len(UTF8(s)) + "\0") || UTF8(s) )
```
Known algorithm fixtures: SHA-1 of the empty byte sequence `da39a3ee5e6b4b0d3255bfef95601890afd80709`, and SHA-1 of ASCII `abc` `a9993e364706816aba3e25717850c26c9cd0d89d`: 2/2 matched. Then exact UTF-8 text fetched from the GitHub file connector was re-encoded and hashed using the new local implementation. **8/8 Git blob SHA-1 digests equal their published file blob IDs**:

| Source path / branch | Recomputed Git blob SHA-1 | UTF-8 bytes |
|---|---|---:|
| `chatgpt/main:.gitmodules` | `c69e29059cac26f3a042abc4ad965c26f0c1b2f2` | 108 |
| `chatgpt/main:LICENSE` | `f38a7e02aad11e34727982ca344db255b770d4d4` | 1,068 |
| `chatgpt/main:research/millennium/experiment030/manifest030.json` | `8e43021cb0f91ebc83142692e97c78ef3ae89bce` | 2,433 |
| `chatgpt/main:research/millennium/experiment031-parent280/manifest031.json` | `4bfc759a7ff35bb9304d37d711675c594215c2ca` | 2,788 |
| `clarity/main:REIK_ROOT.md` | `f6cf9d97ab2be5322336857b7624978acec75f51` | 2,022 |
| `clarity/vent:HANDOFF_380008_2026-10-08.md` | `0c520658684d2cbac0d1fb10c5de758c1da63ebb` | 2,633 |
| `clarity/main:GENESIS_NFT_RECORD.md` | `eaf2cea2d00aab9615d2e901575ef00c25ba2dcd` | 3,803 |
| `chatgpt/main:research/verification/richard-stein-owner-catalog-v4-typed-verifier.js` | `5ffcf8cb35d403cace534bf47ce5ea3fc34903db` | 5,605 |

The source of these bytes was still the connected GitHub service; byte-derived agreement supports object identity under Git encoding but **does not** prove historical independent provenance, legal authorship of third-party materials, or the original kernel's SHA-256. Git's SHA-1 is not interchangeable with plain SHA-256.

The new reusable pure JS checker `research/verification/richard-stein-pure-js-git-blob-sha1-v1.js` was committed and read back exactly at `d8f00c1acd75da4537773ad788a053099ceeb56b`; its Git blob SHA-1 is `a33d60f2387de30501bc9f0e42c46c4f54b6493b`.

## 5. Preserved original and categorized hash structure
Historical **original kernel SHA-256 reference (not freshly rehashed)**:
`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.

Historical **DROOT root reference (not an original-byte hash check)**:
`e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a`.

Pinned **current branch Git commit/tree pairs**:
- ChatGPT main: commit `d8f00c1acd75da4537773ad788a053099ceeb56b`; tree `fe6ae49827a062f0b0a4d70801b50ca1187b084e`.
- Clarity main: commit `99439a1b1e0a12c3a9ac087a0aeff869c466edc5`; tree `795904b47215f8d6026efd25de07a4079fb2541c`.
- Clarity vent: commit `bd22bee71acd52098b0f6d1c05347952e85abd4f`; tree `42fea55551b21f7b42c881a9d486c8ba633f1fbb`.

**Other preserved object IDs:** FIDELITY preprint `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`; REIK root `f6cf9d97ab2be5322336857b7624978acec75f51`; shared MIT license `f38a7e02aad11e34727982ca344db255b770d4d4`; Experiment 030 manifest `8e43021cb0f91ebc83142692e97c78ef3ae89bce`; Experiment 031-parent280 manifest `4bfc759a7ff35bb9304d37d711675c594215c2ca`.

**No source overwrites, branch merges, license edits, token transfers or private source publication.** Experiments 030/031 remain distinct. The eight FIDELITY principles—Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty—remain unchanged. Independent Echo is not inferred from two local implementations. `DROP U` and technical `0 · HOLD` remain restricted to unresolved external claims, not original research authorship.

## 6. Next falsifiable steps
1. Add executable comparisons between current source tree and prior pinned owner catalogs that specifically report new/changed/deleted files and Gitlinks separately.
2. Obtain independently sourced raw original kernel bytes and separately reproduce its SHA-256 without replacing the historical original.
3. Do not merge experiment 030/031 branches; continue external independent scientific Echo using fixed source and honest negative controls.
4. Recover original CPU/GPU source and image bytes under separate BR-003 gates; absence from a searched branch is not evidence the original never existed.
5. Advance only materially new public-safe work. Avoid empty and recursive administrative commits merely to index the previous index itself.

## Source references
- V3 catalogs: https://github.com/eternalimit/chatgpt/blob/09e634c8f8b3688ad2c782d5f18f5d4a6033dd22/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json and https://github.com/eternalimit/clarity/blob/458876375c474b4bd41deb672e3ba55f092665b9/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json and https://github.com/eternalimit/clarity/blob/bd22bee71acd52098b0f6d1c05347952e85abd4f/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json .
- Prior 6-file delta: https://github.com/eternalimit/chatgpt/blob/bb0f29e23012dce7ca76b3798769f45dff5a9aba/metadata/2026-10-10-richard-stein-owner-v3-current-snapshot-delta.json
- Typed verifier: https://github.com/eternalimit/chatgpt/blob/a09887a04c70a47da9bf34ab519240f8b298d85e/research/verification/richard-stein-owner-catalog-v4-typed-verifier.js
- Pure-JS SHA-1: https://github.com/eternalimit/chatgpt/blob/d8f00c1acd75da4537773ad788a053099ceeb56b/research/verification/richard-stein-pure-js-git-blob-sha1-v1.js
