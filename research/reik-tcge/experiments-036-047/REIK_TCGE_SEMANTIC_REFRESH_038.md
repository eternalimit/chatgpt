# REIK/TCGE Research Refresh 038 — Refinement Stability and the Meaning of U

**Date:** 2026-10-10 UTC. **Attribution:** Richard Stein. **Admission:** 0 · HOLD.
**Status:** New bounded local verification, not a third-party independent scientific Echo, original-kernel rewrite, or P-versus-NP result.

## Abstract
This study examines the immutable REIK/TCGE partial-CNF evaluator's three outputs under extensions of partial assignments. Using the original `kernel001.py` bytes recovered from the exact locally available Experiment 035 ZIP, the isolated `partial_state` function was tested on all 256 subsets of eight signed three-literal clauses over three variables and all 27 partial assignments per subset. The study checked all 16,384 compatible total completions with a separately implemented direct satisfaction oracle. All 3,976 terminal-state refinement comparisons passed. A new falsification control identifies 865 partial states labelled `U` for which no satisfying completion exists in this bounded family. Thus `U` describes locally unresolved clause evaluation, not a guarantee that a satisfying completion exists.

## Source-byte provenance
- Exact locally hashed Experiment 035 ZIP SHA-256: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Exact locally hashed archived original `kernel001.py` SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` (4,299 bytes; no edits).
- Exact locally hashed new verification script SHA-256: `b15f3d1ba8d9114202f343de861bd6bc2aae67c81e3140ad33faed85546a9e2b`.
- Exact locally hashed new JSON receipt SHA-256: `4b8e657235125bf744761982f2f65de525d13e365ca4dba8b6a814795d6f80fe`.
- Experiment 036 ZIP `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`, manifest `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749`, and 354-event receipt tip `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0` remain **historical public-record references only**; exact 036 bytes were not available here.

## Method and bounded results
The original source program was not executed wholesale. Its pure AST function `partial_state` was isolated and run against a separately coded direct Boolean satisfaction oracle on full assignments. The bounded test enumerated all 6,912 formula/partial-assignment pairs and all 16,384 compatible full completions. All 16,384 full-assignment checks agreed with the independent oracle. Among 3,976 checks where the partial state was terminal (`0` or `1`), **zero** completion states disagreed. The original function's local terminal statuses are therefore refinement-stable in the tested domain.

Of 3,999 `U` partial cases, **865** had no satisfying total completion and **3,134** had both satisfying and falsifying completions. No `U` case had every completion satisfying in this specific restricted non-tautological family. A separate tautological clause `[[1,-1]]` returns `U` with `x` unassigned although every full assignment satisfies it; this is an explicit example outside strict 3-CNF. The strict 3-CNF consisting of all eight sign patterns on variables 1, 2, 3 returns `U` with all three variables unassigned, although all eight total assignments falsify at least one clause. Therefore `U` is not equivalent to semantic SAT uncertainty. It is a local partial-evaluation status.

## Semantic and epistemic interpretation
Original kernel: `0` = a currently falsified clause; `U` = no currently falsified clause but at least one unresolved clause; `1` = every clause already satisfied. This computational classification is not the separate REIK knowledge-admission classification. The canonical root is `K = R AND I AND E`, with **E** requiring independent validation. The Clarity Pi Math overlay adds typed evidence/provenance conditions; no general correspondence to the original immutable source kernel has been proved. `sqrt(pi)/sqrt(pi)=1` is a mathematical normalization identity and not evidence of independent Echo.

## Lineage non-equivalence and governance
Do not merge Experiment 030 parent histories (280 versus 282 events), or Experiment 031 successors (290 versus two distinct 294-event histories). Preserve the eight FIDELITY principles: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. DROP U means no unsupported evidence promotion, not deletion of uncertainty from audit records. Remain at **0 · HOLD**.

## External admission gates
The public `queens16.cnf` remains a bounded independently sourced 256-variable SAT example but is not strict 3-CNF. No new independently acquired original-byte fully active 256-variable UNSAT instance plus independently checked proof was found. A third-party UNSAT repository (`tamas-schwarcz/mfmc`) publicly documents DRAT artifacts and manifests, but its Git tree does not contain the complete published CNF/proof archives; no eligible exact bytes were obtained. Debian lists `cadical_2.1.3-3_amd64.deb` and expected publisher SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`, but network/DNS restrictions prevented acquisition; no actual package/executable hash or solver run was obtained. No independent external adoption, proof of formal Clarity Pi/kernel correspondence, or P versus NP solution was established.

## Public publication receipt
Connected GitHub `main` read-back observed `eternalimit/clarity` at `8c1a51b62d462158c14d82bcf131ca20040e649e` and `eternalimit/chatgpt` at `d79546b52923526919e61b277361b72d00c377a9`. An attempted publication of the independently rechecked 037 semantic audit was **blocked by tool safety checks**; the subsequent 038 result was retained locally without attempting to bypass that block. No new GitHub commit is claimed. This local paper, verifier and JSON receipt are the durable artifacts of this run; they are not public GitHub records.

## Continue
Acquire and independently rehash exact Experiment 036 ZIP and replay its 354 receipts. Develop typed semantics distinguishing partial CNF evaluation, semantic SAT/UNSAT, and independently validated knowledge. Seek an independently sourced 256-variable UNSAT DIMACS/proof pair and an actually downloaded, rehashed CaDiCaL executable. Preserve original kernel and all separate histories; only publish materially new verified public-safe evidence with GitHub read-back.
