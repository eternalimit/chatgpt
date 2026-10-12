# Battleship-256 parity source audit — 2026-10-12

## Evidence admission and scope
Archive SHA-256 (locally rehashed): `679a8b5394fe82ce02df8ffbba4e61c1650740522ca184f2cd2d249d9529dd4d`. Archive ZIP integrity passed. The archive contains research update, hash ledger, audit receipt, execution output, reconstructed CNF and Python verifier. The source CNF is **locally reconstructed to a matching Git blob identity**, not independently downloaded publisher-original bytes. Historical source commit `efd38ce31035e5ad0c913a1abe4bf71fe9845463`.

## Mathematical research finding
The reconstructed 16×16 Battleship CNF has 256 active variables, 2,176 clauses, including 1,920 row-at-most-one pair clauses and at-least-one clauses for each of 16 columns and 16 modular diagonal families. Every satisfying assignment would have exactly one selected cell per row and per column; the column indices form a permutation of 0..15 (sum 120). The modular diagonal indices must also form a permutation (sum 120). But for one selected cell in each row, the modular diagonal index sum is congruent to the column-index sum minus the row-index sum: (120−120) mod 16 = 0, while a permutation of diagonal indices sums to 120 mod 16 = 8. Contradiction. This is a **bounded local mathematical UNSAT argument** tied to the source identity, not an externally accepted DRAT/LRAT certificate, strict 3CNF result, P-versus-NP solution, or independent Echo.

## Reproducible test method and receipt
Executed in an isolated temporary directory from the verified ZIP:
```sh
python -B verify_battleship_parity.py
sha256sum reconstructed_battleship_16.cnf verify_battleship_parity.py
git hash-object reconstructed_battleship_16.cnf
```
Python exit 0; reported `PASS_LOCAL_PARITY_UNSAT_SUBSET_NOT_EXTERNAL_CERTIFICATION`, 256 variables, 2,176 clauses, 1,920 row pair clauses, 16 column and 16 modular diagonal clauses. Three structural-prerequisite removal controls rejected; three two-family synthetic witness controls passed; small n=4 had no solutions and n=5 had at least one. No stderr. No dedicated solver or established checker was executed for this 256-variable CNF.

## Evidence hash ledger
- Recovered ZIP exact SHA-256: `679a8b5394fe82ce02df8ffbba4e61c1650740522ca184f2cd2d249d9529dd4d`.
- Reconstructed 36,603-byte CNF SHA-256: `2f62adaa851df2a4d6b0e019cd4f0c18ee1c3be44b008a2a76b6189e0f116179`.
- CNF Git blob SHA-1 (not SHA-256): `099d3d6e2ee7103d45201021203d82efc205de39`.
- Executed Python verifier source SHA-256: `cbdb2f63dc4011d0ee7f94f7ddbd1200d884f27589d051efe2d98e5db1b89dfb`.
- Historical protected `kernel001.py` SHA-256 reference, **not rehashed**: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Synthetic controls are not independently sourced proof evidence; full historical lineage hashes remain in the parent archive's HASH_LEDGER.json.

## Falsification persistence and HOLD
Strict 3CNF fails (256 clauses of length 16). No independent original publisher bytes, accepted matching DRAT/LRAT proof, dedicated verified SAT solver, independent proof checker on this instance, or independently administered Echo. Do not open SAT Experiment 042 or merge 030/031 histories, SAT 041, NS-REIK, Clarity/Pi, semantic 048–050, or HCL lineages. Preserve kernel, Block −1 boundary, DROP U and all eight FIDELITY principles: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. `K=R AND I AND E`; independent E absent; `0 HOLD`.

## GitHub audit
Pre-write `eternalimit/chatgpt` main: `b7e9e1cb7f77ed89370d288d02f6c90d281674b4`; `eternalimit/clarity` main: `ef98a67d6716af0bcd2388bbda83ef0ebb1f06fb`. This file is a scoped public-safe summary, not a replacement for original source custody or the full reproducibility archive. Verify the resulting commit and fetch this file back before claiming publication.
