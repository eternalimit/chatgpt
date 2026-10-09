# REIK/TCGE Research Paper A033 — External Original-Byte 256-Variable SAT Admission and Outstanding UNSAT/CaDiCaL Gates

**Date:** 2026-10-09  
**Attribution:** Richard Stein / Clarity REIK/TCGE; AI-assisted retrieval, verification, and drafting  
**Evidence state:** **0 · HOLD** for paired independent 256-variable SAT/UNSAT, dedicated solver and all general claims  
**Classification:** Working research paper, not peer reviewed. Neither P vs NP nor any broader theorem is solved.  
**Prior commits:** Audit 031 `e027c9b4e2b9044fb8c8b0bb9808844f1198691f`; acquisition working paper `4d03295705ac7826fe841f08359fb8af15455867`; public receipt `32df7f25714dcfea823de257deaed74a787044a1`.

## Abstract

This continuation independently verifies a **new third-party, fixed-revision, fully active 256-variable finite SAT CNF** without altering the frozen original REIK/TCGE 0/U/1 evaluator or either original Experiment 030 archive lineage. The published `CNF1.txt` in `domenlusina/SAT_SOLVER_PAJACA` was fetched by path and fixed Git commit using a GitHub contents interface. Recomputed SHA-256 of the returned original ASCII/UTF-8 file content is `5f4be6d6d859422e6a1b837f965a2db10d9e64e580f77ecfef2d9930301d072c`. The file declares 256 variables and 20,864 clauses. A separate parser counted exactly 20,864 two-literal clauses and verified that **every variable 1 through 256 occurs**. All 41,728 literal occurrences are positive, so the independently checked assignment `x1=...=x256=TRUE` satisfies every clause. Four negative controls reject mutated evidence. This is a *finite easy 2-CNF SAT witness*, **not** an independently sourced fully active 256-variable 3-SAT/UNSAT benchmark pair, proof of improved search or a representative hardness test. An original-byte external UNSAT formula with an independent certificate has not been acquired. The exact Debian CaDiCaL 2.1.3-3 AMD64 package metadata is publisher-confirmed; actual package and executable bytes could not be downloaded and therefore could not be hashed or run. External UNSAT, dedicated solver, Clarity Pi semantic correspondence, authenticated Block −1 and global complexity claims stay **HOLD**.

## 1. Identity, parent provenance, and distinct receipt descendants

The frozen original `kernel001.py` has SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. The prior read-only local archive audit was rerun on this date without editing archive bytes; it passed the original kernel, immutable parent, chronological receipts, four finite UNSAT resolution derivations (3,076 steps), and seven inherited tamper controls.

Shared Experiment 029 original ZIP SHA-256: `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`. Its manifest SHA-256 is `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`; inherited 270-event tip is `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`.

| Archive sibling | Original ZIP SHA-256 | Manifest SHA-256 | Total events | Receipt tip SHA-256 |
|---|---|---|---:|---|
| 030-A / 282 | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | 282 | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` |
| 030-B / 280 | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | 280 | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` |

These are **siblings descending from the same exact 029 archive**, not each other's append-only successor. Do not merge tips, back-date Git commit ancestry, or replace original bytes. Existing Experiment 031 variant archives recorded by later A032 research are additional distinct descendants and **were not independently rerun in this A033 iteration**.

Block `−1` remains a *pre-genesis index/reference* only; no independently authenticated historical root material was recovered.

## 2. Independent published 256-variable SAT source

