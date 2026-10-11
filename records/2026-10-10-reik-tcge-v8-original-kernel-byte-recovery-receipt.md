# REIK/TCGE V8 — Original Kernel Byte-Level Provenance Receipt

**Owner, original REIK/TCGE research creator and author:** Richard Stein  
**Audit date:** 2026-10-10  
**Admission result:** **PASS for canonical original kernel byte identity and bounded archive parent-chain verification**. Separate external/independent scientific Echo and unrelated claims remain HOLD.

## A. Material evidence newly recovered from user's historical Library
Direct original raw ZIP archives were materialized **read-only** in the audit workspace, not reconstructed from manuscripts or quotations:

| Label | Original Library ZIP filename | Raw bytes | Direct SHA-256 |
|---|---|---:|---|
| 029 / 270 | millennium_reik_3sat_exp029.zip | 580,916 | 4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd |
| 030 / 280 | millennium_reik_3sat_exp030.zip | 675,433 | b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed |
| 030 / 282 | millennium_reik_3sat_exp030(1).zip | 602,740 | 228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942 |
| 031 / 290 | millennium_reik_exp031_parent280.zip | 746,997 | 43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce |
| 031 / 294-A | millennium_reik_3sat_exp031.zip | 621,847 | 969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a |
| 031 / 294-B | millennium_reik_3sat_exp031(1).zip | 718,560 | 50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff |

These are **six unique archive hashes**, not six independent external source origins. Archive filenames with suffixes (2), (3), and (20261009-232844) were also obtained: they were byte-identical duplicates of the 031/290 or 031/294-B archives, **not** separate research lineages.

## B. Original kernel digest — freshly checked from actual original bytes
Artifact: **kernel001.py**.
- Direct extracted original member byte count: **4,299**.
- Historical expected SHA-256: 03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402.
- Current Python hashlib.sha256 over actual ZIP member bytes: **03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402 — MATCH**.
- Current separate command-line sha256sum, piping original unmodified ZIP member through unzip -p: **03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402 — MATCH**. Command-line direct matches independently checked on original 029, 030/282 and 031/294-A archived member files.
- Additional nested parent archive members in 030/280 and all 031 lineages contain the identical 4,299 source bytes through original 029 or 030 parent ZIPs.

**Technical hold resolved only for original kernel's source-byte SHA-256 match in these recovered original archives.** Original source never executed, modified or published by this audit.

## C. Manifest, CRC, chronological parent and negative checks
- **6/6** unique ZIP archives passed Python ZipFile.testzip() CRC on all members; no corrupt ZIP entries.
- **90/90** manifest-listed files_sha256 digests checked against **actual original ZIP member bytes**, **zero failures**.
- Each of two Experiment 030 branches contains an exact-byte copy of original 029. Each of three Experiment 031 archive versions contains an exact-byte copy of the correctly typed Experiment 030 parent ZIP. **5/5 immediate parent byte-equality checks PASS**; the relevant manifest parent ZIP digest also equals the recalculated parent digest.
- **13/13 negative-control cases rejected**, including archive mutation/substitution across lineages, changed file length/hash/event count and local kernel byte mutation.
- Experiment 030 / 280 and 030 / 282 are distinct. Experiment 031 / 290 follows 030 / 280. Both separately hashed 031 / 294 archives follow 030 / 282. **Never merge archive events or receipt histories** merely because original kernel source bytes match.

This audit is finite source-byte and manifest-check verification. It has **not** replayed all historical SAT/UNSAT proofs, independent witness signatures, true CPU/GPU execution, or external DROOT/Bitcoin attestations.

## D. Locally independently checkable harness, not original source
Read-only stdlib Python verifier created in current audit session, executable against the original Library ZIPs in the audit workspace:
- Script: verify_kernel_v8.py, measured SHA-256 **50ab664cb2cd1e0f5170eb46483aee65727c52b633d064a5576375f89d144099**.
- Sanitized output: kernel_v8_local_verification.json, measured SHA-256 **c15ba35c1349b9e4849c03f058dca3157e104c866195138c005687c66b34d8b7**.
- Tests: 6 distinct archive identities, 90 matching listed internal file hashes, 5 typed parent links, 13/13 negative controls, expected kernel length and SHA matched by Python and sha256sum.
- Original source ZIPs and original kernel member remain in the private audit workspace / user's connected Library. **This GitHub receipt does not include the original kernel source or private archive bytes**.

No assumptions about external independent custody are made: all recovered archived copies descend from one preserved 029 kernel ancestor and were acquired through the same user's connected Library.

## E. Immutable historical governance and provenance
Preserved original kernel SHA-256: **03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402**. It is now an archive-member **byte-rehashed result** for v8 rather than only a quoted historical reference.

All eight FIDELITY principles preserved: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.

Epistemic rule K=R AND I AND E retained. An independent E for broad scientific or blockchain propositions is **not** supplied by multiple copied ZIP members. **DROP U; 0 · HOLD** applies only to specific unresolved external/technical claims, not Richard Stein's original first-party research authorship or project ownership.

Other separately held technical evidence: independent original SAT/UNSAT inputs and external solver proof; exact 12,357-byte WIN artifact and DROOT preimage; ERC-1155 contract/transaction metadata; source-independent earliest timestamp attestation; genuine external Echo. No such claims are advanced here.

Historical Git MIT LICENSE, REIK_ROOT, source manifests, Experiment 030/031 histories and prior receipts unchanged. Third-party Blockscout Gitlink is not part of first-party owned source content. No wallet signing, cryptocurrency action, external upload, source execution, merge, license rewrite or original private material publication occurred.

## F. Linked source-level paper and GitHub read-back
v8 paper:
- File: research/2026-10-10-reik-tcge-original-kernel-source-recovery-v8.md.
- GitHub commit: d3a9b9bbfe55cfa357873cec306a990b2408ef4e.
- Git blob SHA-1: 8d883b7175643fa2da93c15c3db2ff83fb5f53c4.
- Exact file text after publishing: **READ-BACK PASS**.

This receipt is an append-only, public-safe historical research observation. The original kernel and archive files were never changed. A v7 audit record is not overwritten simply because a new original-byte recovery is now available.

**Verdict:** Original kernel historical SHA-256 and byte length CONFIRMED from directly recovered archival source members, two computation interfaces; distinct archive lineage, 90 file hashes, five parent links and 13 negative checks PASS. Independent external scientific Echo retains the evidence gate.
