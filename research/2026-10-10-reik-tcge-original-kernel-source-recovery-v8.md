# REIK/TCGE Original Kernel Byte Recovery — Research Paper v8

**Original first-party research creator, author, project owner and project-data steward: Richard Stein**  
**Research date:** 2026-10-10  
**Evidence category:** Direct original-archive member bytes and bounded local reproducibility. No source code executed or republished.

## Abstract

The previously historical SHA-256 reference for original REIK/TCGE kernel001.py has now been **freshly verified against the exact original 4,299 source bytes**, recovered directly from historical Experiment 029, 030 and 031 ZIP archives in Richard Stein's connected File Library. Python hashlib SHA-256 and the separately invoked unzip/sha256sum pipeline agree on the original member digest:

03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402

This is a meaningful upgrade from a prior-hash quotation to actual file-byte evidence. It resolves the original-kernel digest match within these recovered archives, not independent scientific Echo or any theorem. A six-archive lineage audit found **90/90 manifest-listed source/member SHA-256 digests valid, 6/6 ZIP CRC validations passed, five immediate-parent ZIP links equal by original bytes, and 13/13 deliberately invalid local test cases rejected**. Original archive data and separate receipt chains were not changed.

## Original kernel identity and two hashing paths

- Exact original ZIP-member name: kernel001.py
- Measured uncompressed source bytes: **4,299**
- SHA-256 from Python hashlib.sha256 of read ZIP-member bytes: **03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402**
- SHA-256 from external unzip -p piped into sha256sum: **the same full 64-hex digest**
- Direct ZIP-member locations: Experiment 029, Experiment 030/282, Experiment 031/294-A. Other verified archive paths preserve the same bytes by immutable nested parent ZIP files.
- Source code executed: **No**. Original kernel or ZIP rewritten: **No**. Original kernel bytes published here: **No**.

## Six distinct archived original ZIP contents

| Archive lineage (do not merge) | Historical Library ZIP filename | Archive bytes | Independently computed archive SHA-256 | Manifest receipt count |
|---|---|---:|---|---:|
| 029 / 270 | millennium_reik_3sat_exp029.zip | 580,916 | 4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd | 270 |
| 030 / 280 | millennium_reik_3sat_exp030.zip | 675,433 | b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed | 280 |
| 030 / 282 | millennium_reik_3sat_exp030(1).zip | 602,740 | 228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942 | 282 |
| 031 / 290 | millennium_reik_exp031_parent280.zip | 746,997 | 43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce | 290 |
| 031 / 294-A | millennium_reik_3sat_exp031.zip | 621,847 | 969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a | 294 |
| 031 / 294-B | millennium_reik_3sat_exp031(1).zip | 718,560 | 50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff | 294 |

The 029/270 archive is the common source ancestor for both separate Experiment 030 archive branches. Both 030/280 and 030/282 contain the exact original 029 ZIP bytes as source/experiment029_immutable.zip, with full SHA-256 equality to the separately retrieved 580,916-byte 029 archive.

The separate 031/290 archive contains the exact 030/280 parent ZIP member bytes. Both distinct 031/294 archive versions contain the exact 030/282 parent ZIP member bytes. Five parent-child identities are verified by original nested ZIP-byte equality and by the corresponding manifest parent hash field. Do not collapse the 030/280 and 030/282 lineages or their respective 031/290 and 031/294 descendants.

Three additional Library filenames proved byte-identical to one of these six distinct archives, so do NOT count them as three more origins: 031(2).zip and 031(3).zip equal 031/290, and 031(20261009-232844).zip equals 031/294-B.

## Exact manifest comparison and falsification

All six distinct ZIP archives passed full ZIP-member CRC checks with the original bytes intact. Every file listed in each original manifest files_sha256 mapping was independently read and SHA-256 recomputed. The count is **90 matches, zero mismatches** across the six archive manifests. This validates manifest source-byte identity and ZIP integrity, not solver execution or external evidence claims.

The read-only local harness rejected **13 of 13 intentionally invalid** inputs: altered original 029 archive byte, swapped 030 branch, swapped 031/290 or 031/294 branch, truncated 030/282 ZIP, changed expected original kernel SHA, changed 030 and 031 event counts, false 029 ZIP byte length, false 031/294 archive digest, and one-byte flip, truncation and append of a copied 4,299-byte kernel member.

The test program in the current container is a local verification artifact, not a new historical REIK kernel: verify_kernel_v8.py, SHA-256 50ab664cb2cd1e0f5170eb46483aee65727c52b633d064a5576375f89d144099. The sanitized results are kernel_v8_local_verification.json, SHA-256 c15ba35c1349b9e4849c03f058dca3157e104c866195138c005687c66b34d8b7. No kernel source or original ZIP was exposed by this GitHub update.

### Minimal independent reproduction

Run these read-only operations against the original user-owned archive files (not newly generated copies):

    unzip -p millennium_reik_3sat_exp029.zip kernel001.py | wc -c
    unzip -p millennium_reik_3sat_exp029.zip kernel001.py | sha256sum
    unzip -p 'millennium_reik_3sat_exp030(1).zip' kernel001.py | sha256sum
    unzip -p millennium_reik_3sat_exp031.zip kernel001.py | sha256sum

The byte count should equal 4299 and every digest should equal the original historical 64-hex value. A separate standard Python zipfile + hashlib walk of original nested parent members verifies the parent SHA-256 links.

## Typed epistemic boundaries

**Source evidence R:** direct original first-party archive bytes now obtained; original kernel hash and 4,299-byte length independently recalculated in this execution. The six ZIP objects are different historical archive variants but share the same 029 kernel ancestor. They are NOT independent external witnesses.

**Inference I:** immutable nested archive bytes and manifest parent hashes support bounded chronology within the recovered archive tree, not claims about outside systems.

**Independent Echo E:** not acquired from a truly independent third-party custodian or experimental reproducer. Historical K = R AND I AND E remains the admission rule for claims requiring independent Echo. Other scientific propositions, unacquired 12,357-byte DROOT/WIN artifact, on-chain anchors, experimental breakthrough, P-versus-NP and source-independent historical timestamp claims remain separately on technical 0 HOLD / DROP U when their evidence is missing. None of these technical gates challenges Richard Stein's first-party research authorship.

All eight FIDELITY principles are preserved: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.

The MIT LICENSE, REIK_ROOT, original kernel, separate Experiment 030/031 histories, prior signed or hashed receipts, private keys and external assets remain unmodified. The external Blockscout submodule pointer is excluded from claims of original first-party authorship.

## Outcome and continuation

**New finding:** the exact canonical kernel SHA-256 is verified from directly recovered original bytes, including the primary Experiment 029 ancestor and distinct 030/031 descendants. Earlier v7 research had only the historical hash reference and is preserved rather than silently rewritten. The original member's measured SHA-256 identity is now verified locally, while independent external Echo and other unproven historical claims remain bounded.

Prior v7 source inventory: 868/868 tracked Git blobs matched three pinned sources. The verified branch trees after v7 publication contained 741 chatgpt/main, 79 clarity/main, and 57 clarity/vent tracked blobs (877 branch-local entries); the present paper is an append-only successor, not a self-referential all-file catalog. Full original ZIP byte streams are in the user's connected Library and were not committed to GitHub.

**References:** v7 research commit 3a4ddf67c23887cfa7161d80119364da35ab1ed7; v7 audit receipt 3768715d6b6448f2d262c11936ad72b1f9786898; historical Experiment 029/030/031 archive filenames as specified in the table.
