# REIK/TCGE Research Paper — Experiment 049

**Title:** Synthetic Witness Authentication, Checkpoint Conflict Falsification, and Cross-Epoch Trust-Pin Rotation  
**Research attribution:** Richard Stein — REIK/TCGE (AI-assisted bounded research)  
**Date:** 2026-10-10  
**Parent public commit:** `a0102fd8320aa8f5ea267ce48f57c740068cf600`  
**Admission:** **0 · HOLD**. **DROP U**.  
**Nature of evidence:** Reproducible synthetic software tests. Not independent external Echo, real-world identity proof, or science admission.

## Abstract

Experiment 048 reported 38 local checkpoint controls, but its original complete test program was not uploaded. Experiment 049 adds a separately built, reproducible Python Ed25519 harness and reports **46/46** bounded checks passing locally with cryptography **46.0.4**. The harness demonstrates two fundamental limits: (1) valid signatures over two conflicting histories do not imply history consistency if signers equivocate; and (2) even perfectly valid signatures cannot establish whether a signer roster has a trustworthy real-world origin. A conditional old-roster-authorized epoch-rotation procedure and trusted-parent checks reject several simulated takeover and rollback paths. All keys, witnesses and ledgers here are explicitly synthetic.

## Problem and methods

Given a pinned trusted roster of four Ed25519 demo public keys, an externally supplied roster digest, fixed policy q=3, and a separately trusted prefix anchor, the verifier checks domain-separated canonical checkpoint bytes, signer uniqueness, signer authorization, quorum count, ledger and genesis, policy, epoch trust, chronological height, and exact predecessor digest. Signature validation uses the Python `cryptography` library. A distinct rotation-message signature domain tests whether a previously trusted roster (three signers) can authorize a new roster for the next epoch. A set of negative controls deliberately modifies inputs and confirms rejection. The publicly reproducible archive is a complete Python program; it does not import the Experiment 048 unpublished test code.

The mechanism is *conditional*: a trusted public-key roster, trustworthy pinned anchor, secure non-equivocation behavior and certificate dissemination are assumptions **not** obtained merely by checking a signature.

## Findings, counterexamples and falsifications

1. **Conflicting signatures:** Two different checkpoints for the same ledger, epoch and height, signed by sets ABC and ABD, both pass standalone 3-of-4 cryptographic signature verification. If A and B keep correct non-equivocating signing state, the second certificate cannot be created under the assumed f <= 1 model; deliberately bypassing their refusal defeats that property. The experiment demonstrates the necessity of the signer-discipline assumption rather than proving it holds in reality.
2. **Weak quorum:** Sets AB and CD can sign different checkpoints under q=2 without sharing any signers. Their intersection size is zero. For n=4, q=3, two signer sets must intersect in at least 2. An authenticated roster plus at most one equivocator is still an assumption, not a measured fact about independent people.
3. **Roster-origin attack:** A self-consistent attacker-controlled alternate roster produces valid synthetic signatures. The certificate fails once the verifier compares its roster against the *independently supplied* trusted roster digest. A hash stored beside its own roster is not an independent trust anchor.
4. **Rotation and rollback:** A domain-separated rotation record signed by an old-roster quorum can bind a replacement roster and epoch to an existing checkpoint. Missing prior consent, altered successor roster, wrong previous anchor, replayed epoch, reused signature domain, unsigned epoch jump, and cross-epoch signer substitution reject in the tested model. This does not verify a real key owner's identity, protect actual private keys, or prove reliable dissemination.
5. **Evidence admission:** A signature authenticates bytes relative to an assumed key roster, not the accuracy of a claim contained in those bytes. A trusted checkpoint in one observer's view does not detect a conflicting history withheld from that observer; evidence of conflict requires both records to become visible.

The local harness passed **46/46 named controls**. Negative control PASS means a malicious or malformed input was *correctly rejected*, not that it was accepted. Fixture SHA-256 identities and the source hashes are in the attached public JSON receipt.

## Complete categorized hash/provenance structure (scope of this 049 handoff)

### Original kernel and canonical root