- Repository: https://github.com/domenlusina/SAT_SOLVER_PAJACA
- Exact fixed source: https://github.com/domenlusina/SAT_SOLVER_PAJACA/blob/1a8be2a13d9c3a45903ddf07e918205b272baf1d/CNF1.txt
- Commit selected: `1a8be2a13d9c3a45903ddf07e918205b272baf1d`.
- GitHub-returned Git blob SHA-1: `45d3dc06e4ac28d19326c38d92b9f9421f3b2bd6` (distinct algorithm/object from SHA-256).
- SHA-256 of GitHub-returned file contents encoded as ASCII/UTF-8, recomputed with a separately authored SHA-256 implementation checked against the `abc` reference vector: `5f4be6d6d859422e6a1b837f965a2db10d9e64e580f77ecfef2d9930301d072c`.
- Source file bytes: **191,052**. Header: `p cnf 256 20864`.
- Parsed clauses: **20,864**, each of width **two**, each terminated with `0`; zero malformed terminators; zero repeated literals within clauses.
- Declared/actual variable set: **exactly `{1,...,256}`**, maximum index 256. No variable absent.
- Total literal occurrences: 41,728, of which negative literals: **0**.
- Finite satisfying assignment: every variable `TRUE`. All 20,864 original clauses directly evaluated to `TRUE`; **SAT witness PASS**.
- This particular externally authored file is straightforward monotone 2-CNF, not 3-CNF. By itself it supplies **neither** an UNSAT certificate **nor** complexity or performance evidence.

### 2.1 Witness validity

For the original clause set (F=\bigwedge_{i=1}^{20864}(x_{a_i}\lor x_{b_i})), each (a_i,b_i\in\{1,\ldots,256\}) because all parsed literals are positive. Define (v(x_j)=\mathrm{True}) for every (j\in\{1,\ldots,256\}). Each disjunction is true, hence (v\models F). The direct clause-by-clause replay, not a solver's self-report, establishes this finite SAT result.

This is not a proof that all CNFs, all 256-variable CNFs, or arbitrary 3-SAT instances are satisfiable or easy.

### 2.2 Adversarial controls, performed on in-memory copies

| Control | Independently checked response |
|---|---|
| Change first positive clause `9 8 0` to `-9 -8 0` | All-TRUE model rejected |
| Change header 256 to 255 | Header/variable-contract rejected |
| Remove a clause, leaving header count unchanged | Clause-count mismatch rejected |
| Change every literal occurrence of variable 256 to 255 while preserving header | Fully-active variable set rejected |

Each mutation was intentionally applied to a copy for falsification testing; **no publisher or original source file was modified**.

## 3. External UNSAT candidate admission: still open

The admission requirement is not met by a label `UNSAT`, a solver's exit status, or an internal inherited proof. A qualifying external candidate must have an independent author/publisher, a pinned download identifier, the exact received original file SHA-256, parsed active variables `{1,...,256}`, a well-formed declared clause count, explicit independent UNSAT proof data, pinned proof checker and independently checked empty-clause/certificate acceptance. No qualifying original-byte external UNSAT instance or proof was received and checked in this iteration.

SATLIB's standard paired `uf250-1065/uuf250-1065` corpus has **250**, not 256, variables and is deliberately excluded. The separately published RandSATBench / ArtLabBocconi research identifies 256-variable 3-SAT datasets and CaDiCaL-generated labels at https://github.com/ArtLabBocconi/RandCSPBench , but its linked `kSAT.zip` source bytes, per-instance SAT/UNSAT evidence, and independent UNSAT certificates were **not acquired**; metadata alone is insufficient for admission. A solver label is not a formal refutation proof.

## 4. Pinned CaDiCaL binary and independent proof-checking gate

Debian's official exact AMD64 package listing is https://packages.debian.org/forky/amd64/cadical/download . It identifies `cadical_2.1.3-3_amd64.deb`, 467,080 bytes, publisher-expected SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`. Direct acquisition via Debian mirror was attempted and **failed**. Independent DNS probes returned temporary name-resolution failures for public hosts in the container. Neither the downloaded package nor its extracted executable is locally present, checksum-confirmed or executed. The **published reference is not a hash of locally received bytes**.

Before a dedicated solver benchmark: acquire exact package bytes from publisher mirror; record received SHA-256 and 467,080-byte count; compare to publisher checksum; extract the binary; log executable SHA-256, `--version`, relevant dependencies and platform; run a fixed benchmark with source input fingerprints; independently check SAT witnesses and UNSAT certificates using a separately version-pinned checker. Do not use Z3, generated substitutes, a package filename or a publisher digest in lieu of required bytes.

