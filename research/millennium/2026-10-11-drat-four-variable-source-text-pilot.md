# DRAT four-variable source-text pilot — 2026-10-11

## Provenance and acquisition
Source: marijnheule/drat-trim pinned Git commit `2e3b2dc0ecf938addbd779d42877b6ed69d9a985`. GitHub connector `fetch_file` retrieved exact text of `examples/example-4-vars.cnf`, `examples/example-4-vars.drat` and `examples/example-4-vars.lrat`. Pinned tree reported blob SHA-1 respectively `78888478dee9c0d636d4fb3e8ee90f27bb646044`, `343424c63732ebb1fa020a76f3cf6f11c0212d75`, `7326c50ca99a8a86c072b6aa4fcb0b0fd02a7a05`. GitHub text is not independently downloaded publisher bytes; direct curl of raw.githubusercontent.com failed DNS (exit 6).

Local UTF-8 text SHA-256: CNF `db5e33941144b193ffe718356a57269642e525748415fc2c6deab59b1be07b55`; DRAT `0fada1a0ab0162f053b9d4a17bb42e69caa9fc95c149bc46c26a61d3c746a86b`. These match historical cited values but are newly computed over reconstructed connector text in the isolated runtime. LRAT text was retrieved but not executed or locally hashed in this pilot.

## Actual isolated execution
Command: `python -B /mnt/data/drat_audit/check.py`; Python stdlib only, no external solver/checker executable. Implemented a small independent RUP unit-propagation routine and RAT pivot/resolvent check for DRAT additions, exact tuple deletion and empty-clause acceptance. CNF independently enumerated all 16 Boolean assignments.

Result: original proof accepted, additions `RAT,RUP,RUP`, three deletions, zero satisfying assignments. Four deliberate mutations were rejected: wrong first unit (at later clause), missing final empty clause, premature empty clause, and nonexistent deletion. **Falsification persistence:** changing second added unit from `2` to `-2` was *also accepted* by this local checker; therefore this mutation is NOT a successful negative control. The checker is a local bounded implementation, not an established independent DRAT-trim executable, and its correctness has not been formally proved. Acceptance of that mutation cannot be presented as failure of the published proof or as a successful rejection test.

## Boundaries
No original-byte external custody, no compiled DRAT-trim or LRAT-check run, no solver-emitted 256-active-variable UNSAT certificate, no independent Echo. SAT 041 remains HOLD; no SAT 042; no P-versus-NP claim. This is a separate source-text pilot and must not merge with semantic Experiments 048–050, NS-REIK, or provenance branches. Historical immutable `kernel001.py` reference SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`; original kernel not accessed or modified. Preserve eight FIDELITY principles, DROP U and `0 HOLD`.

## Next gate
Acquire independently hashable original source files and a pinned established checker executable; execute the published DRAT and LRAT proofs with intentionally invalid tampering controls, report exit codes and executable SHA-256. For the Millennium SAT gate separately acquire published exact 256-active-variable UNSAT CNF and matching accepted proof.
