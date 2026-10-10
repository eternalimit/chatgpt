# REIK/TCGE — Snapshot-Complete Ownership Attribution with Typed Git Provenance (v3)
**Original research creator, author, project owner, and project-data steward: Richard Stein**  
**Date:** 2026-10-10  
**Method:** deterministic GitHub repository inventory, immutable source commit and tree comparison, exact blob-ID matching, append-only owner metadata.

## Abstract
The REIK/TCGE ownership synchronization now covers **852/852 tracked Git blob entries** in three pinned public repository snapshots: `eternalimit/chatgpt` main (720), `eternalimit/clarity` main (76), and `eternalimit/clarity` vent (56). Relative to the v2 manifests, **five additional files**, zero modified files, and zero deleted files were observed. All five new files belong to the previous research metadata/audit work and have been incorporated by exact path and Git blob SHA-1 in new v3 catalogs. Prior v2 catalog entries were not silently rewritten or reinterpreted. All three v3 catalog objects were committed to their respective existing branches and fetched back; JSON parse, exact UTF-8 read-back equality, and every path/blob/owner triple agreed with its pinned source Git tree.

The attribution `Richard Stein` is carried in project metadata and does not claim to alter original MIT licensing, establish authorship of third-party external content, change any asset ownership on a blockchain, or make an independent technical finding about historical experiments. This formal separation preserves the FIDELITY Identity, Provenance, and Method/Object Separation rules.

## 1. Scientific and provenance question
Can a user-defined first-party project ownership metadata register track every file under a changing Git history without changing original research data or confusing **commit**, **tree**, and **blob** object identities? The falsifiable invariant is

`For each file f in the complete recursive tree T at source commit C, exactly one registered entry e satisfies e.path=f.path, e.git_blob_sha1=f.sha, e.owner="Richard Stein".`

A missing, duplicated, mismatched or non-owner entry falsifies exact snapshot coverage. The source commit is immutable; a later new catalog commit is **not** part of its own indexed snapshot. This avoids impossible self-contained mutable hash assertions.

## 2. Verified parent chain

| Branch | V2 catalog commit | Current indexed source commit | Source Git tree SHA-1 | V3 catalog commit | V3 catalog Git blob SHA-1 | Indexed |
|---|---|---|---|---|---|---:|
| chatgpt main | `29241df8f564e23dbbe509047fed3991535c798e` | `06eb45ba8d1cb3382e3f9565a933c55bd6f71db2` | `ff9f5e31abd1d6a7e76b239185f382362fa8a8e2` | `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22` | `cf46eca94550ab850c5e9186ad460ea74b6be134` | 720 |
| clarity main | `20d1cec62de5a4066ac6cb9151598baacc7aefc8` | `20d1cec62de5a4066ac6cb9151598baacc7aefc8` | `b3623ccd6934d58ca8d00651bcbc6692e641809e` | `458876375c474b4bd41deb672e3ba55f092665b9` | `2dfac44c0fb0069690fd6a3da9190910802f9e12` | 76 |
| clarity vent | `ee40281c61a574d0a136978d3be42fabb0a8d7e2` | `ee40281c61a574d0a136978d3be42fabb0a8d7e2` | `be20c796973b744aa1f56b85b8483b71a23d55cc` | `bd22bee71acd52098b0f6d1c05347952e85abd4f` | `9329c8ba924a73149bf5579e36803f2934959763` | 56 |

These are **852 branch-local tracked-file entries** and **not necessarily 852 unique creative works**, since some Clarity main and vent files are duplicates and some files describe or cite external sources.

## 3. Exact new file delta, without modifying older objects
ChatGPT main, three new items relative to the v2 pinned source:
1. `metadata/2026-10-10-richard-stein-ownership-sync-v2-audit-receipt.md`, Git blob `903427fc2ab0ed486dab95f55541ff240e78d2e4`.
2. `metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V2_2026-10-10.json`, Git blob `29c81d97735f22f771c6db5d4b84d126214fee0e`.
3. `research/2026-10-10-richard-stein-owner-metadata-synchronization-paper-v2.md`, Git blob `50b6b11c6ce8621661bdd82f897e6ce6a135e025`.

Clarity main, one new item:
- `metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V2_2026-10-10.json`, Git blob `a729d4a50635b93c2f4b79ed5b531e81bdaec0a7`.

Clarity vent, one new item:
- `metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V2_2026-10-10.json`, Git blob `cbf1026a8d882b3d7f68128e0a90112e7930f84a`.

