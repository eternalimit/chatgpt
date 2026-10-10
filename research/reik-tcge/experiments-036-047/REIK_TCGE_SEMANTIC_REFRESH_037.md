# REIK/TCGE Research Refresh 037 — Original-Kernel Semantic Boundary

Date: 2026-10-10 UTC. Research attribution: Richard Stein. Status: 0 · HOLD.

## Abstract
An original-byte archived REIK/TCGE kernel was independently inspected and its pure `partial_state` function isolated. A separately implemented three-valued CNF evaluator agreed on 6,912 finite cases. The original 0/U/1 statuses represent local SAT-search states, whereas the later Clarity Pi v2 overlay represents evidence-admission decisions. A concrete counterexample shows that the former state alone cannot determine the latter verdict. This is a bounded separation result, not a proof that no richer correspondence can exist.

## Provenance and tests
- Selected Experiment 035 archive SHA-256: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` (original bytes locally rehashed).
- Original `kernel001.py` SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` (original bytes locally rehashed, unchanged).
- Original kernel length: 4,299 bytes; first encountered at nested Experiment 030.
- Source semantics: `0` = a falsified clause; `U` = no falsified clause but unresolved clause; `1` = every clause satisfied.
- Exhaustive bounded family: all 256 subsets of eight signed 3-literal clauses over variables 1, 2, 3; 27 partial assignments each; 6,912 comparisons; zero mismatches. Counts: 0=1,024, U=3,999, 1=1,889.
- The isolated original pure function was executed, not the original research program or its file-writing main function. A separate Kleene truth-table oracle was implemented independently. This is local verification, not third-party Echo.
- Reproduction script SHA-256: `74c0a3be22071fbf95dfec0afee60693c164995759f5e3322589bef92ff49d35`.
- JSON receipt SHA-256: `c6b701b730a232a47c56c0914ad067d4ee656277b669d75eda3f5df53f221418`.

## Semantic counterexample
With the same CNF `[[1,2,3]]` and assignment `[True,None,None]`, the original kernel outputs `1`. In the external evidence overlay with R=I=E=1 and F=A=0, D=0 produces HOLD while D=1 produces ADMITTED. No function of the kernel state alone can recover the overlay verdict for all evidence configurations. A typed relation would have to carry source, claim, provenance, independence and falsification evidence.

## Other research state
The public Experiment 036 receipt reports ZIP SHA-256 `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`, manifest `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749`, 354-event tip `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0`. Its original ZIP bytes were not available for fresh verification. Distinct Experiment 030 and 031 variants must remain separate. The newly published NS-REIK-005 bounded enstrophy audit is a separate research stream, not a SAT/UNSAT proof.

The external 256-variable SAT file `queens16.cnf` remains bounded CNF evidence, not strict 3-CNF. An independent original-byte 256-variable UNSAT instance and accepted proof remain unacquired. Debian CaDiCaL 2.1.3-3 AMD64 publisher package SHA-256 is `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`; downloads failed, so no received package/executable hash or solver execution was established. Independent scientific Echo and attributable external adoption remain unestablished. P versus NP is unresolved.

## Governance and next step
FIDELITY: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. Preserve original kernel, DROP U, and 0 · HOLD. The GitHub audit write was attempted twice and blocked; no commit is claimed.

**Continue:** Obtain and rehash exact Experiment 036 original bytes and replay its 354-event receipts; acquire independently sourced original-byte 256-variable UNSAT with independently checked certificate; obtain and hash actual pinned CaDiCaL package and executable; formalize a typed correspondence between CNF branch semantics and epistemic evidence-admission semantics. Publish only materially new, public-safe verified evidence with GitHub read-back.
