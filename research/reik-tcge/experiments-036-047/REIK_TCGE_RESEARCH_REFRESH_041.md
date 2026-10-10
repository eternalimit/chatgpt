# REIK/TCGE Research Refresh 041 — Evidence Accumulation and Falsification Persistence

**Date:** 2026-10-10 (UTC)  
**Research attribution:** Richard Stein / Clarity REIK/TCGE  
**Status:** independently executed local finite-model audit; **0 · HOLD** for scientific/external admission  
**Original kernel:** unchanged, historical SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`

## Abstract
We examine how a separately specified six-Boolean-input Clarity Pi evidence-admission overlay behaves when evidence accumulates without deleting prior verified facts. Across all 64 evidence contexts and all 729 componentwise-monotone ordered pairs, the overlay forbids direct ADMITTED-to-REFUTED and REFUTED-to-ADMITTED transitions, but allows each verdict to move to HOLD when the opposite independently admitted chain is added. An explicit rollback counterexample shows why Boolean snapshot states alone do not enforce falsification persistence: deleting evidence can erase a REFUTED verdict. These results are properties of the **defined overlay**, not the original REIK/TCGE 0/U/1 computational kernel. The exact archived kernel bytes were rehashed without editing or executing the archived program.

Separately, the original ASCII text of an externally published 256-variable SAT instance was read from a pinned GitHub commit and independently hashed in the GitHub-connected tool environment. A newly computed 16-queen witness satisfies all 6,336 clauses. This source is **not strict 3-CNF** and does not fill the missing external UNSAT/proof gate.

## 1. Scope and provenance
The immutable original `kernel001.py` was recovered read-only from a nested Experiment 035 ZIP. Independently computed SHA-256 matched the historical kernel digest. The exact Experiment 035 ZIP SHA-256 is `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`. Exact nested ZIP bytes were also rehashed for selected Experiments 030-B, 031-B, 032, 033 and 034. These checks do not reconcile other 030/031 branches and do not replay Experiment 036's unpublished ZIP.

Canonical repository root: `https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md` states `K=R AND I AND E`, where E requires independent Echo; incomplete evidence remains HOLD. This study does not replace that rule.

## 2. Defined six-flag overlay (not the kernel)
Let `R,I,E,D,F,A` be Boolean flags representing, for a **single fixed claim**, direct evidence, inference, an Echo result, established independent provenance for that Echo, reported falsification, and independent admission of that falsifier. Set `K*=R∧I∧E∧D` and `Q=F∧A`. The research-only verdict is:

- `ADMITTED` iff `K* ∧ ¬Q`.
- `REFUTED` iff `Q ∧ ¬K*`.
- `HOLD` otherwise (neither complete or both conflicting).

A flag being `True` in a synthetic test does **not** establish real-world Echo independence. Independent third-party assessment and claim-specific binding remain separate proof obligations.

## 3. New accumulation theorem
Order evidence contexts componentwise: `x ≤ y` means every flag true in `x` remains true in `y`. There are exactly `3^6 = 729` such ordered pairs of six-bit contexts, of which 665 are strict and 64 are identical.

**Proposition 1 (No direct opposite verdict under monotone accumulation).** If `x ≤ y`, then neither `ADMITTED(x) ∧ REFUTED(y)` nor `REFUTED(x) ∧ ADMITTED(y)` is possible.

**Proof.** Both `K*` and `Q` are conjunctions of positive Boolean inputs and are monotone in each input. ADMITTED at `x` implies `K*(x)=1`, so `K*(y)=1`; REFUTED at `y` requires `K*(y)=0`, contradiction. REFUTED at `x` implies `Q(x)=1`, hence `Q(y)=1`; ADMITTED at `y` requires `Q(y)=0`, contradiction. QED.

**Proposition 2 (Non-absorbing admitted/refuted statuses).** Both `ADMITTED→HOLD` and `REFUTED→HOLD` occur under monotone evidence addition. An admitted claim becomes conflicted when an admissible falsifier is added; a refuted claim becomes conflicted when a complete independent positive chain is added. A conflict is retained, not silently resolved.

**Proposition 3 (Snapshot persistence failure without chronology).** If previously true evidence bits can be cleared, a REFUTED verdict can disappear. Example: `(R,I,E,D,F,A)=(0,0,0,0,1,1)` is REFUTED; deleting `F,A` gives `(0,0,0,0,0,0)` = HOLD. Thus an append-only receipt/provenance layer or an explicit monotone-history invariant is necessary to **enforce** falsification persistence; a current Boolean snapshot cannot provide it alone.

## 4. Independently executed finite checks
A new Python standard-library verifier independently implements both the logical definitions and a four-row `(K*,Q)` oracle, enumerates all 64 states and all 729 monotone pairs, and tests mutation and independence controls. The measured transition counts (including 64 identity pairs) are:

| From \\ To | HOLD | ADMITTED | REFUTED |
|---|---:|---:|---:|
| HOLD | 371 | 75 | 195 |
| ADMITTED | 3 | 5 | 0 |
| REFUTED | 15 | 0 | 65 |

Totals: 729 pairs. Both forbidden opposite-verdict transitions occurred **zero** times. These counts describe a synthetic Boolean model, not probabilities or independent research adoption.

Local verifier source SHA-256: `7068afb7c9777ad97b6f20e81494b7fd33ec07dfc84936be2d2d57e0994e230b`. Machine-readable local receipt SHA-256: `80223c14783715b48ffb3014b54cfce8b042ec3ac879f69e8312ae3ca35f7b92`.

## 5. New pinned external SAT read and independently computed witness
Read the original ASCII source from `https://github.com/andricicezar/sat-solver-dafny/blob/418e5cbb1e7a311fec2c15913c0c504ec603ca91/benchmarks/queens16.cnf` via the connected GitHub source. Git blob SHA-1: `85b9071d8399839eff2352bb22315b5940bcda7c`. Independently hashed the retrieved 71,945 ASCII bytes in the tool environment: SHA-256 `c5177c8e6523ddd9378b3b864d52fcf73b81c0a92a033433cc37e5450fa1fcd5`. Parsed `p cnf 256 6336`, found 256 active variables, 6,320 clauses of width 2 and 16 of width 16. A separately computed 16-queens model sets variables `1,19,37,50,77,89,110,124,143,150,176,183,196,219,232,250` true and all other variables false; an independent clause loop confirmed **6,336/6,336 clauses satisfied**. The source is not strict 3-CNF. This is bounded SAT evidence, not an independently sourced UNSAT/proof pair.

