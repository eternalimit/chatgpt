# REIK/TCGE Experiment 042 — Claim-Scoped Append-Only Evidence Semantics

**Date:** 2026-10-10 (UTC)  
**Attribution:** Richard Stein / REIK / TCGE  
**Classification:** Independent local implementation of a **synthetic** research overlay. Not a successor ZIP, third-party Echo, cryptographic signature, authenticated adoption, or a P versus NP proof.  
**Canonical state:** **0 · HOLD**.

## Abstract

Experiment 041 found that a six-Boolean evidence snapshot cannot, by itself, guarantee persistence of falsification when previously recorded facts can be deleted. Experiment 042 supplies a *separate* claim-scoped, append-only event representation and tests a more precise finite claim: under an append-only event set and a fixed, synthetic external-trust fixture, once an admissible refutation exists for a claim, adding events cannot erase the existence of that refutation. A different relational oracle confirms the claim-specific verdict function on 512 claim/subset combinations. Exhaustive tests cover 6,561 ordered subset/superset pairs, 40,320 permutations of eight synthetic events, and 4,096 cross-claim locality comparisons. Sixteen tampering and admission controls are rejected. The original archived kernel bytes were independently rehashed but never executed or modified. This is a **bounded software-model result**, not proof of actual independent Echo or equivalence to the original kernel.

## Research question and distinction

Can a proposed evidence ledger make **falsification persistence**, **non-expansion across claims**, **chronological tamper detection**, and **independent Echo admission** explicit without rewriting the original REIK/TCGE 0/U/1 CNF kernel?

The original kernel evaluates Boolean CNF formulas under partial assignments. The separate canonical REIK root defines `K = R AND I AND E`, where `E` must independently validate the inference. The v2 Clarity Pi overlay defines conditional support and refutation flags. This study does **not** identify those three different systems as the same semantics.

## Defined synthetic event model

An event contains a unique identifier, type (`OBS`, `INF`, `ECHO`, `REFUTE`), exact claim identifier, scope, actor label, typed references, and payload SHA-256. A claim can obtain a *synthetic conditional* positive chain only when its observation, inference and Echo records have matching claim/scope and explicit references, the Echo actor differs from the inference author, and a **separate** fixture permits that actor to act as an Echo for that claim. A similarly validated refutation forms a negative chain. An event cannot grant its own actor permission merely by setting a field on itself.

**Crucial limitation:** The external trust fixture is synthetic, not a signature verifier or real identity registry. Even a matching fixture entry is *not* independently established scientific Echo. The results test a proposed admission rule under assumptions; they do not validate any real-world assertion.

For each claim `c`, let `P_c(S)` denote existence of a complete admissible positive chain in event set `S`, and `F_c(S)` existence of a complete admissible refutation chain. The proposed research-only verdict is:

- `ADMITTED` iff `P_c(S)` and not `F_c(S)`;
- `REFUTED` iff `F_c(S)` and not `P_c(S)`;
- `HOLD` otherwise, including incomplete or conflicting evidence.

**Falsification-persistence lemma (fixed trust fixture):** If `S ⊆ T` and `F_c(S)` is true, then `F_c(T)` is true. **Proof:** The finite records witnessing `F_c(S)` are members of `S`, and hence members of `T`; no record is deleted. The same observation applies to `P_c`. Consequently, no append-only successor with a persisting admitted falsifier can be `ADMITTED` under the defined verdict. This does not prove that a refutation is scientifically valid, and it does not handle external revocation of a verifier's trust status; a real system needs a versioned, independently authenticated trust policy.

**Claim-locality lemma:** If a change adds only events that cannot satisfy any admissible chain for claim `c`, then the verdict for `c` is unchanged. The experiment tests this for changes affecting only the distinct claim B while evaluating claim A. Hash-chain tips, however, are *order-sensitive*, even when the semantic verdict is order-insensitive.

## Original source-byte integrity

From the attached original Experiment 035 ZIP, the verifier independently recomputed:

