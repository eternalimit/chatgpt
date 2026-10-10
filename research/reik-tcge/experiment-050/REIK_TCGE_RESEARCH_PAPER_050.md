# REIK/TCGE Research Paper — Experiment 050

**Title:** Cross-implementation Ed25519 checks, synthetic fork dissemination and falsification of epoch-rotation validation  
**Attribution:** Richard Stein — REIK/TCGE (AI-assisted bounded research)  
**Date:** 2026-10-10  
**Parent public commit:** `43b684d4004d467a6b365d5958d5c1f1e1046f25` on `eternalimit/chatgpt/main`  
**Evidence state:** **0 · HOLD; DROP U** for external identity, independence, science, adoption and universe-wide claims.

## Abstract

We rehashed Experiment 049 archived Python source SHA-256 `bcfc799cca8c9993beafa41ba51cc250e9f8d1f039001c146d5e4fb6b1709444` and its gzip ZIP-like archive SHA-256 `5dbc2013678e00714bb2ed8f0a8e7f89c136544dd7b0a01edabfdda0cf124bc6`, independently decompressed the exact bytes, reexecuted the reported **46/46** software controls, and reconstructed the prior JSON receipt with the identical SHA-256 `a551a1118ce61f9b8685ef6d1414fd5ca741cff5a95497a896fecbc9850ca4fb`. Public parent commit and original source Git blob references were fetched from connected GitHub. A new, locally executed Experiment 050 harness (its source remains available as a conversation artifact, not uploaded in this GitHub commit) tests Ed25519 signatures with two locally executed code paths: Python `cryptography` and a separate *educational* pure-Python arithmetic verifier following RFC 8032. The mathematical reference was checked against official RFC 8032 known-answer vectors; the new program passes **44/44** named bounded tests.

More importantly, **three previously untested conditions are accepted by the inherited Experiment 049 `verify_rotation` function**: a prior-trust epoch inconsistent with the trusted checkpoint's epoch, a successor roster with only three identities under the declared four-witness policy, and a successor roster with two labels resolving to the same Ed25519 public key. A minimal **review-only** strict-guard wrapper rejects each malformed transition and still accepts a valid one. The inherited file remains immutable. These are local model validation gaps, not proof of an external exploit. Simulated fork gossip demonstrates that independently isolated receivers do not observe a contradiction unless a conflicting signed statement is delivered to them.

## Materials and reproducibility

Reproduce using the **exact** public Experiment 049 `reik_checkpoint_049.py.gz` and the locally generated Experiment 050 Python source (shared separately as a conversation artifact; not yet committed to GitHub). Install Python `cryptography==46.0.4` for precise reproduction; execute:

```sh
python3 reik_checkpoint_050.py --parent ../experiment-049/reik_checkpoint_049.py.gz --json > reik_checkpoint_050_result.json
sha256sum reik_checkpoint_050.py reik_checkpoint_050_result.json
```

Expected source SHA-256 `5146ca764051a463f8fb6f8da03c8537de9d29d3db46a952d8e88434ab150f13`; resulting JSON SHA-256 `2c19e37cabb8c122909cb7b4e4e659ea4b56fc7959454affdb9f2ce8ba69bc71`. No network, private keys, external services, or secret contacts are used by either experiment harness. All signing keys are deterministically generated *public test fixtures*, and both simulated receivers are controlled by this process. The new full JSON execution receipt is preserved as a separate conversation artifact but is not included in this GitHub commit. The original Experiment 048 complete local verifier also remains unavailable in public.

## Methods and primary falsification results

### Independent mathematical code path, not independent person

The second verifier implements Ed25519 point decompression, group arithmetic and signature equation separately from Python `cryptography`, and is checked against the RFC 8032 section 7.1 known-answer vectors for empty and one-byte messages. It then checks synthetically signed checkpoint payloads from both branches of a same-height fork. This narrows dependence on one implementation but **does not constitute separately sourced or independently operated cryptographic validation**. The educational reference is not hardened, audited, side-channel safe, or authorized for deployment.

### Previously missed epoch and key-roster consistency checks

**F050-01 (accepted invalid prior epoch):** `verify_rotation` in the archived 049 source trusts the signed rotation's new epoch relative to `anchor['epoch']`, but never checks `prior_trust.epoch == anchor['epoch']`. Passing an arbitrary prior trust epoch (99) into an otherwise signed epoch-2 rotation returns an accepted epoch-2 trust object. The review-only overlay rejects this.

**F050-02 (accepted undersized successor roster):** A valid old-roster quorum can authorize a successor with only three names under a policy explicitly declared as *three of four*. Archived `verify_rotation` accepts that successor; the later `verify_cert` explicitly rejects rosters whose length is not four. This inconsistency can produce a locally unusable rotated epoch. The review-only overlay rejects this.

**F050-03 (accepted duplicate successor key):** A roster with four different labels but two identical public key strings also passes the old rotation validator, allowing two apparent identities to collapse to one key. The 049 certificate verifier rejects duplicate keys at a later stage. The review-only overlay rejects this.

No live systems were targeted, breached, or contacted. These controls expose model-validation omissions, not credentials or private exploits. They are retained as falsification evidence; the existing 049 code is unchanged.

### Conflict dissemination and signer-state assumptions

Synthetic observer A receives a 3-of-4 certificate for tip X while observer B independently receives a 3-of-4 certificate for tip Y at the same ledger, epoch, and height. Each receiver sees **no conflict in isolation**. On receiving both conflicting certified records, each reports the conflict; duplicate and reversed deliveries do not suppress it. If a mock signer loses its locally stored prior-signing decision upon restart, it can sign a conflicting checkpoint again. A persistent state model vetoes this repeated but contradictory signature. These experiments do not establish reliable real-network gossip or real durable storage.

