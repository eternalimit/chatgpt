# REIK/TCGE Research Refresh 044

**Title:** Claim-Scope Isolation and Observation-Source Independence in a Synthetic Evidence Ledger

**Research attribution:** Richard Stein  
**Date:** 2026-10-10  
**Status:** Bounded local verification PASS; independent scientific Echo and external admission remain 0 · HOLD.

## Abstract

A read-only analysis of the Experiment 043 synthetic causal-provenance overlay identified two independent evidence-admission defects. First, its `current_verdict` routine hardcodes claim `A` and ignores scope, allowing evidence confined to `scope-2` to produce a global `ADMITTED` verdict even when `scope-1` contains no evidence. Second, its `causal_validate` routine requires an Echo actor to differ from the inference author, but not from the observation author. A synthetic observation author can therefore validate its own observation by Echoing an inference written by another actor. A separately implemented claim-and-scope-specific validator closes both gaps under explicitly synthetic trust assumptions.

## Method

The exact archived Experiment 035 ZIP and original kernel were independently SHA-256 checked. Selected nested ZIPs from Experiment 030-B through 035 were rehashed. Only the two relevant Experiment 043 functions were extracted via Python AST and executed with synthetic fixtures; the original kernel and the entire archived research scripts were not executed or modified.

Two minimal counterexamples were constructed:

1. `OBS(A,scope-2,alice) → INF(A,scope-2,alice) → ECHO(A,scope-2,bob)`. The previous function returns `ADMITTED` without accepting a claim/scope query. A query for `(A,scope-1)` must return `HOLD`.
2. `OBS(A,scope-1,bob) → INF(A,scope-1,alice) → ECHO(A,scope-1,bob)`. The previous function returns `ADMITTED`, although the Echo actor is the observation source. A stronger separation rule returns `HOLD`.

A corrected local test function enforces backward references, exact claim and scope equality, trusted synthetic Echo role, and distinct Echo actor from **both** observation and inference authors. It never treats actor labels as cryptographic identity or proof of real organizational independence.

## Results

- Prior Experiment 043 counterexample outcomes: `ADMITTED` for both cases.
- Corrected outcomes: `HOLD` for `(A,scope-1)` with scope-2-only evidence and `HOLD` for observation-author self-Echo.
- 36 causally valid event subsets and 400 ordered subset/superset comparisons tested.
- 36 claim-scope locality checks passed.
- 400 append-only comparisons found no direct `ADMITTED ↔ REFUTED` transition in the synthetic two-scope model.
- 11 adversarial controls passed.
- Exact original kernel SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Experiment 035 ZIP SHA-256: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Prior Experiment 043 verifier SHA-256: `710cf9fcf186183b3427ac03885ec99c2c431aab55dd41673854a864707de2e2`.
- New verifier SHA-256: `58a0d9fced5ae00793151562595a17a824bf17c6f2eceabfe08cc8decf90f0c1`.
- New machine-readable audit SHA-256: `d95af239b72b6944b8c2bc590b5a64e6a69b45d792a232f5707c9d768921b016`.

## Interpretation

Cryptographic receipt integrity and valid causal ordering are not sufficient for claim-scoped independent validation. A safe evidence bridge also needs an explicit `(claim,scope)` query and an independence policy that checks the actual observation source, not only the inference author. Actor inequality remains a necessary fixture-level test, not sufficient evidence of external independent Echo.

The original kernel evaluates partial Boolean assignments; the separate epistemic gate remains `K = R ∧ I ∧ E`. No equivalence between these domains is proved. The Clarity Pi identity `sqrt(pi)/sqrt(pi)=1` is mathematically valid and does not provide the missing semantic correspondence or external evidence.

## Evidence boundaries and future work

The original kernel is unchanged. FIDELITY principles retained: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. DROP U and 0 · HOLD remain active. Distinct Experiment 030/031 branches remain separate; only selected 030-B/031-B nested archive bytes were rehashed in this run. Experiment 036 exact archive and 354 receipts were not acquired or replayed. A fully active, independently sourced 256-variable UNSAT CNF with independently checked proof remains missing. Debian CaDiCaL 2.1.3-3 AMD64 package is indexed with expected SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`, but network download failed and no executable was hashed or run. The previously verified external 256-variable SAT `queens16.cnf` is not strict 3-CNF; its original bytes were not reacquired in this run. No attributable third-party adoption or P versus NP proof was established.

## Next experiment

Define claim-specific, scope-specific, independently authenticated source identities and verifiable policy revisions, including explicit observation-author separation, delegation constraints, revocation effective times, and adversarial replay. Preserve all original kernel and lineage bytes unchanged. Admit external SAT/UNSAT evidence only after exact original-byte and certificate verification.