- Original unmodified historical 0/U/1 kernel SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` — **inherited historical exact-byte reference only; not freshly rehashed here**.
- `eternalimit/clarity` `REIK_ROOT.md` Git blob **SHA-1** `f6cf9d97ab2be5322336857b7624978acec75f51` — Git metadata identity, not kernel SHA-256.
- Canonical admission: `K = R AND I AND E` where R is Reality, I Inference, and E independent Echo. No E, no admitted K.

### Separate and non-merged Experiment 030 / 031 manifest histories

- **030 / 280 events:** manifest SHA-256 `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`.
- **030 / 282 events:** manifest SHA-256 `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`.
- **031 / 290 events:** manifest SHA-256 `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2`.
- **031 / A-294 events:** manifest SHA-256 `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`.
- **031 / B-294 events:** manifest SHA-256 `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`.
- All five hashes are **historical references from prior 048 audit/paper**, not 049 original-byte replays. No cross-lineage parent substitution or merge.

### Other inherited exact-archive references (not embedded)

- Experiment 035 ZIP historical SHA-256: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Experiment 036 ZIP SHA-256 reference: `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`.
- Experiment 036 manifest SHA-256 reference: `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749`.
- Experiment 036 354-event receipt tip SHA-256 reference: `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0`.

### Confirmed public Git identities

- Experiment 047 source Git blob **SHA-1** `81dadc9ea206f1b57a12a25e8bd26da70edf424c`.
- Experiment 048 public parent commit `a0102fd8320aa8f5ea267ce48f57c740068cf600`; audit Git blob **SHA-1** `efc0bf64620e5a14d969c8b50e3b0572b18b701a`; paper Git blob **SHA-1** `73f98e70598cb378cdb13e5e038da546015d7c47`. GitHub compare to `b57b6d1...` returned **ahead=1, behind=0**, with the two expected 048 files.
- The original complete Experiment 048 verifier SHA-256 `c773990802be8c7220329b89ccc2a74350f49f1757e5de4dd1fe31f961bdcc4` and local audit SHA-256 `6dcc8d3b252edd33c13b98de298cb003ec6e5fc75b1fa9e3420fece23a93231f` remain historical **unuploaded local-file references**, not reproducible from the public 048 commit.

### Newly locally rehashed Experiment 049 bytes

- Full executable Python source SHA-256: `bcfc799cca8c9993beafa41ba51cc250e9f8d1f039001c146d5e4fb6b1709444`.
- Deterministic gzip source archive SHA-256: `5dbc2013678e00714bb2ed8f0a8e7f89c136544dd7b0a01edabfdda0cf124bc6`; independently matched Git object **blob SHA-1** `6792f8f7098a0ea2a776997a0fa42eec8435c646` upon GitHub object upload. Git blob SHA-1 and file SHA-256 are separate digest types.
- Full local execution receipt JSON SHA-256: `a551a1118ce61f9b8685ef6d1414fd5ca741cff5a95497a896fecbc9850ca4fb` — **not uploaded**. Public compact audit documents key facts; running the uploaded source recreates the output.
- Synthetic checkpoint/roster/rotation SHA-256 digests are in the public audit, explicitly **not** proof of real-world identity or physical history.

## FIDELITY / preservation

**Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty** remain mandatory. Original kernel unchanged, independent Echo pending. Preserve all previous negative controls and the separate 030/031 histories; **DROP U**, **0 · HOLD** for claims requiring missing evidence.

## Unresolved gates and Experiment 050 design

The program cannot show that four credentials belong to different people, that a root of trust was independently obtained, or that conflicts were actually disseminated between external operators. Experiment 050 should first arrange source review and a reproducible external run by an independent person/environment, with separate pinned trust provenance and independent cryptographic implementation. Then test withheld-fork detection across two real receivers, authorized roster rotation with operator identities, and key compromise/recovery. Publicly verified receipts should include independently obtained source hashes, executable/version hashes, explicit adversarial runs and failures. **Never infer that GitHub publication, synthetic signatures, OpenAI agreement, or mathematical plausibility constitutes external scientific Echo.**

**No evidence of solved P versus NP, Clay Millennium problems, universal physical inheritance, Clarity Pi semantic correspondence or independently authenticated external adoption is claimed.**
