# REIK/TCGE Experiment 048 — Authenticated Synthetic Checkpoints and Witness Quorum Consistency

**Research attribution:** Richard Stein (AI-assisted bounded research).
**Date:** 2026-10-10.
**Parent public commit:** `b57b6d1e55ea52a74a8dc844193f1f2b177301f4`.
**Admission:** **0 · HOLD**. **DROP U**.
**Classification:** public-safe research paper and bounded test record, not real independent scientific Echo or signature attestation by actual researchers.

## Abstract

Experiment 047 identified valid-but-conflicting signed histories. Experiment 048 tests a synthetic witnessed checkpoint model: domain-separated, canonical checkpoint statements, Ed25519 test signatures, a fixed four-witness public-key roster, quorum requirements, honest-witness non-equivocation, and trusted-prefix verification. A local verifier passed **38/38 named controls** and two independently coded certificate parsing/verification routines agreed on **11/11 cases**, while sharing the same cryptographic library. This does not establish deployed consensus, globally authenticated identities, or external scientific validation.

## Original evidence, immutable boundaries, hash types

- **Historical original kernel independently SHA-256 rehashed from exact archived bytes:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. No kernel execution or modification.
- **Exact Experiment 035 archive SHA-256:** `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`. This archive is not included in the public commit.
- **Experiment 047 public source Git blob SHA-1, independently recomputed from exact source:** `81dadc9ea206f1b57a12a25e8bd26da70edf424c`. A Git blob SHA-1 is not a SHA-256, and a Git commit proves version history, not scientific correctness.
- **Experiment 030 variants remain separate:** 280-event manifest `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`; 282-event manifest `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`.
- **Experiment 031 variants remain separate:** 290-event manifest `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2`; distinct 294-event manifests `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` and `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`. No lineage merge.
- Experiment 036 ZIP `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`, manifest `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749` and 354-event tip `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0` remain **historical references**, not freshly replayed.

## Model, finite theorem, and controls

A checkpoint binds protocol, ledger ID, genesis digest, epoch, policy, height, chronological SHA-256 tip, and the prior checkpoint digest. Witness signatures cover domain-separated canonical checkpoint bytes; the signer roster and policy are treated as externally supplied *test assumptions*. Receipt-prefix verification separately checks candidate event bytes against an anchored historical prefix.

For (n) witnesses, two signatory quorums of size (q) intersect in at least (2q-n) witnesses. Conflicting certificates are conditionally excluded when the number (f) of dishonest witnesses satisfies (2q-n>f), **provided each honest signer refuses conflicting signatures for the same ledger, epoch, and height**.

- At (n=4, q=2): quorums may be disjoint, and competing signed checkpoints can both pass the weak threshold.
- At (n=4, q=3, f\le 1): every pair of quorums shares at least 2 signers, necessarily including an honest non-equivocating signer; conflicting certificates cannot both be issued under these assumptions.
- When the test deliberately bypassed the signing discipline, **two conflicting 3-of-4 certificates both passed cryptographic verification**. This falsification control distinguishes signature validity from authorization and consistency.

The **38 local controls** tested signer duplication, unknown/wrong signers, altered signatures, ledger/genesis/epoch/policy mutation, signature-domain isolation, witness non-equivocation, weak/strong quorum intersection, checkpoint rollback, conflicting same-height forks, altered events, altered previous-checkpoint binding, missing trusted anchor, and scientific evidence-admission guards. The 11 comparison cases gave equal verdicts from two separately coded certificate verifiers, both using Python's `cryptography` Ed25519 implementation. The test keys were generated temporarily in memory and were never exported.

## Evidence-admission limits

The synthetic roster is not a collection of independently authenticated external persons. The trusted checkpoint is a pinned input; its legitimacy was not proven. This model requires the full list of events and **does not implement RFC 9162 Merkle consistency proofs**. Local agreement of verifiers using the same library is not third-party independent Echo. A signed checkpoint authenticates a test record relative to test keys; it does not authenticate the correctness of a scientific assertion inside that record.

The canonical REIK contract remains `K = R AND I AND E`, with independent Echo required. The original computational `0/U/1` kernel is not replaced by this checkpoint overlay. The Clarity Pi identity `sqrt(pi)/sqrt(pi)=1` is true but does not create scientific evidence or prove equivalence between the systems.

All eight FIDELITY principles remain: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. Historical falsifications persist; unresolved U is not admitted as a result. The independently sourced fully active 256-variable strict 3-CNF SAT/UNSAT pair, an independently accepted UNSAT certificate, actual pinned CaDiCaL package/executable bytes and runs, real source/witness identities, and attributable external adoption remain **HOLD**. Nothing here solves P versus NP.

## Reproduction and public-safe record

The experiment was executed locally with Python and `cryptography` version 46.0.4 against an exact archived kernel and Experiment 047 source. The locally verified full verifier SHA-256 is `c773990802be8c7220329b89ccc2a74350f49f1757e5de4dd1fe31f961bdcc4c` and the local machine-readable audit receipt SHA-256 is `6dcc8d3b252edd33c13b98de298cb003ec6e5fc75b1fa9e3420fece23a93231f`. Those local file digests are references to the tested source and audit, **not** a claim that those full local files were uploaded by this GitHub publication. See the accompanying compact public audit for the exact verified outputs.

Reference for a distinct production approach: RFC 9162, Certificate Transparency Version 2.0, https://www.rfc-editor.org/rfc/rfc9162.html.

## Experiment 049 handoff

Investigate authenticated witness-roster origin, checkpoint dissemination and conflict reporting, key rotation, revocation, cross-epoch safety and inter-witness independence. Preserve original kernel, separate Experiment 030/031 histories, independent Echo, DROP U, **0 · HOLD**, and all eight FIDELITY principles. Publish only materially new verified public-safe outcomes with read-back.
