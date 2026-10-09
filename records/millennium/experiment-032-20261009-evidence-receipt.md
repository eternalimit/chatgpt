# Millennium Research — Experiment 032 Public Evidence Receipt

Date: 2026-10-09  
Canonical state: **0 · HOLD**  
Classification: **finite archived integrity/proof audit PASS; external acquisition HOLD; P versus NP NOT SOLVED**.

## Original identity and single parent

- Original unchanged REIK/TCGE 0-U-1 kernel SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- **Selected original-byte local parent** Experiment 031 ZIP SHA-256: `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff`.
- Exact parent Experiment 031 manifest SHA-256: `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`.
- Exact parent Experiment 031 294-event tip: `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f`.
- Immutable Experiment 030 inner manifest: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`; 282-event tip: `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5`.
- **Do not merge** the distinct public Experiment 031 variant (manifest `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`). The selected parent lineage was publicly distinguished at commit `3fc088960a8ac374e87345a22693e7932e5691c7`.

## One locally sealed append-only Experiment 032 successor

- Local `manifest032.json` SHA-256: **`2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f`**.
- Chronological 306-event tip: **`c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8`**. Exactly 294 inherited + 12 append-only successor receipts.
- Locally sealed `millennium_reik_3sat_exp032.zip` SHA-256: **`4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c`** (799,684 bytes). **ZIP binary is not uploaded in this public text commit.**
- Independent read-only Python-standard-library audit rehashed exact immutable archives from Experiment 031 down to 023, all 294 historical receipt links (Experiments 019–031), and four finite UNSAT resolution derivations with **3,076 correct resolution steps**, each source having all **256 active variables**. Independent verifier does not import predecessor audit scripts.
- Eighteen new local falsification/admission controls passed expected rejection; fresh ZIP extraction and comprehensive audit passed.
- Original kernel and eight FIDELITY principles retained: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.

## New pinned SAT candidate inspection (not admission of complete benchmark pair)

- Via GitHub connector, read full text of pinned `domenlusina/SAT_SOLVER_PAJACA` source **without a space in actual repository name**: `https://github.com/domenlusina/SAT_SOLVER_PAJACA/blob/1a8be2a13d9c3a45903ddf07e918205b272baf1d/CNF1.txt`; Git blob SHA-1 `45d3dc06e4ac28d19326c38d92b9f9421f3b2bd6`.
- Independently parsed **20,864** two-positive-literal clauses and all **256** active variables; the all-true Boolean assignment satisfies every returned clause (41,728 positive, no negative literal occurrences).
- **HOLD**: connector text was not received and locally SHA-256-checked as an immutable original raw file inside the sealed ZIP. It is one straightforward SAT candidate, not a verified independent 256-variable SAT **and UNSAT** pair. No external UNSAT original bytes or independent UNSAT proof checker acceptance.

## Dedicated solver HOLD

- Debian publisher *expected* checksum metadata only, for CaDiCaL 2.1.3-3 AMD64 `cadical_2.1.3-3_amd64.deb`: `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25` (467,080 bytes), reference: `https://packages.debian.org/sid/amd64/cadical/download`.
- Actual `curl` binary download failed with exit **6**: `Could not resolve host: ftp.debian.org`; a second container download attempt failed. No package bytes, **no locally computed package SHA-256**, no executable SHA-256 or version/architecture check. `cadical`, `kissat`, `minisat` absent from execution PATH.
- **No new solver runtime benchmarks. No Z3 substitution. No locally generated cases relabeled as independent.**

## Scope and evidence boundary

This public status receipt is **not** an uploaded source archive, independently obtained 256 SAT/UNSAT benchmark pair, verified dedicated solver executable, independently controlled peer audit, cryptographic signature, or general SAT/P-versus-NP proof. No secrets/private inputs disclosed. One forward local lineage; unresolved **0 · HOLD**. Exact full research paper, manifest and independent reproducer remain in the separately generated local ZIP.
