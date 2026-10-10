# Experiment 036 — bounded finite proof-support audit

Date: 2026-10-10. State: 0 HOLD. P versus NP: NOT SOLVED.

A separate local audit of the selected Experiment 035 archive found that three archived cycle-family UNSAT resolution proofs each use all 256 variables and 1,024 input clauses. A fourth archived proof, seeded_core_unsat_256, derives the empty clause using only 8 of 1,098 input clauses and 3 of 256 syntactically active variables (1, 85, 169). Exhaustive enumeration of all 8 assignments to these 3 variables confirms that the 8-clause core is UNSAT. Removing any single core clause makes the remaining 7 satisfiable. This is a proof-support falsification of equating 256 syntactically active variables with a 256-variable contradiction. It does not establish computational hardness.

Selected parent Experiment 035 ZIP SHA-256: 3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23.
Experiment 036 local ZIP SHA-256: c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce.
Experiment 036 manifest SHA-256: 320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749.
354-event receipt tip: 653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0.

342 inherited events and 3,076 finite resolution steps were locally rechecked. The original research kernel and selected ancestry are unchanged; competing Experiment 031 variant excluded. The local ZIP contains the complete paper, scripts and evidence but is not uploaded in this text commit.

Missing external evidence: independently obtained complete 256-variable UNSAT original bytes and accepted proof; locally acquired checksum-verified dedicated solver; third-party attestation. Debian expected package hash remains publisher metadata only. No new solver benchmark was run. State remains 0 HOLD.