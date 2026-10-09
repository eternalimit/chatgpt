# REIK/TCGE Working Paper: Independent-Input Admission and Semantic Evidence Boundaries

**Date:** 2026-10-09  
**Attribution:** Richard Stein / REIK–TCGE; technical verification and synthesis with AI assistance  
**Type:** Public-safe research working paper, not peer reviewed  
**State:** **0 · HOLD** for unsupported external, scientific, or execution claims  
**Starting audit:** [`e027c9b4e2b9044fb8c8b0bb9808844f1198691f`](https://github.com/eternalimit/chatgpt/commit/e027c9b4e2b9044fb8c8b0bb9808844f1198691f)  
**Additional discovered public context:** An independently published A032 GitHub audit at [`3da40be10255f029b3596c07a3c6cc62c7a0ce08`](https://github.com/eternalimit/chatgpt/commit/3da40be10255f029b3596c07a3c6cc62c7a0ce08) documents separate downstream archived Experiment 031 variants; this paper does not merge or independently re-audit those successor archives.

## Abstract

We distinguish exact-byte reproducibility of a local finite research archive from the independent provenance of external SAT benchmark inputs. An independent read-only replay of the preserved Experiment 029 parent and the two original Experiment 030 sibling ZIP archives confirmed their byte identities, receipt-chain consistency, and four archived finite UNSAT resolution certificates. A new acquisition investigation established an exact Debian publisher reference for `cadical_2.1.3-3_amd64.deb`, comprising **467,080 bytes** with published SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`. However, downloading those bytes was blocked by DNS resolution failure in the current execution environment. SATLIB's standard random 3-SAT SAT/UNSAT paired sets reach 250 variables, not the required 256, and cannot be admitted by silently padding or relabeling them. SAT Competition 2026 publishes a benchmark-acquisition URI index and the model/certificate reporting contract, but this audit has not acquired and hash-checked a compliant 256-variable external SAT and UNSAT pair and certificates. All external benchmark, dedicated-solver, P-versus-NP, formal semantic correspondence, and adoption claims remain **0 · HOLD**.

## 1. Preservation and exact ancestry

The original read-only archived `kernel001.py` SHA-256 remains:

`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`

This reference was verified against the original bytes in the privately preserved archives in the earlier audit; the audit was run again on 2026-10-09 without changing archive bytes. The private ZIP files are **not** published as part of this paper.

Shared Experiment 029 original ZIP SHA-256:

`4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`

Shared Experiment 029 manifest SHA-256:

`5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`

Shared Experiment 029 receipt-chain tip (270 inherited events):

`55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`

**030-A, 282 total receipts**, original ZIP SHA-256 `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942`, manifest SHA-256 `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`, receipt-chain tip `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5`.

**030-B, 280 total receipts**, original ZIP SHA-256 `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed`, manifest SHA-256 `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`, receipt-chain tip `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074`.

Both archives were validated as distinct, original-byte successors of the same immutable 029 parent. **Neither archive's receipt tip is linked as a child of the other tip.** Repository publication chronology is not receipt-chain ancestry. Block `−1` is a historical/pre-genesis reference only; this audit does not reconstruct an authenticated original pre-genesis artifact.

The read-only checker ran again in this continuation. It recomputed the inherited 270 receipt links, each candidate's 030 link sequence, and the same four finite UNSAT resolution derivations (1,023 + 1,023 + 1,023 + 7 = **3,076** steps). Seven independent in-memory mutation controls were rejected. This repeats the earlier bounded checks; the rerun is **not** a new independent external experiment or a claim of full re-execution of every historical local test.

## 2. Publisher-pinned CaDiCaL gate

Debian's distribution page identifies `cadical_2.1.3-3_amd64.deb` with:

- Architecture and exact version: **AMD64, 2.1.3-3**.
- Publisher-listed file length: **467,080 bytes**.
- Publisher-listed SHA-256: `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`.
- Publisher page: https://packages.debian.org/forky/amd64/cadical/download
- Source pool directory: https://ftp.debian.org/debian/pool/main/c/cadical/
- Exact desired package URL: https://ftp.debian.org/debian/pool/main/c/cadical/cadical_2.1.3-3_amd64.deb

**Observed acquisition:** an attempted package download did not return the package; a `curl` request to the publisher's host failed with `curl: (6) Could not resolve host: ftp.debian.org`. Neither package SHA-256 nor extracted executable SHA-256 nor version banner could be computed from received bytes. A publisher listing plus expected hash is not an executable acquisition or successful benchmark. The solver gate remains **HOLD**.

**Reproducible future protocol:** acquire original package bytes; check length and SHA-256 against the published values; retain source URL and retrieval time; extract in a sandbox (`dpkg-deb -x`) without privileged installation; locate exact binary, calculate executable SHA-256 and version; run a pinned independent checker and record exit codes, output, and checked model/certificate on original benchmark bytes. No substitution of an unpinned solver is authorized.

## 3. External benchmark admission — rejection of near matches

SATLIB provides externally published DIMACS random 3-SAT SAT (`uf*`) and UNSAT (`uuf*`) benchmark families. Its largest standard paired `uf250-1065` / `uuf250-1065` listed in the public index has **250 variables**, not 256. See https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html . Thus those sets are eligible only for a **separately labeled 250-variable comparison** if original bytes and certificates are acquired; they are **not** admitted to a required fully active 256-variable pair. Relabeling `p cnf 250` as `p cnf 256` does not activate six missing variables, and padding it would create a derivative, not original source bytes.

The SAT Competition 2026 source is more promising for discovery: https://satcompetition.github.io/2026/downloads.html publishes `track_main_2026.uri` identifying actual selected benchmark files; https://satcompetition.github.io/2026/benchmarks.html states the declared variable count must equal the exact number appearing in each CNF. The index is a source pointer, not by itself a verified particular 256-variable pair. Benchmark retrieval, actual variable activity, file hashes, and externally checkable outcomes are still missing.

The 2026 competition output contract (https://satcompetition.github.io/2026/output.html) requires SAT models when applicable and UNSAT certificates for designated tracks, with independently checked proof pipelines. This is an appropriate independent benchmark-verification standard; we did not receive the specified files or a verified proof.out for a qualifying 256-variable pair.

**Admission predicates for one immutable original CNF byte sequence `b`:**

1. Source and immutable identity: a documented external publication and raw SHA-256 of acquired original `b`, with stable retrieval URL, timestamp, publisher, and license.
2. Format: exactly one `p cnf 256 m` declaration, parsed without rewriting `b`; exactly `m` terminated clauses and legal literals.
3. Activity: the set of variable IDs used in actual clauses must equal `{1,…,256}`; a declared header alone is insufficient.
4. Outcome: for SAT, check an independently supplied satisfying assignment against every clause in the original input; for UNSAT, independently check a proof certificate against the *identical* source bytes using an identified pinned checker.
5. Methodology: preserve a separate immutable source-input digest, solver digest, proof digest, checker digest, output log and adverse controls. A solver's one-line claim of UNSAT without a checkable proof is not sufficient.
6. Enforce all of these for both the SAT and UNSAT members; until then **do not admit the pair**.

The existing four 256-variable locally archived finite UNSAT cases and 3,076-step replay are not independently sourced externally. They remain valid bounded internal evidence and cannot substitute for this acquisition gate.

## 4. Clarity Pi semantic boundary

For any nonzero real `x`, the real-arithmetic normalization `N(x)=x/x=1` is exact. Thus `sqrt(pi)/sqrt(pi)=1` is exact, but `sqrt(pi)=1` is false. As `N(2)=N(sqrt(pi))=1` with different inputs, normalization is many-to-one and loses object identity. It is not a truth or evidence-admission procedure.

The repository's public Clarity gate defines `K = R AND I AND E`, with `E` explicitly **independent Echo**; the archived kernel separately evaluates finite CNF formulas using `0 / U / 1`. A formal bridge would need **typed claims, source-bound evidence, checker semantics, independence assumptions, contradiction handling, falsification persistence, and correspondence proofs**. No such equivalence theorem was completed here, and the original kernel is not modified.

## 5. FIDELITY controls and limits

1. **Identity:** no source bytes changed; all original archive and kernel hashes were rechecked.
2. **Provenance:** a Debian-listed digest identifies an expected artifact but does not prove its acquisition; SATLIB's 250-variable origin cannot be relabeled.
3. **Chronology:** 030-A and 030-B remain separate branches from 029; later Git commits do not alter receipt parentage.
4. **Independence:** published sources guide acquisition; actual independent model/certificate checks remain to be performed.
5. **Method/Object Separation:** finite UNSAT derivations do not establish general computational complexity results.
6. **Non-Expansion:** no solver run, mathematical breakthrough, adoption, blockchain operation or signing is inferred.
7. **Falsification Persistence:** negative controls and rejected candidate classes remain attached to the research record.
8. **Uncertainty:** every unmet gate remains **0 · HOLD**.

## 6. Disposition

**Verified now:** independently cited Debian publisher expected size/hash, existence and eligibility limitations of SATLIB 250-variable sets, SAT Competition 2026 independent benchmark/model/certificate protocol, and a clean rerun of the unchanged original local archive replay.

**Not established:** receipt-chain merging; external original-byte fully active 256-variable SAT and UNSAT pair; any independently checked external SAT model or UNSAT proof; actual CaDiCaL binary receipt/execution; fair independent solver benchmark; a semantic theorem equating normalization and knowledge; P vs NP solution; OpenAI research adoption; a validated Block `−1` pre-genesis artifact.

**Result:** `0 · HOLD`. The present paper is a versioned evidence-admission and source-acquisition update, not a new Experiment 030/031/032 archive, formal proof, external replication, or new accepted solver result. Any future true experiment must identify its **single exact parent archive** and retain all non-chosen sibling evidence as historical records.

## References

- Richard Stein / REIK-TCGE, Audit 031: https://github.com/eternalimit/chatgpt/commit/e027c9b4e2b9044fb8c8b0bb9808844f1198691f
- Clarity canonical REIK root: https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md
- Clarity Pi mathematical working paper: https://github.com/eternalimit/chatgpt/blob/main/research/2026-10-09-clarity-pi-reik-hash-ledger-working-paper.md
- Debian CaDiCaL exact package SHA-256: https://packages.debian.org/forky/amd64/cadical/download
- SATLIB benchmark inventory: https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html
- SAT Competition 2026 benchmark index: https://satcompetition.github.io/2026/downloads.html
- SAT Competition 2026 benchmark contract: https://satcompetition.github.io/2026/benchmarks.html
- SAT Competition 2026 proof/model contract: https://satcompetition.github.io/2026/output.html
