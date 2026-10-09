---
title: 'Millennium Research Experiment 030: Append-Only Receipt Replay, Resolution Verification, and External Acquisition Gating'
author: 'Richard Stein (REIK/TCGE framework originator); technical audit and synthesis with AI assistance'
date: '9 October 2026'
geometry: margin=0.86in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
---

# Abstract

This paper reports a strictly bounded, reproducible integrity audit of the REIK/TCGE `0/U/1` research sequence through Experiment 029 and a single append-only Experiment 030 successor. The identical original `kernel001.py` has SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Experiment 029's exact manifest rehashes to `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`; its inherited 270-event tip is `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`. Both the inherited audit scripts and a separate Experiment 030 read-only verifier independently reconstructed the 270 chronological receipt links and four finite UNSAT resolution derivations totaling 3,076 steps. The separate verifier audits exact archive-byte SHA-256, nested manifest/file membership, the original kernel, clause-level inference, and preserved HOLD labels without executing a solver. Twelve additional local adversarial admission controls passed. Independently sourced **original-byte**, **fully active**, **256-variable** SAT and UNSAT benchmark inputs and independent outcome certificates were **not** acquired. Debian's published SHA-256 for `cadical_2.1.3-3_amd64.deb` was corroborated; the actual file was not received owing to network/DNS restrictions, so neither received-package nor extracted-executable SHA-256 could be computed and there was no solver execution. The paper asserts neither a performance improvement nor a polynomial-time algorithm for 3-SAT. **P versus NP remains HOLD.**

# 1. Research scope and problem statement

The long-running REIK/TCGE series examines a frozen evaluator for conjunctive normal form (CNF) formulas under partial Boolean assignments. The evaluator has exactly three possible judgments: definite rejection `0`, definitive formula satisfaction `1`, and unresolved `U`. It is essential to distinguish a useful **semantic classification** of a partial assignment from an asymptotic claim about the complexity of deciding whether a satisfying total assignment exists.

Experiment 030 has three audit questions: (Q1) Can the immutable historical archive, event provenance, and four finite UNSAT derivations be reconstructed from the actual parent bytes without trusting summaries? (Q2) Can separately sourced original 256-variable SAT and UNSAT DIMACS files, with all 256 variables truly active and independently checkable answers, be admitted? (Q3) Can a specific publisher-identified CaDiCaL 2.1.3-3 AMD64 binary be acquired, locally SHA-256 verified, and paired with an independent proof checker before use? Q1 passed as a **local finite artifact audit**. Q2 and Q3 remain HOLD.

The archived four 256-variable UNSAT cases are finite, internally constructed/derived examples, not a replacement for an independently acquired published benchmark pair. There is no permission to rename them as independent acquisitions. Nothing in this paper relies on Z3 as a replacement for the required dedicated solver, or on a locally transformed CNF being called an original independent input.

# 2. Immutable kernel and semantics

Let $F=C_1\wedge \cdots \wedge C_m$ be a CNF formula on Boolean variables $x_1,\ldots,x_n$ and let $a$ be a partial assignment. A literal is true, false, or unassigned under $a$. The preserved evaluator reports

$$
K(F,a)=\begin{cases}
0 & \text{if some clause has every literal definitively false under } a,\\
1 & \text{if each clause contains a literal definitively true under } a,\\
U & \text{otherwise.}
\end{cases}
$$

This notation describes the retained three-valued decision logic; **the actual original program is the authoritative implementation**. `U` is not equivalent to false, true, a satisfiability proof, or a terminal accepted state. Refining $a$ can turn `U` into either `0` or `1`. Once a clause is falsified, extensions cannot make that clause true without changing prior assignments. Once every clause already contains a true literal, extending the assignment preserves satisfaction. These observations concern the semantics of a partial assignment, not the existence of a polynomial-time total search or a complexity-class separation.

