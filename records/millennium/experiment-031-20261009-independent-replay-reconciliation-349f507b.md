# Experiment 031 — independent replay variant / public provenance reconciliation

Date: 2026-10-09. State: **0 · HOLD**. P vs NP **NOT SOLVED**.
Purpose: distinguish a separately reproduced local Experiment 031 artifact from the already-public Experiment 031 receipt without rewriting either one. **One local successor ZIP is preserved; this commit is a public reconciliation note, not a second solver run or newly claimed proof.**

## Unchanged original and exact parent

- REIK/TCGE original kernel `kernel001.py` SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Exact Experiment 030 parent ZIP SHA-256: `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942`.
- Exact Experiment 030 manifest SHA-256: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`.
- Experiment 030 chronological 282-event tip: `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5`.
- Verified parent public commit: `b5578bc70bfc6333c7ea1eba84c404979760edc8`.

## Locally computed *independent replay artifact* (this note)

- Original-byte nested archive lineage replayed down through Experiment 023, and all historical events independently recalculated for Experiments 019 through 030 (282 of 282).
- Four historical, finite UNSAT resolution certificates checked step by step (1023 + 1023 + 1023 + 7 = 3076). Each archived problem uses all 256 variables. These are *internal historical constructions*, not external original-byte benchmark acquisitions.
- Eight FIDELITY principles preserved: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.
- Fourteen additional local mutation/admission controls passed; no new solver runs.
- Sealed local successor ZIP: `millennium_reik_3sat_exp031.zip`, SHA-256 **`50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff`**.
- Corresponding *local* `manifest031.json` SHA-256 **`349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`**.
- 294-event tip (282 parent + 12 local successor events) **`6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f`**.
- The detailed Markdown/PDF research paper, independent replay script, falsification records and unchanged Experiment 030 parent ZIP are included in the **local downloadable ZIP**. That ZIP is *not* uploaded by this text commit.

## Existing public Experiment 031 record is distinct

The earlier record at `records/millennium/experiment-031-20261009-evidence-receipt.md` on main states *different* Experiment 031 identifiers: manifest `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`, 294-tip `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384`, ZIP `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a`. That record was fetched from GitHub, **but its corresponding original binary ZIP was not rechecked in this reconciliation**. These two self-consistent *claimed local successors* must not be represented as the same artifact or collapsed into a single receipt chain. No existing GitHub record was edited or overwritten.

## External admission gates remain HOLD

- Independently sourced, genuine original-byte fully active 256-variable SAT and UNSAT pair with independently checked SAT model and UNSAT certificate: **HOLD**.
- CaDiCaL 2.1.3-3 AMD64 expected publisher package SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`: **metadata only**; DNS prevented receipt of actual package bytes. No locally calculated package/executable hash or dedicated solver execution.
- New fair solver benchmarks: NOT RUN. No Z3 or locally generated substitutions. General polynomial-time 3-SAT claim and P versus NP: **HOLD**.

This public record reports hashes of produced local artifacts; it is not an external signature, published binary, peer certification, or mathematical proof. Preserve both distinct histories and advance neither unresolved claim.