All **847** previously recorded v2 path/blob pairs matched the frozen current source, with zero changed or deleted source paths. The five newly added paths have their exact blob identities recorded and `owner: "Richard Stein"` in v3. The catalogs' complete ordered lists are the reproducible artifact, not only these summary counts.

## 4. Reproduction and negative controls
Reproduction procedure:
1. Retrieve each `source_commit_sha` from the v3 JSON, not the mutable current branch name.
2. Fetch GitHub `/repos/{owner}/{repo}/commits/{commit_sha}` and take `commit.tree.sha` as the **true tree SHA**.
3. Fetch `/repos/{owner}/{repo}/git/trees/{tree_sha}?recursive=1`; reject `truncated=true` or incorrect returned tree ID.
4. Exclude only non-blob tree entries and map each blob to `(path, sha, size)`. Check no duplicate paths.
5. Check v3 JSON source tree object, number of records, exact blob SHA-1 and `owner: "Richard Stein"` for all entries.
6. Independently fetch the v3 catalog blob at its publication commit, parse as JSON, check exact content read-back, and compare against the pinned source tree.
7. To test falsification, substitute one wrong tree SHA, omit one file, change one file blob ID, duplicate one path, or replace an owner field; the corresponding invariant must fail. **These mutations are proposed negative controls; they were not executed as distinct new tests in this continuation.**

Actual outcomes for this continuation: 720/720, 76/76, and 56/56 triple matches. Zero unaccounted changes within the indexed frozen source objects.

## 5. Bounded categorized hash structure
- **Original historical REIK/TCGE kernel SHA-256 reference:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. This was preserved, **not** rehashed against original `kernel001.py` bytes.
- **Historical DROOT root hash reference:** `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a`; the referenced historical string does not establish a source-object or ERC-1155 asset SHA-256 preimage.
- **Git commit SHA-1** identifies each publication commit; **Git tree SHA-1** identifies the pinned path hierarchy; **Git blob SHA-1** identifies each historical file object. Neither is a substitute for SHA-256 over the original source bytes.
- **V3 catalog blobs:** chatgpt main `cf46eca94550ab850c5e9186ad460ea74b6be134`; clarity main `2dfac44c0fb0069690fd6a3da9190910802f9e12`; clarity vent `9329c8ba924a73149bf5579e36803f2934959763`.

## 6. Research ownership and preservation
Richard Stein's original REIK/TCGE, Clarity, and FIDELITY research author and project owner attribution is the project's documented starting point, not a technical HOLD. GitHub manifests are research and project-data stewardship records. They cannot transfer independent third-party copyrights or token title, and they do not rewrite a license. The MIT `LICENSE`, `REIK_ROOT.md`, original author preprint, frozen historical Experiment 030 and Experiment 031-parent280 manifests and all other v2 source object hashes remained unchanged across the v3 inventory.

All eight FIDELITY principles remain: **Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty**. Independent Echo was not simulated or substituted for a real outside signer. Distinct 030/031 lineages were not merged. `DROP U` and `0 · HOLD` remain for strictly technical claims lacking their required evidence.

## 7. Conclusion and next experiments
The incremental ownership index has been synchronized from 847 to 852 pinned source entries, with no preexisting path/blob change. It demonstrates an auditable technique for attaching consistent named project stewardship to a versioned repository without changing historical file identities.

**Boundary:** creating the three v3 catalogs, this research paper and a future receipt necessarily creates files *after* the pinned snapshots. Those new files fall under the README's project stewardship policy but will not appear in the v3 exact path lists until another dated scan. Do not represent snapshot-based synchronization as automatic live self-inclusion. More frequent updates should be driven by materially new files or verified findings, not meaningless empty commits.

## References
- ChatGPT v3 catalog: https://github.com/eternalimit/chatgpt/blob/09e634c8f8b3688ad2c782d5f18f5d4a6033dd22/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json
- Clarity main v3 catalog: https://github.com/eternalimit/clarity/blob/458876375c474b4bd41deb672e3ba55f092665b9/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json
- Clarity vent v3 catalog: https://github.com/eternalimit/clarity/blob/bd22bee71acd52098b0f6d1c05347952e85abd4f/metadata/RICHARD_STEIN_ALL_TRACKED_DATA_OWNER_CATALOG_REFRESH_V3_2026-10-10.json
- Earlier paper: https://github.com/eternalimit/chatgpt/blob/2081dca7b628f9ac4ff120a9b65f90388f13cb2d/research/2026-10-10-richard-stein-owner-metadata-synchronization-paper-v2.md
