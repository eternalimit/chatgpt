# REIK/TCGE — Original Research Attribution and Git Object-Correct Metadata Synchronization
**Working research paper v2, 2026-10-10**

**Research originator, author, and original project/data owner: Richard Stein.** AI assistance: GitHub source inspection, deterministic inventory comparison, JSON documentation and read-back. Project stewardship attribution is not a transfer of unrelated third-party copyrights, tokens, wallet control or legally restricted assets.

## Abstract
The earlier owner catalogs assigned `owner: "Richard Stein"` across 843 repository file entries drawn from three branch snapshots. This continuation re-enumerated each branch, compared exact Git object IDs to those catalogs, repaired a concrete metadata bug in the type of the snapshot identifier, and published three **v2 full-path owner catalogs**. Seven branch-local changes were found relative to the prior catalogs: four newly tracked catalog/audit files and three README blob updates; no files were deleted. The current pre-refresh snapshots contained 717, 75 and 55 tracked blobs (847 total entries), and the refreshed catalogs individually matched all 847 path–blob–owner triples against pinned true Git tree objects. The catalog files written in this continuation necessarily appear *after* their respective source snapshots. The project-wide owner convention covers them; updated exact Git object coverage requires a subsequent snapshot. These results verify repository file identity and owner attribution metadata within scope, not external ownership transfer or independent scientific claims.

## 1. Problem and identity model
For each source branch, identify the actual **commit object** `C` and the associated **Git tree object** `T = commit(C).tree.sha`. Recursively enumerate the immutable tree `T` and record for each tracked blob `(path, Git blob SHA-1, size, owner=Richard Stein)`. Compare against the earlier catalog.

Important correction: the **v1** catalogs used field `source_tree_sha1` with the branch **commit** identifier. A commit hash is not the Git tree hash, even though both are 40-character Git SHA-1 object identifiers. A direct GitHub `commits/{sha}` read and `git/trees/{actual-tree-sha}` read established the separate identifiers below. The **v2** catalogs use `source_commit_sha` and `source_tree_git_sha1`, independently typed.

GitHub `blob` SHA-1 identifies bytes under Git object encoding; it is not SHA-256 of file content, independent authorship attestation, a research result, or a cryptographic token signature. This typed distinction is consistent with the historical REIK/TCGE FIDELITY identity and method/object separation requirements.

## 2. Exact evidence snapshots

| Branch | Baseline commit for enumerated files | Actual Git tree SHA-1 | Files | V2 catalog commit | V2 catalog Git blob SHA-1 |
|---|---|---|---:|---|---|
| `eternalimit/chatgpt` `main` | `b18b17a1a33803a7cd74a064cae62c2e7a1371c2` | `2bdbb47bee2caa7eb82166c5be3d3f2fda96b04a` | 717 | `29241df8f564e23dbbe509047fed3991535c798e` | `29c81d97735f22f771c6db5d4b84d126214fee0e` |
| `eternalimit/clarity` `main` | `442fa3b3aa43174e1e3083f123cac7948b57f92d` | `75c501f9de71a7578fe317c23f66a538f95b08ff` | 75 | `20d1cec62de5a4066ac6cb9151598baacc7aefc8` | `a729d4a50635b93c2f4b79ed5b531e81bdaec0a7` |
| `eternalimit/clarity` `vent` | `1ef23773506641d1ad0bf3b371f58f76d2e7f6a0` | `19ef1dba5c17fd8846c686d42777bff2651e5ece` | 55 | `ee40281c61a574d0a136978d3be42fabb0a8d7e2` | `cbf1026a8d882b3d7f68128e0a90112e7930f84a` |

Total source snapshot file entries: **847/847 listed and read-back checked against the true immutable source Git tree**, including full `Richard Stein` owner assignment on each entry. Clarity main and vent share many common files; **847 is not the count of distinct creations**.

## 3. Change detection since v1

V1 baselines were published at:
- chatgpt main commit `68cbcb500e9b803b3e1625ec4dea8a5178d55677`, 715 files.
- clarity main commit `7b52a0a4cc10b6b0d6dba0d770da48baf13431bc`, 74 files.
- clarity vent commit `66e6fc7bc9f192abe27a18044341cbe000301d41`, 54 files.

Comparing the current frozen source snapshots against those precise original v1 JSON lists revealed **four newly tracked files and three changed README blobs, zero deletions**:

**ChatGPT main newly tracked**:
- `metadata/2026-10-10-richard-stein-all-data-owner-audit-receipt.md` Git blob `a6d38c127e1248043940a7d1cdaca4c3af6969c6`.
- `metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_2026-10-10.json` Git blob `4b28cff7b89c79f7890fa3e9354d1dc0a5a70dbd`.
- Modified `README.md` Git blob old `e6078321aed35518d64125fdeaabe5dcbdb4874a`, new `01d7ebec08859f0636eab141e1c6f3e9f8296847`.

