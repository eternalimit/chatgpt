# Millennium Research — Experiment 035 (selected 034 ancestry only)

**Date:** 2026-10-09. **Research provenance:** Richard Stein, REIK/TCGE (first-party originator claim, not independently adjudicated priority). **Canonical state:** `0 · HOLD`. **P vs NP NOT SOLVED.**

This public evidence receipt is deliberately committed to branch `research/selected-e033-e034-e035-byte-audit-20261009` rooted in exact selected Experiment 034 commit `5508ce80915ad152192179d913a2a40015f6ed34`, **not merged into other A034/A035 or competing Experiment 031 histories**.

## Exact lineage (locally rehashed, full proof replay)

- Original unchanged REIK/TCGE `0/U/1` kernel SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Selected Experiment 034 ZIP SHA-256: `cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452`.
- Experiment 034 manifest SHA-256: `a224064727ef89415a9a4f20e088b3921f6269111ee6e3bd842cc25a49ae89f4`.
- Experiment 034 receipt-chain tip after 330 events: `1c73efb335758ecba4dbd20676ab6f98b4177333ab5ef0197d9da502429d47fb`.
- Selected Experiment 031-B ZIP ancestry: `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff`.
- Alternate Experiment 031-A manifest `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` **excluded**, not merged.
- Fresh replay of parent: **330/330 receipts PASS**, **four historical finite UNSAT resolution certificates PASS**, **3,076 resolution steps PASS**; original kernel unchanged.

## Material new result: original-byte-equivalent external SAT CNF now archived locally

- Third-party source: `andricicezar/sat-solver-dafny`, path `benchmarks/queens16.cnf`, pinned commit `418e5cbb1e7a311fec2c15913c0c504ec603ca91`. Original header credits **Forrest Sheng Bao** and references GNU General Public License; third-party original-source priority is not claimed.
- Source initially completely fetched and hashed by GitHub connector in Experiment 034. In Experiment 035 the published text was **reconstructed deterministically byte-for-byte** using its clause ordering and whitespace. **It was NOT directly downloaded via HTTP**; the direct raw URL had DNS failure.
- Local exact-equivalent source file now physically included in the sealed offline ZIP: **71,945 bytes**.
- Locally computed file SHA-256 `c5177c8e6523ddd9378b3b864d52fcf73b81c0a92a033433cc37e5450fa1fcd5` **MATCHES third-party original**.
- Independently computed Git blob SHA-1 `85b9071d8399839eff2352bb22315b5940bcda7c` **MATCHES original GitHub connector blob**.
- Independently parsed header `p cnf 256 6336`, **256/256 variables active**, 6,320 width-2 and 16 width-16 clauses. **NOT STRICT 3-CNF**.
- Complete 256-variable model true literals `1,19,37,50,77,89,110,124,143,150,176,183,196,219,232,250` (240 others false); **6,336/6,336 clauses SAT** verified entirely offline.
- Reconstruction script `reconstruct_queens035.py` and independent source checker `verify_source035.py` included in local archive. No full third-party CNF bytes are uploaded into this public text receipt.

## Experiment 035 local cryptographic artifacts

- Experiment 035 manifest SHA-256: **`96a4ce38b7689cc38b086d2dcfa32ec3ef6ab01ef7f86ce946cb7cd6e3512b0c`**.
- 342-event receipt-chain tip SHA-256: **`7492a249bdf0fa8ac4bc4421ac7553ec7c79a30f9addf837abd0df698868cda1`** (330 selected parent + exactly 12 new events).
- Sealed local ZIP SHA-256: **`3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`**, 973,980 bytes. **The ZIP is NOT uploaded by this GitHub commit.**
- **20/20** manifest-covered files passed SHA-256, **16/16** local falsification/admission controls passed.
- Independent full audit ran successfully after fresh ZIP extraction, including inherited proof replay. An offline deterministic ZIP re-seal yielded **byte-identical ZIP** with same SHA-256.

## FIDELITY, Echo and unresolved requirements

All eight FIDELITY controls preserved: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. Independent Echo remains required; separate same-environment implementations are **not** externally authenticated attestation. DROP U; canonical `0 · HOLD`.

**HOLD:** independent original-byte fully active 256-variable UNSAT DIMACS with independently checked machine-readable proof; complete strict 3-CNF SAT+UNSAT benchmark pair; actually downloaded and locally SHA-256 verified CaDiCaL/Kissat/MiniSat package and executable; independently authenticated Echo; general polynomial-time SAT algorithm; P vs NP proof.

Debian CaDiCaL `cadical_2.1.3-3_amd64.deb` `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25` is a **publisher-expected package SHA-256 only** (467,080 bytes), not a locally acquired package checksum. **No dedicated solver or Z3 substitute was run**. No Bitcoin signing, private data, adoption claim, or mathematical complexity breakthrough is represented.

This is a **public-safe finite evidence and provenance receipt**, not an externally signed proof certificate or original benchmark source publication.