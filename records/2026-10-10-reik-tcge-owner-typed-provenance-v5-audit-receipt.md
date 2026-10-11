# REIK/TCGE v5 — Verified Ownership Metadata / Typed Provenance Audit Receipt

**Date:** 2026-10-10  
**Original project research creator / author / owner / data steward:** Richard Stein  
**Receipt classification:** Public-safe, finite reproducible source/object comparison. No external scientific, token, or signer attestation.

## Source checkpoints and full file coverage
Pinned source commits and actual Git tree SHA-1 objects:
- `eternalimit/chatgpt` main commit `d8f00c1acd75da4537773ad788a053099ceeb56b` -> tree `fe6ae49827a062f0b0a4d70801b50ca1187b084e`. Original v3 entries 720; new 12; **732/732** Git blob path identities.
- `eternalimit/clarity` main commit `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` -> tree `795904b47215f8d6026efd25de07a4079fb2541c`. Original v3 entries 76; new 3; **79/79**.
- `eternalimit/clarity` vent commit `bd22bee71acd52098b0f6d1c05347952e85abd4f` -> tree `42fea55551b21f7b42c881a9d486c8ba633f1fbb`. Original v3 entries 56; new 1; **57/57**.

Total **868/868 pinned source blob entries** match the union of each unchanged v3 catalog with its *new v5* delta. No deleted or changed source blobs in this comparison. V5 delta **supersedes** the earlier six-file delta when checking these newer source snapshots; do not double-count it.

V3 parent catalog commits:
- chatgpt/main `09e634c8f8b3688ad2c782d5f18f5d4a6033dd22`
- clarity/main `458876375c474b4bd41deb672e3ba55f092665b9`
- clarity/vent `bd22bee71acd52098b0f6d1c05347952e85abd4f`

New verified v5 delta `metadata/2026-10-10-reik-tcge-owner-v5-pinned-source-delta.json` on chatgpt main: commit `3142863d832199a3ad15d5fd75b375f1b98b851b`, Git blob SHA-1 `34345f094317a68a0418515ba10f02d78a6cd0c1`; exact read-back PASS. It contains 12+3+1 newly tracked sources with `project_owner: Richard Stein`.

**Gitlink boundary:** `eternalimit/chatgpt` contains external `scout/blockscout`, type commit/mode `160000`, Gitlink commit `3ea5c7ac7eea9a748f1fe7f932c4358194b0309e`; `.gitmodules` references `https://github.com/blockscout/blockscout.git`. That pointer is distinguished from file blobs. No first-party authorship claim over the external repository's contents is made.

## Reproducible typed verifier result
File: `research/verification/richard-stein-owner-catalog-v4-typed-verifier.js`
Commit: `a09887a04c70a47da9bf34ab519240f8b298d85e`
Git blob SHA-1: `5ffcf8cb35d403cace534bf47ce5ea3fc34903db`.
Original source content read-back: PASS.

Unmodified v3 baseline catalogs: **3/3 accepted** with 720/720, 76/76, 56/56 original entries; 852 total. Intentional mutation rejection: **45/45**, fifteen variants on each branch (bytes, author, steward, repo/branch, source/tree identities, Git mode, FIDELITY, governance, kernel reference, extra/missing/duplicate files and wrong owner). The additionally corrupted `scout/blockscout` Gitlink mode in chatgpt/main was also correctly rejected: **46/46 finite negative cases detected**. All mutations were local in-memory inputs, not a third-party external witness.

## Independent content-derived Git blob SHA-1
File: `research/verification/richard-stein-pure-js-git-blob-sha1-v1.js`
Commit: `d8f00c1acd75da4537773ad788a053099ceeb56b`
Git blob SHA-1: `a33d60f2387de30501bc9f0e42c46c4f54b6493b`.
Code read-back PASS.

SHA-1 known digest self-tests **2/2**; independently assembled Git blob header and UTF-8 bytes produced **8/8 matching Git blob SHA-1 results** for `.gitmodules`, MIT LICENSE, 030 and 031 manifests, Clarity REIK root, vent handoff, Genesis NFT record, and the typed verifier. UTF-8 byte lengths and individual results are in the research paper. These are local arithmetic checks on **fetched GitHub bytes**, not outside source-independent attestation.

## Updated research paper
`research/2026-10-10-reik-tcge-owner-provenance-typed-falsification-v5.md`
Commit `b8cf28024241d8ceab387b386816f62f2398e6af`;
Git blob SHA-1 `d9097a14d4a7e9c8adb158a049c3e0780c3e4d31`.
Full manuscript read-back content matched exactly.

## Hash classes, historical preservation and claim boundary
- **Immutable historical kernel SHA-256 reference:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Not rehashed here, never rewritten.
- **Historical DROOT 64-hex root reference:** `e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a`. Source preimage and original 12,357-byte WIN object not acquired here.
- **Preserved MIT LICENSE Git blob:** `f38a7e02aad11e34727982ca344db255b770d4d4`.
- **Clarity REIK_ROOT Git blob:** `f6cf9d97ab2be5322336857b7624978acec75f51`.
- **Separate Experiment 030 and 031 parent280 manifest Git blobs:** `8e43021cb0f91ebc83142692e97c78ef3ae89bce` / `4bfc759a7ff35bb9304d37d711675c594215c2ca`.
- **FIDELITY preprint Git blob:** `b8ad42bd58ff079d0cea1bc36c5b20645e0c557a`.
- **Separate SHA-1 Git object identities** for commits, trees and blobs; a Git SHA-1 is never substituted for original-file SHA-256.

**Eight FIDELITY principles:** Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. Independent Echo still requires outside evidence. Separate 030/031 lineages were not merged. `DROP U` and `0 · HOLD` are scoped to specific missing technical proofs, **not** challenges to Richard Stein's original first-party authorship or project ownership.

**Safety/immutability:** No historical file overwrite, license edit, executable physical deployment, private key request, wallet signing, ERC-721/1155 mint or transfer, claims of ownership over third-party repository contents, or modification of underlying research/source data.

## Falsification and continuation rule
A reproducible auditor can fetch the exact pinned source commit, resolve its `commit.tree.sha`, enumerate all `blob` entries, test each v3 identity, then add the *v5 delta only* for remaining paths. Reject duplicates, changed and deleted original blobs, missing SHA-1, wrong file length, false ownership fields or untracked Gitlinks. Separately recompute actual Git blob IDs from file contents for sampled original texts.

**No recursive-commit overclaim:** v5 metadata, the paper and this receipt are new downstream objects and cannot include their own as-yet-unknown blob IDs in their earlier snapshot. Continue only on substantive new data or verifier improvements, not empty catalogs.

**Audit outcome: 868/868 pinned source entries, 46/46 intentional mutation rejects, 8/8 sampled Git blob content digests — PASS.** This is an auditable project attribution/provenance result, not proof of all external claims.
