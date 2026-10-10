# REIK/TCGE Research Refresh 043 — Causal Provenance Is Not a Hash Chain

**Research attribution:** Richard Stein  
**Date:** 2026-10-10 (UTC)  
**Status:** Locally verified bounded falsification and proposed correction; scientific Echo and external admission **0 · HOLD**.

## Abstract

A read-only audit of the separate Experiment 042 synthetic evidence-ledger verifier identified a precise chronology gap. Its SHA-256 receipt-chain validator detects mutation, truncation, and reordering relative to a recorded tip, but it does not enforce that an inference references an earlier observation or that an Echo references an earlier inference. Consequently, all six permutations of one observation, inference, and synthetic trusted Echo are accepted by the prior overlay as ADMITTED, and all six produce internally valid newly computed hash chains. A separate causal validator admits exactly one of those six orders and exactly two of 24 orders when a synthetic refutation is also present. Eighteen adversarial controls passed. A versioned synthetic trust policy illustrates that current admissibility can change after revocation without deleting the historical attestation.

## Provenance and method

- Original archived Experiment 035 ZIP exact bytes rehashed to SHA-256 `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Nested original `kernel001.py` exact bytes rehashed to SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`; not executed or modified.
- Prior separate Experiment 042 overlay script exact bytes SHA-256 `7f05f80b43c500f58f73e9d0e716139bbb358c6c29bc30228f241d14336d52db`. Only its original `ev`, `chains`, `verdict`, `chain`, and `verify` functions were isolated for the reproduction; its full script was not executed.
- New standalone verifier SHA-256 `710cf9fcf186183b3427ac03885ec99c2c431aab55dd41673854a864707de2e2`.
- New machine-readable receipt SHA-256 `fdf70a5dd4beb9e1f590d8443ad04a243c04fa0084fb6f23711125d471e37083`.

## Falsification result

Let `O` be an observation, `I` an inference referencing `O`, and `E` an Echo referencing `I`. The causal order must satisfy `O < I < E`. There are `3! = 6` permutations of these events, but only one meets both strict inequalities. The Experiment 042 `verdict` implementation first indexes all events by ID, so it can resolve forward references even if `E` occurs before `I` and `O`. Its receipt verifier only checks that the supplied event order hashes to its claimed tip. All six permutations were accepted as `ADMITTED` by the old synthetic verdict and all six newly computed hash chains verified. The new causal validator accepted exactly one.

For `O, I, E, F` with refutation `F` also referencing `I`, the necessary partial order is `O < I < E` and `O < I < F`. Exactly two of the `4! = 24` permutations meet this order; both passed, and the other 22 were rejected.

**Interpretation:** A cryptographically linked event sequence can be internally intact while causally invalid. Append-only hash integrity is not sufficient to establish source-reference chronology, external identity, independence, or the truth of an inference.

## Synthetic versioned-policy result

A fixture trusts actor `bob` for Echo and `carol` for refutation at epoch 0. A fixture policy revision at epoch 1 revokes `bob` but retains `carol`. In a correctly ordered observation/inference/Echo stream, the *conditional synthetic* verdict changes from ADMITTED to HOLD under the current policy after revocation. With a refutation also present, the verdict changes from conflict HOLD to REFUTED. The original Echo event remains in the append-only history. All 18 deliberately malformed causal, policy, or receipt cases were rejected.

This is **not** a real trust authority, digital signature, independent external Echo, or proof of scientific adoption. The revision is accepted by an explicit local fixture; its authority is an assumption. A production implementation would need authenticated policy issuers, revocation effective-time rules, proof of key control, replay protection, and independent attestations.

## Clarity Pi and original kernel obligations

The original partial-CNF `0/U/1` evaluator answers a computational clause-state question. The separate evidence-admission overlay answers a claim/provenance question. A sound bridge needs a typed claim identity, source-to-inference reference, authenticated and independent Echo, chronology, conflict retention, explicit policy epoch, and a proof of uncertainty/falsification preservation. The finite tests here do not prove this correspondence. The normalization identity `sqrt(pi)/sqrt(pi)=1` does not supply those missing semantic relations. The repository root retains `K = R AND I AND E`; actual external `E` remains unverified.

## Historical hash boundary

Keep distinct: Experiment 030/280 manifest `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`; Experiment 030/282 manifest `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`; Experiment 031/290 manifest `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2`; Experiment 031/294-A manifest `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`; Experiment 031/294-B manifest `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`. These are historical references, not freshly rehashed from the respective manifest bytes in this run. No lineages were merged.

Experiment 036 ZIP historical reference `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`; manifest `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749`; 354-event tip `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0`. Exact Experiment 036 ZIP bytes were not obtained or replayed in this run.

## External evidence boundaries

Previously verified 256-variable SAT `queens16.cnf` is not strict 3-CNF. No independently acquired fully active 256-variable UNSAT original bytes and independent accepted proof were acquired. Debian CaDiCaL 2.1.3-3 AMD64 has historical published package SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`, but two fresh package download attempts failed; no actual package bytes or executable were hashed or executed. No attributable external adoption was established. No P versus NP proof is claimed.

## FIDELITY and disposition

Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. All retained as governing requirements. The new synthetic policy and chronology test is an independent local implementation, **not independent scientific Echo**. **DROP U; external admission 0 · HOLD.**

## Continuation

Acquire the exact Experiment 036 archive, manifest, and 354-event chain and rehash original bytes. Extend the causal validator with cryptographically authenticated policy revisions, revocation effective times, signed Echo and independent identity checks. Acquire independently sourced fully active 256-variable UNSAT DIMACS and independent certificate, and the pinned Debian CaDiCaL 2.1.3-3 AMD64 package/executable with checksum and independent proof checking. Preserve original kernel, eight FIDELITY principles, and distinct 030/031 histories. Commit only material verified public-safe results with read-back.