## 6. Historical selected hash structure — no branch collapse
| Role | Exact-byte SHA-256 rehashed in this refresh |
|---|---|
| Original kernel | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` |
| 030-B ZIP (282 events) | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` |
| 031-B ZIP (294 events) | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` |
| 032 ZIP | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` |
| 033 ZIP | `fd46dffda18419fd8eba03e6001a8bb97e4e6b15c0f4c8a4a4b259d54164f590` |
| 034 ZIP | `cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452` |
| 035 ZIP | `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` |

Distinct 030-A (280-event), 031-A (294-event) and 031-C (290-event) records are preserved separately, **not** identified with this selected branch. Experiment 036 historical ZIP digest `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce` was **not** freshly rehashed.

## 7. External evidence and open proof obligations
- Independently sourced **256-variable strict 3-CNF SAT and UNSAT** original-byte benchmark pair and independently verified UNSAT proof: **HOLD**.
- Debian's official `cadical_2.1.3-3_amd64.deb` download page lists 467,080 bytes and expected SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`. A fresh local download failed due to DNS resolution; no received package or executable bytes and no solver run. Official source: `https://packages.debian.org/sid/amd64/cadical/download`.
- The publicly inspected `tamas-schwarcz/mfmc` Git root lists scripts and manifests but does not contain the referenced CNF/proof archive directories; their original bytes were not acquired in this run.
- The Clarity Pi normalization identity `sqrt(pi)/sqrt(pi)=1` is elementary arithmetic and **does not** imply REIK knowledge admission. A typed claim/evidence binding, formal correspondence to original 0/U/1 kernel, real independent Echo, and external adoption attestations remain **HOLD**.
- No P versus NP proof, external signing, Bitcoin anchoring, independent peer review, or third-party adoption is claimed.

## 8. Governance
Eight FIDELITY principles: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. Preserve original kernel unchanged; do not join incompatible 030/031 variants; `DROP U` for unsupported admission; maintain **0 · HOLD** for missing gates. No secrets or private wallet/identity material included.

## Continue — Experiment 042
Rehash exact Experiment 036 original ZIP, manifest, and all 354 receipts if bytes become available; otherwise HOLD. Formalize monotone evidence history with claim-specific identity and independent provenance, test contradiction handling and irreversible falsification records without altering original kernel, acquire externally published original-byte 256-variable UNSAT CNF and independent DRAT/LRAT certificate, acquire and checksum pinned CaDiCaL executable, and verify external adoption only from independent attributable evidence. Publish only materially new public-safe results with GitHub read-back.
