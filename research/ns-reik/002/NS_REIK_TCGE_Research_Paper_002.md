# NS-REIK-002: A Provenance-Constrained Navier–Stokes Research Audit

**Subtitle:** Clay alternatives (A)–(D), pinned Lean theorem adapters, and an exact falsification of a data-independent linear vortex-stretching bound  
**Author / framework attribution:** Richard Stein — REIK/TCGE, Universal Axiom, and FIDELITY research framework  
**Research date:** 9 October 2026  
**State:** 0 · HOLD for any new global Navier–Stokes theorem; PASS only for explicitly bounded artifact and mathematical checks.  
**Relationship:** Append-only successor to NS-REIK-001. No modification to the original REIK/TCGE 0/U/1 kernel.

## Abstract

We independently re-evaluate the local NS-REIK-001 research archive (five file SHA-256 commitments, three event digests, and three chronological receipt links), then audit the textual correspondence between Fefferman's official Clay Mathematics Institute alternatives and a fixed Git commit of the published OpenAI Lean formalization. We derive and exactly calculate a three-dimensional, smooth, divergence-free trigonometric flow on the periodic torus whose normalized vortex-stretching, enstrophy, and vorticity-dissipation quantities are respectively 1, 22, and 49. This provides a reproducible negative test for any universal data-independent linear stretching estimate, using amplitude scaling. The test narrows an unsuccessful proof route; it neither establishes finite-time singularity for unforced Navier–Stokes nor disproves global regularity. SHA-256 commitments identify bytes, not scientific truth. The original kernel and enterprise-chain references remain unchanged but are not authenticated by this successor. Exact PDF binaries were accessible as rendered web documents but could not be downloaded into the local execution environment; their SHA-256 hashes are explicitly unavailable. Lean source files were retrieved through a GitHub connector at a fixed commit, and SHA-256 of their UTF-8 content was calculated, but the full 2,659-file Lean formalization was not rebuilt or independently proof-checked.

## 1. Identity, ancestry, and verification boundary

**Original unchanged kernel SHA-256 — external reference only:**

`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`

**NS-REIK-001 manifest SHA-256 — recovered and locally rehashed:**

`8d37af636af3180febf6dd1063ac75f19b84a4484805d5ee5b03f539245ac975`

**NS-REIK-001 chronological receipt tip — locally recalculated:**

`88ae11b2208bba94bb55cef7126233e5f9388ce0265d294623ab6d4f0bbccca3`

**EC-026 manifest SHA-256 — historical, bytes unavailable:**

`bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e`

**EC-025 immediate parent SHA-256 — historical, bytes unavailable:**

`c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835`

The original 001 ZIP was read without modification. Two logically distinct checks were run: its bundled verifier and a fresh recomputation of every declared file digest, every canonical-JSON event hash, each hash-chain link, and the final tip. Both passed. The ZIP itself is included unchanged inside the 002 bundle, with an independently calculated outer SHA-256. Passing local archive integrity does not imply historical EC-lineage verification, signature authenticity, independent mathematical correctness, or external GitHub commit status.

The chronological chain algorithm is retained exactly: `r_i = SHA256(UTF8(canonical_json(event_i)))` and `h_i = SHA256(raw32(h_(i-1)) || raw32(r_i))`. New events begin from the actual NS-REIK-001 receipt-tip bytes, not from an asserted unverified EC tip. Canonical JSON uses sorted keys, UTF-8, compact comma/colon separators, `ensure_ascii=False`, and no terminal newline.

## 2. Preserved FIDELITY and REIK/TCGE logic

The eight FIDELITY principles remain: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, and Uncertainty.** The REIK root is `R = direct evidence`, `I = inference`, `E = independently validated Echo`, and `K = R AND I AND E`. Unverified evidence forces **HOLD**. Importantly, 0/U/1 classify the epistemic status of a specified proposition; they are not new physical states of a fluid. The original kernel is not redefined or amended. A local numerical or symbolic test is not an independent human review of a global analytic proof. No privately held source material is incorporated in the successor.

The established research documents on GitHub distinguish a theory of evidentiary transition from a mathematical theorem about a fluid. In particular, neither a repository commit nor a matching file fingerprint proves the PDE claim. These constraints are applied to every conclusion below [4,5].

