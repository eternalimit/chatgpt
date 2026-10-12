# Battleship-256: 2014 ASlib ground-truth provenance and HOLD audit
Date: 2026-10-12. Scope: SAT benchmark historical metadata only. This is not SAT Experiment 042.

## Research finding and interpretation
An independently maintained SAT algorithm-selection dataset includes the original SAT11 Battleship benchmark as `./SAT11/crafted/skvortsov/battleship/battleship-16-16-unsat.cnf,?` in `SAT11-HAND/ground_truth.arff`. The exact same file blob was retrieved at historical Git commit `ff5cffb640006f817f161392bba5bf9349a49b70` (recorded author date 2014-12-09) and later pinned commit `551b22beef8df17de59286b4822ef720e0aa4d6f` (2025-09-29). Git blob SHA-1: `78ebba7c6598fa9d1a67507a0a811109ae6f76d8`.

The ARFF schema declares `@ATTRIBUTE satunsat {SAT,UNSAT}` and the dataset uses `?` for unknown/missing values. Therefore this source does NOT independently certify UNSAT for Battleship-256. It also does NOT contradict the bounded local modular-parity mathematical argument; the two answer different evidentiary questions. The original third-party benchmark and prior orthomorphism mathematics remain distinct from Richard Stein's REIK/TCGE evidence workflow. Neither exclusive authorship nor scientific novelty is established.

## Evidence manifest / categorized hashes
- Fresh fetched historical original text: `coseal/aslib_data/SAT11-HAND/ground_truth.arff` at commit `ff5cffb640006f817f161392bba5bf9349a49b70`, Git blob SHA-1 `78ebba7c6598fa9d1a67507a0a811109ae6f76d8`; no fresh SHA-256 computed. This is dataset original text, NOT original SAT11 CNF bytes.
- Cross-check same Git blob at 2025 pinned commit `551b22beef8df17de59286b4822ef720e0aa4d6f`.
- Historical third-party CNF SHA-256 reference (NOT rehashed this run): `2f62adaa851df2a4d6b0e019cd4f0c18ee1c3be44b008a2a76b6189e0f116179`; Git blob SHA-1 `099d3d6e2ee7103d45201021203d82efc205de39`.
- Historical protected kernel SHA-256 reference (NOT rehashed): `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`, 4299 bytes.
- Original SAT11 archive expected SHA-1 `f8183301571b146d91235e577327cad6b0d5c661` is publisher/download-script metadata only; no archive bytes acquired.
- Synthetic/local: previous parity tests and controls not rerun. Unresolved: original 2011 archive bytes, accepted matching UNSAT certificate, dedicated independent checker, independent Echo, externally administered custody.

## Actual execution and negative controls
Method: read GitHub historical commit and pinned file using connected read-only API; parse fetched ARFF text using JavaScript. Exact parser procedure: split on newline, omit empty and @ header lines, split last comma field into SAT / UNSAT / ? / other; find basename `battleship-16-16-unsat.cnf`.
Output: 296 instance rows; SAT=143, UNSAT=76, ?=77, other=0. Exactly one Battleship row, marked `?`. Controls PASS: SAT and UNSAT examples present, Battleship row unique, unknown not misclassified as UNSAT. No shell command or shell exit code; no independent SAT checker, Lean or Echo executed.
Local HTTPS HEAD attempt to `https://www.cril.univ-artois.fr/SAT11/bench/SAT11-Competition-SelectedBenchmarks.tar` with `python -B` failed with DNS resolution error; process exit 2. No archive transfer.
GitHub research HEAD before write: `7bc95c2b04013220bf75d217ec81f4fc97abb221`. Clarity HEAD: `ef98a67d6716af0bcd2388bbda83ef0ebb1f06fb`.

## FIDELITY, limitations and next gate
Preserve Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence and Uncertainty. Keep original `kernel001.py` unchanged, `K=R AND I AND E`, `E=0`, `DROP U`, `0 HOLD`. Preserve separate provenance 016–031 branches, SAT 039–041, NS-REIK, Clarity/Pi, CPU/GPU, semantic 048–050 and HCL histories. The `?` label is not an accepted proof and cannot be promoted to either SAT or UNSAT. Next: acquire original 2011 competition archive bytes and independent matching SAT certificate/checker before advancing.
