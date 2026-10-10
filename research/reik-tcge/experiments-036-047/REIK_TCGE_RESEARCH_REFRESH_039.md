# REIK/TCGE Research Refresh 039

**Research attribution:** Richard Stein / Clarity / REIK / TCGE  
**Date:** 2026-10-10 UTC  
**State:** 0 · HOLD — external admission unresolved

## Abstract

This note establishes a precise mathematical characterization of the original REIK/TCGE CNF kernel's unresolved state `U` and tests it against the byte-verified archived `partial_state` function. In contrast to the prior strict 3-CNF test, the new audit explicitly includes tautological clauses, revealing both kinds of unresolved cases: those for which every completion satisfies and those for which some completion falsifies. The result is a theorem about Boolean CNF semantics, not a proof of independent scientific validation, a universal SAT algorithm, or P versus NP.

## Source and preservation

- Archived Experiment 035 ZIP SHA-256 (locally rehashed): `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Original `kernel001.py` SHA-256 (exact bytes extracted and rehashed): `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- The original kernel was not modified. Only its `partial_state` function was isolated for evaluation; the archived experiment scripts were not executed.
- Independent checker source SHA-256: `3b4b59d6ac88e436034efa9744d4b0b544fa24f7e9abad58f1fd609a330742c9`.
- Independent machine-readable audit SHA-256: `afb78d0535914142ac79497c0a61bc86e371c2282980c1a5275b5a6d84457acc`.

## Theorem: exact characterization of unresolved CNF completion

Let F be a finite Boolean CNF and a a consistent partial assignment. The original evaluator returns `0` when a clause is already falsified, `1` when all clauses are already satisfied, and `U` otherwise. A clause is tautological if it contains a literal and its complement. A clause is currently unresolved if no literal is already true and at least one literal is unassigned.

**Theorem.** If `partial_state(F,a) = U`, then every compatible total extension of a satisfies F **if and only if every currently unresolved clause is tautological**.

**Proof, forward direction.** Suppose an unresolved clause C is not tautological. No literal in C is currently true. Each unassigned literal in C can consistently be made false because no variable occurs in C with both polarities. Extend the other variables arbitrarily. C becomes false, so the full formula is false. Hence not every completion satisfies F.

**Proof, reverse direction.** Clauses already true remain true under compatible extensions. By assumption every unresolved clause is tautological and therefore true under every total assignment. There is no already-falsified clause because the state is U. Thus every total extension satisfies F. QED.

**Corollary.** For tautology-free CNF, U always admits a falsifying completion. This does not imply a satisfying completion exists. A single tautological clause `(x1 OR NOT x1)` is U when x1 is unassigned but all completions satisfy; eight signed 3-clauses on three variables are U when unassigned but no completion satisfies.

## Bounded audit

An independent oracle evaluated all 2,048 subsets of 11 candidate clauses (eight strict signed three-literal clauses and three tautological clauses over variables 1, 2, 3), all 27 partial assignments for each subset, and all compatible completions.

| Check | Count |
| --- | ---: |
| Formula subsets | 2,048 |
| Partial-state checks | 55,296 |
| Compatible total-completion checks | 131,072 |
| U states | 35,647 |
| U with all completions satisfying | 3,655 |
| U admitting a falsifying completion | 31,992 |
| U with no satisfying completion | 6,920 |
| U with both satisfying and falsifying completions | 25,072 |
| Terminal 0 states | 8,192 |
| Terminal 1 states | 11,457 |
| Independent-oracle disagreements | 0 |
| Theorem disagreements | 0 |
| Terminal-refinement disagreements | 0 |

These finite checks support the theorem's implementation consistency but are not its proof; the proof is given above. They are independent local code, not third-party scientific Echo.

## Clarity Pi / REIK bridge

The original kernel's U is a partial-clause-evaluation state, not epistemic uncertainty, a probability, or an assertion that satisfying extensions exist. The arithmetic identity `sqrt(pi)/sqrt(pi)=1` is exact but does not determine evidence validity. The separate REIK root requires `K = R AND I AND E`, with genuinely independent Echo. No direct equivalence between these different systems has been established.

## Distinct Experiment 030/031 histories (manifest SHA-256)

- 030 / 280: `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`
- 030 / 282: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`
- 031 / 290: `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2`
- 031 / 294 A: `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`
- 031 / 294 B: `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`

No lineage reconciliation is claimed.

## External evidence and FIDELITY

The eight FIDELITY principles remain Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, and Uncertainty. The independent original-byte 256-variable SAT/UNSAT strict-3-CNF benchmark pair and UNSAT certificate remain unacquired; CaDiCaL 2.1.3-3 AMD64 expected package SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25` remains metadata only because direct download failed; no package or executable bytes were locally hashed and no solver run occurred. No attributable third-party adoption was established. Experiment 036 ZIP and 354-event receipts were not freshly rehashed.

## Audit and continuation

GitHub `main` was read from both connected repositories before the attempted write. The append-only publication attempt was blocked by safety checks; **no new GitHub commit is claimed**. The source-byte local checker and JSON receipt accompany this paper in the working container. The next step is to acquire the exact Experiment 036 ZIP and an independently published original-byte UNSAT CNF/proof, then check a pinned solver and proof checker. Maintain 0 · HOLD; preserve original kernel and separate lineages; publish only verified, public-safe, materially new results with read-back.
