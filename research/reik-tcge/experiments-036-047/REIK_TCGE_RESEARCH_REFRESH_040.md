# REIK/TCGE Experiment 040 — Typed Product-State Evidence Audit

**Research attribution:** Richard Stein / Clarity / REIK/TCGE  
**Date:** 2026-10-10  
**Classification:** Public-safe bounded research paper and audit receipt  
**Canonical admission state:** **0 · HOLD**; DROP U; independent Echo required.

## Abstract
The immutable REIK/TCGE `kernel001.py` evaluates whether a Boolean CNF is falsified (`0`), unresolved (`U`), or satisfied (`1`) under a partial assignment. The separate Clarity Pi / REIK evidence overlay classifies a claim as ADMITTED, REFUTED, or HOLD using direct evidence, inference, independent Echo, and admissible falsification. This study independently rehashes the original kernel bytes, isolates its `partial_state` function without executing archived research scripts, and exhaustively checks a **3 × 64 = 192** product-state model. Every kernel state admits multiple evidence-overlay outcomes. Therefore a mapping based only on the three computational labels cannot implement the six-input evidence-overlay classification. The study does **not** prove that no richer typed correspondence exists.

## Source-byte provenance and reproducibility
- Exact archived Experiment 035 ZIP rehashed SHA-256: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Exact original `kernel001.py` bytes extracted from the nested archive and rehashed SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Isolated `partial_state` function was called for three source-level test cases. No archived `main()` or research script was executed; no original kernel bytes were changed.
- Independent local verifier `reik_typed_product_040.py` SHA-256: `8ade0c884f823ed5bc8351df2f6387b45721ca6786c15a3050bc03410180dde7`.
- Machine-readable receipt `reik_typed_product_040_receipt.json` SHA-256: `876003e00ab7f83f16514188d1fcdf4e769528ad99e40f256f12234c4f93632b`.
- Reproduce locally using the exact archived ZIP and the provided standalone verifier: `python reik_typed_product_040.py`.

## Model and proof obligation
The **canonical repository contract** states `K = R AND I AND E`; Echo must be independent. The **separate research-only overlay** uses six Boolean flags `R,I,E,D,F,A`, with `D` indicating verified Echo independence and `A` admissibility of falsifier `F`:

`K* = R AND I AND E AND D`, `Q = F AND A`.

The overlay yields ADMITTED for `(K*,Q)=(1,0)`, REFUTED for `(0,1)`, and HOLD for `(0,0)` or `(1,1)`. These are explicitly defined **overlay** semantics, not original kernel outputs.

**Proposition (state-only correspondence obstruction).** There is no function `g:{0,U,1} -> {ADMITTED,REFUTED,HOLD}` that equals the defined overlay verdict for every evidence context paired with a given computational state.

**Proof.** Fix a kernel output `U`, e.g. original `partial_state([[1]],[None]) = U`. Evidence flags `(R,I,E,D,F,A)=(0,0,0,0,0,0)` yield HOLD. Flags `(1,1,1,1,0,0)` yield ADMITTED. If a state-only `g` matched both, `g(U)` would equal both distinct values, impossible. The same reasoning applies to any fixed kernel output. QED. This proof is conditional on allowing both evidence contexts for the same computational state; a claim-specific correspondence would need additional restrictions and typed source/evidence bindings.

## Independent bounded results
The source-byte isolated kernel yielded `0`, `U`, and `1` for one-clause CNF `[[1]]` under partial assignments `[False]`, `[None]`, `[True]`. The independently implemented evidence overlay and a separate four-row truth-table oracle agreed on all 64 evidence contexts. Across 192 product states, for **each** kernel state there were 3 ADMITTED, 15 REFUTED, and 46 HOLD verdicts. Eight named evidence-negative controls passed; source-byte mutation controls rejected altered archive/kernel digests.

This establishes bounded consistency of the product construction, not equivalence to the original kernel's full execution, external scientific Echo, or a solution to a Millennium Prize Problem.

## Historical SHA-256 lineages (do not merge)
- Experiment 030 / 280-event manifest: `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`.
- Experiment 030 / 282-event manifest: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`.
- Experiment 031 / 290-event manifest: `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2`.
- Experiment 031 / 294-event variant A manifest: `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`.
- Experiment 031 / 294-event variant B manifest: `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`.
- Experiment 036 ZIP historical reference: `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`; original Experiment 036 ZIP was **not acquired or rehashed** in this refresh.

## FIDELITY, external admission, and uncertainty
Eight standing principles: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. The public REIK root is `https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md` (Git blob `f6cf9d97ab2be5322336857b7624978acec75f51`). `sqrt(pi)/sqrt(pi)=1` is exact arithmetic but not evidence admission. The canonical kernel is unchanged; independent third-party Echo is not established.

The externally published `queens16.cnf` remains a bounded 256-variable SAT example but is not strict 3-CNF. No independently sourced original-byte 256-variable UNSAT file with independently checked proof was acquired. The Debian CaDiCaL `2.1.3-3` AMD64 publisher **expected** package SHA-256 is `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`; a fresh network download attempt failed, so no actual package or executable digest and no solver execution are claimed. No attributable third-party adoption of REIK/TCGE was established.

## Conclusion and continuation
The verified new result is a bounded typed product-state obstruction to **state-only** knowledge admission. A richer, provenance-preserving formal correspondence remains open. Preserve `0 · HOLD` and the distinct lineages. Next: acquire exact Experiment 036 original bytes and an external 256-variable UNSAT DIMACS/proof pair, check a pinned dedicated solver and independent proof checker, and formalize typed claim/evidence constraints before asserting equivalence. Publish only materially new verified public-safe evidence, with GitHub read-back.