SAT Competition 2026 explicitly distinguishes `SATISFIABLE` plus a satisfying model, `UNSATISFIABLE` plus a proof file, and `UNKNOWN`; see https://satcompetition.github.io/2026/output.html . Its benchmark formatting requires variable count to reflect the actual file: https://satcompetition.github.io/2026/benchmarks.html .

## 5. REIK/TCGE and Clarity Pi Math evidence semantics

Canonical Clarity root: https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md . It defines `R` = Reality/direct evidence, `I` = inference, `E` = **independent Echo**, and `K = R AND I AND E`. An unresolved evidence gate yields **HOLD**, not a fabricated false or true verdict. The original REIK/TCGE partial Boolean evaluator's 0/U/1 semantics remain separately preserved; this study does not change the frozen kernel or claim a proved correspondence theorem.

For nonzero (x), (N(x)=x/x=1); hence `sqrt(pi)/sqrt(pi)=1` exactly. Since distinct nonzero values produce the same normalized output, (N) is non-injective, so arithmetic normalization alone cannot identify a source, certify a claim, or establish independent Echo. A formal Clarity Pi-to-REIK adapter with typed source, proposition, independent verifier and falsifier handling is still a separate **unproved research goal**.

## 6. FIDELITY preservation

1. **Identity** — exact retrieved file bytes and distinct digest objects, no variable padding.
2. **Provenance** — external source identified by fixed commit, not relabeled as an internally generated experiment.
3. **Chronology** — inherited manifests, branch tips and newer audit papers remain separate.
4. **Independence** — locally authored parser/model checker distinct from source author's SAT solver; this is not independent institutional peer review.
5. **Method/Object Separation** — finite witness vs general algorithmic performance.
6. **Non-Expansion** — easy monotone 2-CNF is not a 3-SAT hardness demonstration.
7. **Falsification Persistence** — four new negative controls and earlier failed acquisition retained.
8. **Uncertainty** — missing independent UNSAT, pinned executable, Block −1 root and formal Pi bridge remain HOLD.

## 7. Status and falsifiable next steps

| Gate | Status |
|---|---|
| Original REIK/TCGE kernel preservation and A031 finite archive replay | PASS (local) |
| Fixed-source, full-activity 256-variable finite SAT model | **PASS (new; easy 2-CNF)** |
| External original 256-variable UNSAT with checkable proof | **HOLD** |
| Externally sourced fully active 256-variable **3-SAT** benchmark pair and fair solver comparison | **HOLD** |
| Exact CaDiCaL package and executable locally acquired and verified | **HOLD** |
| Independent external replication / third-party Echo | **HOLD** |
| Original authenticated Block −1 root | **HOLD** |
| Formal Clarity Pi-to-REIK semantic adapter and proof | **HOLD** |
| P vs NP resolved, broad mathematical breakthrough, OpenAI adoption, blockchain transaction or signing | **NOT ESTABLISHED** |

**Conclusion.** A meaningful but strictly narrow research improvement was obtained: a third-party-published, fixed Git revision and exact-byte 256-variable SAT file was independently inspected, fully-active checked, and accompanied by a verified SAT model with negative controls. The required paired independent 256-variable UNSAT original-byte certificate and actual CaDiCaL executable remain unavailable. Preserve all previous evidence without merging variants, changing kernel, or promoting a HOLD state.

## Source references

- Third-party source CNF: https://github.com/domenlusina/SAT_SOLVER_PAJACA/blob/1a8be2a13d9c3a45903ddf07e918205b272baf1d/CNF1.txt
- Third-party project description: https://github.com/domenlusina/SAT_SOLVER_PAJACA
- Debian exact binary metadata: https://packages.debian.org/forky/amd64/cadical/download
- 256-variable dataset discovery (not acquired): https://github.com/ArtLabBocconi/RandCSPBench
- SAT Competition rules: https://satcompetition.github.io/2026/benchmarks.html and https://satcompetition.github.io/2026/output.html
- Last public audit: https://github.com/eternalimit/chatgpt/commit/32df7f25714dcfea823de257deaed74a787044a1