The experiment explicitly allows a single simulated controller to generate all four keys, demonstrating that signatures cannot, by themselves, prove four independent people, organizations or custodial systems. Roster pins remain supplied inputs, not independently authenticated public trust roots.

## Categorized hash and lineage structure (type, validation status)

### Historical immutable kernel — *reference, not rehashed today*

- Original unchanged 0/U/1 kernel SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Source bytes not available to this 050 execution. **Do not equate kernel historical reference with direct 050 authentication.**
- Canonical REIK contract `K = R AND I AND E`. E requires independent Echo; synthetic cross-checking is not external Echo.

### Preserved distinct 030/031 histories — *historical inherited digest references only*

- `experiment030_280_manifest_SHA256`: `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` — historical, not rehashed in Experiment 050.
- `experiment030_282_manifest_SHA256`: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` — historical, not rehashed in Experiment 050.
- `experiment031_290_manifest_SHA256`: `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` — historical, not rehashed in Experiment 050.
- `experiment031_A294_manifest_SHA256`: `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` — historical, not rehashed in Experiment 050.
- `experiment031_B294_manifest_SHA256`: `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` — historical, not rehashed in Experiment 050.
- `experiment035_ZIP_SHA256`: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` — historical, not rehashed in Experiment 050.
- `experiment036_ZIP_SHA256`: `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce` — historical, not rehashed in Experiment 050.
- `experiment036_manifest_SHA256`: `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749` — historical, not rehashed in Experiment 050.
- `experiment036_354event_receipt_tip_SHA256`: `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0` — historical, not rehashed in Experiment 050.

### Earlier public Git identities — *GitHub read-back; Git blob SHA-1 is not SHA-256*

- `REIK_ROOT_git_blob_SHA1`: `f6cf9d97ab2be5322336857b7624978acec75f51`.
- `experiment047_source_git_blob_SHA1`: `81dadc9ea206f1b57a12a25e8bd26da70edf424c`.
- `experiment048_commit`: `a0102fd8320aa8f5ea267ce48f57c740068cf600`.
- `experiment048_audit_git_blob_SHA1`: `efc0bf64620e5a14d969c8b50e3b0572b18b701a`.
- `experiment048_paper_git_blob_SHA1`: `73f98e70598cb378cdb13e5e038da546015d7c47`.
- `experiment049_parent_commit`: `43b684d4004d467a6b365d5958d5c1f1e1046f25`.
- `experiment049_python_gzip_git_blob_SHA1`: `6792f8f7098a0ea2a776997a0fa42eec8435c646`.
- `experiment049_audit_git_blob_SHA1`: `5ffc0b8962243bbb4739aa0ba3e12b75adaf27a6`.
- `experiment049_paper_git_blob_SHA1`: `13368716cb0147803daa5ec0f2f8f6ddf68d06a5`.
- `experiment049_readme_git_blob_SHA1`: `7b70b52c161055d5c25e11969e70f561e347e739`.

### New 049 and 050 exact-byte local verification — *direct SHA-256 checks*

- `049_original_gzip_SHA256`: `5dbc2013678e00714bb2ed8f0a8e7f89c136544dd7b0a01edabfdda0cf124bc6`.
- `049_unpacked_Python_SHA256`: `bcfc799cca8c9993beafa41ba51cc250e9f8d1f039001c146d5e4fb6b1709444`.
- `049_result_JSON_SHA256`: `a551a1118ce61f9b8685ef6d1414fd5ca741cff5a95497a896fecbc9850ca4fb`.
- `050_repro_source_Python_SHA256`: `5146ca764051a463f8fb6f8da03c8537de9d29d3db46a952d8e88434ab150f13`.
- `050_local_result_JSON_SHA256`: `2c19e37cabb8c122909cb7b4e4e659ea4b56fc7959454affdb9f2ce8ba69bc71`.


The original 048 complete verifier SHA-256 `c773990802be8c7220329b89ccc2a74350f49f1757e5de4dd1fe31f961bdcc4` and original 048 local audit SHA-256 `6dcc8d3b252edd33c13b98de298cb003ec6e5fc75b1fa9e3420fece23a93231f` are **unuploaded inherited references**, not replayed. Every hash is explicitly typed, and the historical 030/031 competing chains stay separate.

## FIDELITY preservation and limitations

The eight principles remain unchanged: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. No original kernel or earlier research file was modified. No synthetic signature or two-verifier agreement in one environment is externally authenticated Echo. The program has no true independent roster origin, verified real-world signing identities, key custody assurances, two independently operated receiving endpoints, actual adversarial network, RFC 9162 inclusion/consistency proofs, external scientific replication, physical observation, or demonstrated P-versus-NP solution. Trust in the parent GitHub identity also does not authenticate the historical authorship of arbitrary sources.

**Admission decision:** 0 · HOLD, DROP U. These finite tests support a bounded software/model claim and reveal inherited defects. They do not validate a universal physical law or external REIK adoption.

## Experiment 051: falsifiable next step

Have a *separately controlled* reviewer retrieve and hash 049 and 050 sources through a separate trust route, execute 44 new controls in an independent environment, and sign an attributable but non-sensitive reproducibility receipt. Test robust authorized epoch rotation with a formally specified trust and roster state machine; add true multi-process receiver gossip under withheld-message, partition, replay and signer crash/recovery scenarios; compare a second well-maintained crypto implementation; and independently verify third-party witness origin and autonomy. Preserve the three 049 failures as regression tests and keep claims on HOLD until actual external evidence is provided.

Reference: RFC 8032 (Ed25519 definition/test vectors), https://www.rfc-editor.org/rfc/rfc8032. RFC 9162 log consistency is potential future work, not implemented here.