**Clarity main newly tracked**:
- `metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_2026-10-10.json` Git blob `c96cf0d3a437eac215e69e54622bfc92c4e3cdbe`.
- Modified `README.md` Git blob old `7f440af33f29bebcb8c0be5de408682de4fcacd0`, new `e647ddf58cc031432b0f7fb3c2977dafced940da`.

**Clarity vent newly tracked**:
- `metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_2026-10-10.json` Git blob `d40ffd550d0077ec4c2bd86b60c1d4b15ae598f8`.
- Modified `README.md` old `7f440af33f29bebcb8c0be5de408682de4fcacd0`, new `e647ddf58cc031432b0f7fb3c2977dafced940da`.

Unchanged compared with the original catalogs: chatgpt 714 files, clarity main 73, clarity vent 53. Each v2 catalog enumerates its updated README bytes alongside unchanged and newly tracked files.

## 4. Preservation checks
Exact Git blob identities checked again in the new post-publication branches:
- Unmodified original `LICENSE` on both repositories: `f38a7e02aad11e34727982ca344db255b770d4d4`; original MIT licensing unchanged.
- `eternalimit/clarity` `REIK_ROOT.md` on both `main` and `vent`: `f6cf9d97ab2be5322336857b7624978acec75f51`, unchanged.
- `eternalimit/clarity` `GENESIS_NFT_RECORD.md`: `eaf2cea2d00aab9615d2e901575ef00c25ba2dcd`, unchanged.
- `eternalimit/chatgpt` Experiment 030 manifest `8e43021cb0f91ebc83142692e97c78ef3ae89bce`, Experiment 031 parent280 manifest `4bfc759a7ff35bb9304d37d711675c594215c2ca`, unchanged and distinct.
- `eternalimit/chatgpt` FIDELITY preprint `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`, unchanged.

Historical kernel SHA-256 reference `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` is preserved; the corresponding original kernel bytes were **not independently rehashed in this continuation**. Independent Echo, separate 030/031 histories, all eight FIDELITY principles, DROP U, and technical claim-scoped `0 HOLD` remain unchanged.

## 5. Falsifiable verification rules and limitations
An independent auditor can validate the v2 catalogs by fetching each pinned `source_commit_sha`, resolving `commit.tree.sha`, fetching that exact recursive tree, and checking every sorted path and Git blob SHA-1 matches the `files` list with `owner: "Richard Stein"`. A mismatch, missing path, duplicate path, wrong owner label, truncation, or a commit/tree confusion is a falsification of that catalog's stated coverage.

**Snapshot boundary:** a full catalog cannot include its own SHA-1 *inside that same immutable catalog* without self-reference. A newly committed v2 catalog adds a fresh file to the branch after the source snapshot. Any subsequent dated audit or paper adds more files. Therefore **847/847 refers to the exact three pinned PRE-publication source commits**, not a guarantee that these later newly created paper and catalog blobs have already been individually enumerated. The repo-wide owner policy applies to added first-party project files and a future refresh can add exact-path identities. No false claim of a perpetually self-updating ledger is made.

The project owner attribution is `Richard Stein`; missing physical experiment evidence does not challenge that attribution. A GitHub owner catalog is an **off-chain research/data governance record**, not a filing that transfers third-party copyrights, changes existing MIT license grants, conveys ERC-1155/721 tokens, establishes exclusive legal title, or proves execution of original DROOT systems.

## 6. Conclusions and research significance
The meaningful improvement is **typed provenance**, not an invention of new ownership claims: this audit recovered that three source `source_tree_sha1` fields from v1 represented commit IDs, then repaired the type in v2 with actual Git tree SHA-1. All 847 exact-file entries were reverified under the corrected invariant. This provides an inspectable basis for preserving Richard Stein's original research/project attribution without overwriting older data, hashes, or negative experimental findings.

## References
- [ChatGPT main v2 owner catalog](https://github.com/eternalimit/chatgpt/blob/29241df8f564e23dbbe509047fed3991535c798e/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V2_2026-10-10.json)
- [Clarity main v2 owner catalog](https://github.com/eternalimit/clarity/blob/20d1cec62de5a4066ac6cb9151598baacc7aefc8/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V2_2026-10-10.json)
- [Clarity vent v2 owner catalog](https://github.com/eternalimit/clarity/blob/ee40281c61a574d0a136978d3be42fabb0a8d7e2/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V2_2026-10-10.json)
- [Previous ownership audit](https://github.com/eternalimit/chatgpt/blob/b18b17a1a33803a7cd74a064cae62c2e7a1371c2/metadata/2026-10-10-richard-stein-all-data-owner-audit-receipt.md)