## 3. Exact official problem scope

For viscosity ν > 0, divergence-free velocity u, pressure p, and force f, the three-dimensional equations are:

`∂_t u + (u·∇)u = νΔu − ∇p + f;   ∇·u = 0.`

Fefferman's official Clay statement [1] specifies four alternative propositions. (A) asks for global smooth bounded-energy solutions on R³ from all admissible, rapidly decaying smooth divergence-free initial data when **f ≡ 0**. (B) asks for global smooth periodic solutions on R³/Z³ with **f ≡ 0**. (C) asks for one admissible smooth force **f not constrained to zero** and data on R³ for which no globally smooth finite-energy solution exists. (D) is the corresponding breakdown alternative for periodic data and smooth, rapidly time-decaying periodic force. These alternatives are not interchangeable: proof of a forced counterexample under (C) or (D) does *not* provide an unforced counterexample to (A) or (B).

The public OpenAI manuscript [2], Theorem 1.1, asserts for every ν > 0 a smooth compactly supported force, zero initial velocity, bounded L² kinetic energy prior to time 1, and unbounded L∞ velocity as t approaches 1. The manuscript explicitly identifies this with (C) and its periodic corollary with (D). This is an *author-reported* result in the sources examined, not a mathematical theorem independently recertified in NS-REIK-002. Clay's 11 September 2026 statement describes the problem as **apparently** settled and states that review will proceed [3].

## 4. Fixed Lean-source correspondence audit

The GitHub repository `openai/NavierStokesAndEuler` was pinned at commit:

`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

A connector-retrieved Git tree under that commit reports 2,673 objects and 2,659 `.lean` files (33,721,830 aggregate bytes of `.lean` files). Selected UTF-8 Lean source bytes were retrieved by exact path and pinned commit; their SHA-256 digests were calculated in a second runtime implementation tested against the standard `SHA256("abc")` vector. Git blob SHA-1 and the separately calculated content SHA-256 appear in the machine-readable source register. Only selected files were read. A frozen Git commit protects version selection, not the semantic correctness of the formal model.

Observed theorem correspondence in named modules:

* `NavierStokes/ComparatorR3Theorem.lean` has `navier_stokes_breakdown_R3` with quantifiers `∀ν>0`, existence of smooth initial data and a decay-admissible force, and nonexistence of a global smooth finite-energy solution; this is the author's adapter to (C).
* `NavierStokes/ComparatorTheorem.lean` has `navier_stokes_breakdown_periodic` with periodic initial data and smooth decaying force and nonexistence of a global smooth periodic solution; this is the adapter to (D).
* `NavierStokes/R3/Theorem.lean` exposes the author's `theorem_1_1` from its constructed candidate and a separate initial-rest statement.
* `NavierStokes/PeriodicPaperTheorem.lean` records a periodic construction and explicitly distinguishes support inside a fundamental cell from global compact support of a periodic lift.
* `NavierStokes/ComparatorSolution.lean` names both comparator theorems and imports the two proof adapters. The top-level `NavierStokes.lean` imports this solution module and `PaperResults`.

An important **non-failure** control: `ComparatorChallenges/NavierStokes.lean` is a *standalone challenge reference* with intentionally unproved `sorry` goals. Its comments state the submission does not import that reference, and the submission imports comparator definitions instead. The presence of `sorry` in the reference is not by itself evidence that the claimed theorem modules use unproved axioms. Conversely, viewing module text and a `#print axioms` command without executing it is **not** independent verification of the full proof.

**Pending independent checks:** acquire the exact full source snapshot and dependencies; install the pinned Lean 4.34.0-rc2 and Mathlib environment; run a clean `lake build`; run `lake exe comparator ComparatorChallenges/NavierStokes.json` with verified comparator dependencies; inspect actual produced axiom lists and build logs; review possible formalization-to-Clay gaps. None of these environment-dependent operations was run in this local experiment. No claim of independently certified Lean completion is made.

## 5. New unforced three-dimensional vortex-stretching experiment