| Artifact | SHA-256 | Result |
|---|---|---|
| Exact Experiment 035 ZIP bytes | `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` | MATCH |
| Original nested `kernel001.py` bytes | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` | MATCH |

Five nested ZIP hops were traversed to find the kernel. No archived source code was imported or executed. The script performs no writes to the original ZIP.

## Finite test results

| Check | Verified count / outcome |
|---|---:|
| Synthetic events | 8 |
| Ordered subset/superset pairs | 6,561 / 6,561 |
| Cases with a preexisting admitted falsifier | 243 / 243 preserved |
| Cross-claim non-promotion cases | 2,187 / 2,187 |
| Separately implemented relational-oracle comparisons | 512 / 512 |
| Claim-locality comparisons | 4,096 / 4,096 |
| Event permutations, invariant verdict | 40,320 / 40,320 |
| Tamper and admission negative controls | 16 / 16 rejected |
| Synthetic append-only SHA-256 receipt chain | PASS |

Conditional examples: complete positive evidence without refutation -> `ADMITTED`; independently permitted refutation without positive evidence -> `REFUTED`; both -> `HOLD`; self-Echo, wrong-claim Echo, and untrusted actor -> `HOLD`.

The event-receipt chain uses canonical sorted-key compact JSON for event hashing, then `SHA256(previous_tip_bytes || event_digest_bytes)` for the next tip. Its synthetic tip is:

`f8dd20bd09e7b1c06972f5359f8965c33d7934b7835397c32814220e4841774f`

**This is not part of any Experiment 030–036 historical receipt sequence.** It is a separate synthetic fixture. A SHA-256 chain does not establish a trustworthy timestamp, third-party identity, or independent verification.

## Script and receipt identities

- Verifier `reik_typed_ledger_042.py` SHA-256: `7f05f80b43c500f58f73e9d0e716139bbb358c6c29bc30228f241d14336d52db`.
- Local machine-readable receipt `REIK_TCGE_AUDIT_042.json` SHA-256: `f77a5445c83e964aef4441928a6c344b7b156b560e9d2351eace08a9f8e2b857`.
- To reproduce: place the original `millennium_reik_3sat_exp035.zip` next to the verifier and execute `python3 reik_typed_ledger_042.py` using Python 3.10+ standard library.

## Hash lineage preservation — no collapsing variants

| Lineage | Manifest SHA-256 | Receipt count |
|---|---|---:|
| 030 / 280 | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | 280 |
| 030 / 282 | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | 282 |
| 031 / 290 | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | 290 |
| 031 / 294-A | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | 294 |
| 031 / 294-B | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | 294 |

Experiment 036 remains **historical-reference only**: ZIP SHA-256 `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`; manifest SHA-256 `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749`; 354-event tip `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0`. The exact Experiment 036 ZIP was not acquired for this refresh.

## Independent external gates — HOLD

The published `queens16.cnf` source is a previously locally checked 256-variable SAT example, **not strict 3-CNF**. Its original source bytes were not newly acquired in this run. A genuine original-byte externally sourced fully active 256-variable UNSAT instance with independently checked proof is still missing.

The exact Debian CaDiCaL 2.1.3-3 AMD64 package is publicly indexed, but the download attempt failed. Its expected publisher SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25` is **metadata**, not a computed hash of received bytes. No executable digest or dedicated solver run was obtained. No independently attributable external REIK/TCGE adoption was found in the bounded public search. No full formal correspondence with the unchanged kernel was proved.

## FIDELITY, governance and conclusion

The eight principles remain Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, and Uncertainty. `DROP U` prevents promotion of unsupported claims but does not erase uncertainty or falsification from the audit. The actual REIK knowledge gate remains `K = R AND I AND E`; no real external Echo was verified here. No private data, signing material, deployment or Bitcoin anchor is involved.

**Conclusion:** The new local synthetic event model passes finite tests for append-only falsification persistence, claim isolation, tamper detection, and explicit independent-Echo gating **under a stated synthetic trust fixture**. Original kernel remains unchanged. External scientific admission: **0 · HOLD**.