The original `kernel001.py` remains byte-for-byte unchanged in the immutable Experiment 029 parent ZIP and all available nested predecessor archives inspected in this audit. Its SHA-256 is `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. The protected root snapshot remains inside the archived lineage.

# 3. Evidence preservation and methodology

## 3.1 Archive and manifest gates

The Experiment 029 source artifact, copied from the user's file library, comprises 580,916 bytes and hashes to `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`. It contains an unchanged `source/experiment028_immutable.zip`. Successive encapsulated parents descend through Experiments 027, 026, 025, 024, and 023. The separate `independent_audit030.py` reopens these ZIPs in memory, checks their CRCs, disallows duplicate or unsafe names, reads each original manifest and its matching `.sha256` sidecar, checks every declared file's raw SHA-256, and confirms exact archive membership. It verifies each nested parent archive SHA when declared. It does not import the earlier verifiers, use generated source replacements, or write to the parent ZIP.

The Experiment 029 manifest is verified against the immutable SHA-256 `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`. The original Experiment 028 package SHA-256 embedded in 029 is `974cc9e3aa6ff657811c4a658fbeb92ce73e49eb05125a27ca85fdc91cfcb5ab`. The 028 manifest is `360d6b52a6810482d0b5685699811759238fe8103d33dd24ae2c5e274830b08f`. These digests are **byte identities**, not evidence of an external cryptographic signature or immutable public storage.

## 3.2 Event ledger

Each receipt generation has its own `genesis` object, hashed as canonical JSON with sorted keys and compact separators. Within a generation, the next event must have a sequential event number and contain the immediately prior running chain hash. Its event JSON is SHA-256 hashed; the next chain tip is calculated as SHA-256 of the concatenation of the 32-byte previous-tip digest and the 32-byte event digest. The historical Experiment 019 chain uses different record field names; the independent verifier explicitly handles this legacy schema. Between generations, the genesis object must name the exact prior receipt tip and, where available, the exact prior manifest hash. A mere matching event count is insufficient.

| Experiment | Events independently replayed in 030 |
|:--|--:|
| 019 | 42 |
| 020 | 24 |
| 021 | 36 |
| 022 | 40 |
| 023 | 36 |
| 024 | 24 |
| 025 | 20 |
| 026 | 12 |
| 027 | 12 |
| 028 | 12 |
| 029 | 12 |
| **Total historical** | **270** |

All 270 links were recomputed to the exact Experiment 029 tip `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`. Experimental receipts bind local event and artifact identities; **no GitHub commit, digital signature, blockchain settlement, or external review is inferred from the chain itself.** The Experiment 030 successor appends to this evidence chain; it never edits an earlier receipt event.

## 3.3 Independent finite UNSAT resolution checker

For each of the four inherited UNSAT cases, the checker reads the original archived JSON problem bytes, recomputes the SHA-256 bound into its certificate, verifies the 256-variable declared count and actual activity of every variable $1,\ldots,256$, and initializes an ordered clause database using the recorded original clauses. Each proof step names two existing parent clause IDs, a signed pivot, and its claimed resolvent. The verifier checks that one parent contains the pivot and the other contains its negation, recomputes the complete resolvent by deleting the pivot literals and unioning the remaining literals, rejects a tautological derived clause, and checks literal-exact resolvent equality. It rejects skipped or reused new clause IDs and requires the recorded last derivation to be the empty clause. A valid sequence of resolution inferences ending in the empty clause proves the **particular** CNF unsatisfiable. It does not prove any statement about arbitrary CNFs' asymptotic runtime.

| Archived finite UNSAT case | Original clauses | Resolution steps | Result |
|:--|--:|--:|:--|
| `cycle256_unsat` | 1,024 | 1,023 | PASS |
| `cycle256_unsat_perm022` | 1,024 | 1,023 | PASS |
| `cycle256_unsat_signed023` | 1,024 | 1,023 | PASS |
| `seeded_core_unsat_256` | 1,098 | 7 | PASS |
| **Total** | | **3,076** | **PASS** |

The first three are related variants of a cycle construction. Their proof sizes are therefore **not** four independent random samples or evidence of improved worst-case performance. The seeded-core derivation terminates in seven steps because the recorded formula includes a small contradictory core. These are finite witnesses of UNSAT under the exact recorded formulas, not original-byte external benchmarking.

## 3.4 FIDELITY and admission controls

All eight inherited FIDELITY principles are retained: **Identity** (raw bytes checked rather than trusting filenames); **Provenance** (external origin not inferred from locally generated content); **Chronology** (each receipt binds its predecessor); **Independence** (a checker separate from a generator); **Method/Object Separation** (a certificate verifies a finite object, not general algorithmic correctness); **Non-Expansion** (claims do not exceed the measured evidence); **Falsification Persistence** (negative tests and historical failures remain attached); and **Uncertainty** (`U` and HOLD are not silently promoted to `1`).

Historical admission suites contain 16 Experiment 026 stored outcomes, 20 Experiment 027 recomputed outcomes, 16 Experiment 028 recomputed outcomes, and 12 Experiment 029 controls. The original standalone Experiment 026 runner is missing; its 16 stored outcomes can be hash-checked but cannot be truthfully represented as a newly rerun standalone test. The new Experiment 030 script executes **12** local admission/corruption tests, including kernel and manifest mutation, prior-digest mutation, invalid resolution pivot or resolvent, absent original SAT/UNSAT bytes or answer artifacts, fake package hash, unavailable CaDiCaL file, and Z3 identity exclusion. These tests concern the rejection logic; they are not independently acquired benchmarks or a proof of general solver correctness.

# 4. Independently sourced 256-variable SAT and UNSAT pair: HOLD

A valid acquisition requires **two** original-byte artifacts from an independently documented source, one satisfiable and one unsatisfiable. Both must be parseable DIMACS CNF with exactly 256 declared variables and exactly 256 active variables ($|\{\lvert\ell\rvert : \ell\text{ appears}\}|=256$), valid clause count, and no missing/altered bytes. The SAT case needs a independently recomputed satisfying assignment against every original clause. The UNSAT case needs an independently checked certificate such as a valid LRAT/DRAT-format proof with a compatible verifier, or a formal resolution derivation of the **original** input. Each source file should have an acquisition URL, pinned version or commit, raw SHA-256 computed after receipt, and separate public/source pedigree. The checker and answer label must not simply be a circular restatement of one solver's output.

A prior lead is the GitHub candidate `CNF1.txt`, reported with header `p cnf 256 20864`, at pinned repository commit `1a8be2a13d9c3a45903ddf07e918205b272baf1d` in `domenlusina/SAT_SOLVER_PAJACA`. It is only a **candidate**: this experiment did not acquire the original bytes, inspect all used variable IDs, establish SAT/UNSAT status, or obtain a matching independent certificate. The archived SATLIB `uf250-01.cnf` is an original-byte 250-variable example, expressly **not** 256. We also located SAT Competition DIMACS format requirements and large public archival datasets (e.g. the 2016 application track on Zenodo) but did not download or certify a suitable pair. An index link or benchmark metadata record is not a local original-byte acquisition. The admission state is **HOLD**.

# 5. Dedicated CaDiCaL 2.1.3-3 AMD64: HOLD

Debian publishes the package `cadical_2.1.3-3_amd64.deb` in its package pool. Its Debian package-download information reports a precise file size of **467,080 bytes** and SHA-256:

`a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`

A current independent web check established that the Debian pool lists that exact package and the Debian download information gives the expected SHA-256. Attempts to retrieve it into the working container using the download mechanism and `curl` did not produce package bytes; `curl` returned a DNS resolution error for `ftp.debian.org`. Therefore the **actual received package SHA-256 = NOT COMPUTABLE**, the **actual extracted executable SHA-256 = NOT COMPUTABLE**, and **executed version/binary identity = NOT ESTABLISHED**. No package was installed, extracted, or executed. No dedicated solver runtime benchmark or independent DRAT/LRAT result is claimed. Publisher metadata, no matter how authoritative, must not be substituted for the actual received-package checksum.

On a future machine where network retrieval is available, the admission protocol is: (1) fetch from a fixed official URL to a nonempty file, recording size; (2) calculate actual raw package SHA-256 with `sha256sum`; (3) reject on *any* mismatch with the Debian checksum; (4) extract without running scripts and identify the exact ELF CaDiCaL executable path; (5) compute its separate executable SHA-256, inspect architecture and dynamic dependencies, and record the version; (6) run only after those checks; (7) produce SAT models and independently check them, and produce UNSAT proofs that an independently identified checker accepts. The current record **does not claim these steps occurred**.

# 6. Experimental results and non-results

The observed outcomes are: parent archive integrity PASS, all nested manifest/receipt cross-links PASS, 270 chronological events PASS, four local 256-active-variable resolution certificates with 3,076 steps PASS, 12 local Experiment 030 adversarial admission controls PASS, and publisher-expected Debian package checksum **externally corroborated as metadata**. The 256-variable independent original-byte SAT/UNSAT pair and the locally executable CaDiCaL identity remain HOLD. Because no new solver was run, there is no comparative runtime, median, speed-up factor, asymptotic bound, or original-input result to report. Repeating an old runtime or quoting locally generated SAT instances as published independent benchmarks would violate the admission gate.

**What passed:** a falsifiable audit of finite data and proof objects, including independent reconstruction of every recorded resolution inference. **What did not pass:** provenance for independent fresh 256-variable SAT/UNSAT source files, separate independent answer certification for that pair, and local acquisition plus exact binary verification of the dedicated solver. **What is not claimed:** general SAT algorithm correctness, polynomial complexity, a collapse or separation of P and NP, or a solution eligible for a Millennium Prize.

# 7. Reproducibility and adversarial checks

Unzip the Experiment 030 evidence bundle into a clean directory, retaining the original archive and folder names. Run `python independent_audit030.py`, `python admission_controls030.py`, `python verify_integrity030.py`, and `python verify_receipts030.py` with Python 3. The first audit reconstructs the original 029 archive without importing or executing any predecessor audit script. The independent auditor and negative controls are source code inside the artifact; a new reader can inspect and rerun them. `manifest030.json` and `manifest030.sha256` bind all Experiment 030 payload file bytes except those two self-referential files. `verification/experiment030_receipts.json` links the new events to the unchanged Experiment 029 manifest and receipt tip; `manifest030.json` summarizes the exact new tip.

Recommended falsification trials include changing one archive byte, modifying a historical receipt predecessor, altering any resolution pivot or resolvent, replacing a declared 256-active-variable file with an inactive 256-declared-variable variant, changing one byte of a source CNF after calculating its expected SHA-256, and withholding the independent UNSAT proof. Any trial that incorrectly returns `ADMIT` invalidates the gate. The scripts do not promote simulated positive fixtures to external evidence.

# 8. Limitations and threat model

SHA-256 hashes detect accidental or adversarial post hoc changes conditional on trustworthy anchors; they are not digital signatures, proof of authorship, trusted timestamping, or complete chain-of-custody on their own. The audit trusts the recovered 029 bytes **as the object being checked** and compares them with the provided earlier anchors; the provenance of those earlier anchor publications is not independently established in this session. Nested archives are convenient, but their shared lineage is not the same as separate external sourcing. Historical `.json` clauses and local proofs are internally consistent and finite, but a separate third-party certificate checker and publisher-identified executable remain missing for future external benchmark testing. The independent 030 verifier was newly written and executed in the same general working environment, not audited by a separately controlled human, organization, or execution host. The conclusion is appropriately narrower than an externally peer-reviewed proof.

# 9. Conclusion and next falsifiable step

Experiment 030 preserves the original REIK/TCGE `0/U/1` evaluator byte-for-byte and appends a new, read-only independently implemented finite verifier to the 270-event Experiment 029 ledger. Four UNSAT resolution certificates totaling 3,076 steps pass reconstruction. The new tests enforce the boundary between evidence, source provenance, solver identity, and speculation. The next appropriate experimental step is not another synthetic 256-variable benchmark or a repeated, unjustified performance comparison: it is **acquiring an authentic, fully active independent 256-variable SAT/UNSAT pair with original bytes and independent certificates**, and **receiving plus checking the actual CaDiCaL Debian package and extracted executable** before any solver run. Until then, new external input and tool claims are HOLD. **P versus NP remains HOLD.**

# 10. Source and artifact references

1. Original frozen evaluator: `source/experiment029_immutable.zip` (nested `kernel001.py`), exact SHA-256 recorded in the Experiment 030 manifest.
2. Experiment 029: nested `manifest029.json`, `verification/experiment029_receipts.json`, `source/experiment028_immutable.zip` and archived predecessor proofs.
3. Debian CaDiCaL package metadata and expected checksum: <https://packages.debian.org/de/sid/amd64/cadical/download>.
4. Debian package pool: <https://ftp.debian.org/debian/pool/main/c/cadical/>.
5. SAT Competition 2026 DIMACS/source rules: <https://satcompetition.github.io/2026/benchmarks.html>.
6. SAT Competition 2016 original public application collection: <https://zenodo.org/records/11430532>.
7. DIMACS benchmark historical archive: <https://archive.dimacs.rutgers.edu/pub/challenge/sat/benchmarks/cnf/>.
8. Historical 256-variable candidate (unadmitted): <https://github.com/domenlusina/SAT_SOLVER_PAJACA/blob/1a8be2a13d9c3a45903ddf07e918205b272baf1d/CNF1.txt>.

**Status declaration:** local finite verification PASS; source and executable acquisitions HOLD; no new solver execution; no external signature or release implied by this paper; P versus NP HOLD.