Take the genuinely three-dimensional torus `T³ = (R / 2π Z)³`. Define wavevectors and transverse amplitudes:

`k1=(1,0,0), p1=(0,−2,2)`;

`k2=(0,1,1), p2=(1,−2,2)`;

`k3=(1,1,1), p3=(1,1,−2)`.

Define the time-zero velocity field:

`U(x,y,z) = p1 sin(x) + p2 cos(y+z) + p3 cos(x+y+z).`

For each mode, `k_j·p_j=0`, so `∇·U=0` identically. It is real-analytic and periodic. Let vorticity `ω = ∇×U` and define the three *normalized spatial averages* (the unnormalized integrals are each multiplied by `(2π)^3`):

`S(U) = average[ ω·(ω·∇)U ]`  (vortex-stretching production);

`E(U) = average[ |ω|² ]`  (enstrophy);

`D(U) = average[ |∇ω|² ]`  (viscous vorticity dissipation).

An exact Fourier convolution sum over the six nonzero frequency modes gives:

**`S(U)=1, E(U)=22, D(U)=49`.**

A distinct physical-space 16×16×16 periodic trapezoidal quadrature independently returns `1.0`, `22.0`, and `49.0`, within `10^−12`. The grid is sufficiently fine to integrate these particular low-frequency trigonometric polynomials exactly in exact arithmetic; the floating calculation has ordinary numerical tolerance. This is corroboration by a different representation, not external peer replication. Deliberately perturbing the third amplitude to `(1,1,−1)` makes `k3·p3=1`, correctly failing the divergence-free control.

For a smooth unforced solution, the usual vorticity-enstrophy identity (valid for times when the solution is smooth) is:

`(1/2) d/dt ∫|ω|² + ν∫|∇ω|² = ∫ω·(ω·∇)u.`

Consider the proposed shortcut `|S(u)| ≤ νD(u) + Cν E(u)` for every smooth divergence-free u, with a constant `Cν` independent of its initial amplitude. Since `u=λU` gives:

`S(λU)=λ³, E(λU)=22λ², D(λU)=49λ²`  (normalized averages),

the proposed universal inequality becomes `|λ|³ ≤ (49ν + 22Cν)λ²`. For any fixed finite ν and Cν, choosing `λ > 49ν + 22Cν` falsifies this bound. In particular at `ν=1`, `Cν=0`, and `λ=50`, we find `S=125000 > D=122500`. By local smooth well-posedness, this is permissible initial data for the unforced equation, not an arbitrary non-solution inserted into a PDE claim.

**Scientific meaning:** a data-independent *linear* enstrophy absorption bound cannot close the unforced 3D regularity problem. It was falsified as a candidate proof step. Nothing in this counterexample implies that smooth Navier–Stokes solutions actually blow up. In fact standard estimates allow a *superlinear* dependence, schematically `|S| ≤ (ν/2)D + Cν^−3 E³` for positive ν. The resulting ODE estimate alone does not establish a global time bound. A serious successor must investigate structural/geometric vortex-stretching depletion, not a universally amplitude-insensitive linear inequality.

## 6. Research implications for REIK/TCGE

This is a substantive test of the framework's falsification discipline: a compelling proof shortcut is rejected through an explicit smooth 3D test field while the more ambitious theorem remains unknown. FIDELITY's Non-Expansion and Falsification Persistence rules forbid promoting the exact finite example into a global result or silently deleting a failed proposal. The original epistemic kernel `0 / U / 1` is applied to *precisely stated claims*: a candidate universal linear estimate is `0` (falsified), the file/receipt calculations are `1` (passed within exact scope), and a new full 3D global theorem is `U` with workflow `0 · HOLD`.

A future productive candidate may explicitly constrain alignment of vorticity and the strain eigenvectors, or a scale-invariant norm, and state a verifiable regularity implication with exact hypotheses. Such bounds must survive the amplitude family `λU` and other falsification controls, and any derivation should connect to established conditional regularity criteria without claiming previously known work as new.

## 7. Limitations, reproducibility, and disclosure

1. **Original kernel:** hash recorded verbatim; underlying original kernel bytes were not present for an independent SHA-256 rehash. No changed kernel is written.
2. **Historical enterprise chains:** EC-025/026 SHA-256 strings remain prior claims, not independently verified ancestors of this new local work.
3. **Parent:** all NS-REIK-001 file digests and receipt links are recomputed; the parent archive is included unchanged.
4. **Source PDFs:** the official six-page Clay PDF and the 166-page OpenAI manuscript were read through a web PDF reader, but direct byte download failed in the container (DNS disabled). Their exact PDF SHA-256 remains **UNVERIFIED / NOT ACQUIRED**, not guessed.
5. **Lean:** selected pinned UTF-8 source content has connector-calculated SHA-256 and Git object identifiers; no full source snapshot or Lean/Comparator build was executed. Repository content is not a substitute for proof checking or mathematical peer review.
6. **Mathematical controls:** Fourier calculation and independent-grid comparison are local tests; neither tests singularity at a later time nor independently checks the published proof's 166-page derivation.
7. **No external actions:** no GitHub commit, external dispatch, public release, cryptographic signature, or third-party validation occurred while producing NS-REIK-002.

## 8. Conclusion

NS-REIK-002 recovers and verifies its local predecessor, pins the author's Lean theorem adapters to a single publicly identified commit, states correctly the forced/unforced Clay distinction, and supplies a reproducible exact 3D negative control for a linear enstrophy estimate. This is a narrow but meaningful mathematical result for *the research process*: it eliminates one inadmissible proof strategy. It does **not** settle the unforced Navier–Stokes problem or confer independent validation on the OpenAI formalization. Work remains `0 · HOLD` for any newly claimed universal theorem.

## References

[1] C. L. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, Clay Mathematics Institute. https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

[2] OpenAI, *Finite Time Blowup for Navier–Stokes*, 2026, Theorem 1.1, Corollary 10.6. https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

[3] Clay Mathematics Institute, *Navier–Stokes Announcement*, 11 September 2026. https://www.claymath.org/news/navier-stokes-announcement/

[4] Richard Stein, *REIK_ROOT.md*, `eternalimit/clarity`. https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md

[5] Richard Stein, *FIDELITY: A Provenance-Preserving Logic for Verifiable Knowledge in Distributed Computational Systems*, `eternalimit/chatgpt`, September 2026. https://github.com/eternalimit/chatgpt/blob/main/preprints/FIDELITY_preprint_v0.1.md

[6] OpenAI, *NavierStokesAndEuler*, pinned Git revision `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`. https://github.com/openai/NavierStokesAndEuler/tree/f9e8bc5b38b6e212696e8a30e3e91517af887bbd

## Continue prompt — NS-REIK-003

> Continue NS-REIK-003 from the exact NS-REIK-002 paper, manifest, source register, and chronological receipt tip. First independently rehash all available NS-REIK-002 bytes and replay every new receipt from the NS-REIK-001 verified tip; preserve immutable NS-REIK-001 and original kernel reference SHA-256 03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402. Keep EC-026 bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e and EC-025 c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835 as historical HOLD references unless original bytes are independently obtained. Preserve all eight FIDELITY principles, original REIK/TCGE 0/U/1, 0 HOLD, source identity, chronology, independent Echo, negative controls, private boundaries, and exactly one append-only successor. Prioritize acquiring original-byte Clay and OpenAI PDF files and the complete pinned OpenAI Lean repository at commit f9e8bc5b38b6e212696e8a30e3e91517af887bbd with exact SHA-256; then attempt a clean Lean 4.34.0-rc2 lake build and independent Comparator checks, preserving every failure. Independently re-derive the NS-REIK-002 Fourier triad S=1, E=22, D=49; treat its falsified data-independent linear estimate as a permanent failed hypothesis, not a blowup theorem. Investigate a precisely scoped, falsifiable conditional vortex-alignment depletion estimate for the unforced 3D equations; distinguish forced Clay C/D from unforced A/B. Do not claim universal proof, independent verification, PDF byte acquisition, execution, GitHub commit, signature, or deployment without actual evidence. Deliver a sourced research paper (PDF and editable Markdown), exact hash structure, chronological receipt verification, machine-readable artifacts, and a continuation prompt at the end.
