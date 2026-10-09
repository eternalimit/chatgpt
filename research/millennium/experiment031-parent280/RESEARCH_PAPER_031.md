# Millennium Research Experiment 031: A Third-Implementation Finite Evidence Replay and Unresolved External 256-Variable SAT Admission

**Richard Stein** — REIK/TCGE framework originator; technical investigation and preparation with AI assistance  
**Research date:** 9 October 2026  
**State:** `0 · HOLD` for unacquired benchmark pair, CaDiCaL executable, and P versus NP.  
**Method:** Exact-byte archival replication, independent finite resolution derivation checker, chronological SHA-256 receipts, adversarial admission controls, and bounded external acquisition attempts.

## Abstract

We continue the immutable REIK/TCGE `0/U/1` partial-assignment framework using the exact 675,433-byte Experiment 030 ZIP with SHA-256 `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed`. The frozen kernel SHA-256 remains `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. A newly authored, read-only Experiment 031 verifier independently opens and checks nested predecessor ZIP archives, SHA-256 file manifests, the 280 historical chronological receipt links, and the four inherited UNSAT resolution certificates. All 3,076 individual resolution inference steps are reconstructed and checked, together with active-variable and final-empty-clause requirements. Sixteen new logical negative gate tests pass. The exact Debian repository page independently confirms publisher metadata for CaDiCaL `2.1.3-3_amd64` (467,080 bytes; expected SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`), but repeated binary acquisition attempts failed at DNS resolution; actual received-package and executable SHA-256 checks could not take place. The required independently sourced exact-original-byte fully active 256-variable SAT and UNSAT DIMACS inputs together with independent certificates were not acquired. We publish one bounded, local, append-only Experiment 031 successor and a new 10-event evidence chain. There were no new SAT solver executions or performance comparisons, and **P vs NP remains HOLD**.

## 1. Scope and falsifiable questions

The goal is not to modify or reinterpret the original evaluator, nor to present finite checks as a proof of a complexity-class statement. Our admission questions are:

**Q1.** Does the exact Experiment 030 ZIP bind to the user-provided SHA-256, and does its sealed manifest bind to `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`? **Yes.**

**Q2.** Can a new checker, not importing any inherited audit script, independently reconstruct the full 280-event history and 3,076 resolution steps? **Yes, for the finite objects actually present.**

**Q3.** Are there now two independent *original-byte* fully active 256-variable CNF benchmarks of opposite independently checked satisfiability status? **No; HOLD.**

**Q4.** Was Debian CaDiCaL `2.1.3-3_amd64` acquired, hashed, extracted, its executable hashed, and subsequently run with an independent checker? **No; HOLD.**

**Q5.** Do these experiments establish a general polynomial-time 3-SAT procedure or either possible answer to P versus NP? **No.**

These outcomes define a sharp boundary between local evidence replay and missing external admission.

## 2. Fixed theory and original implementation

Let F be a conjunctive normal form formula on Boolean variables, and a be a partial assignment. A clause is definitively false if every literal is assigned false; the entire CNF is definitively true if every clause has an assigned true literal. The original kernel reports:

\[
K(F,a)=\begin{cases}
0 & \text{if at least one clause is definitely false},\\
1 & \text{if every clause is already satisfied},\\
U & \text{otherwise.}
\end{cases}
\]

This is a three-way semantic classifier, not a three-valued replacement of Boolean input assignments in the standard SAT decision problem. `U` is unresolved, not an accepted or refuted theorem; it can later become `0` or `1`. Already-falsified clauses stay false when extending the partial assignment without changing previously assigned values; already-satisfied clauses stay satisfied. Those elementary monotonicity facts do **not** establish a polynomial upper bound on exploring unresolved branches. The actual archived `kernel001.py` is authoritative, rather than the displayed notation.

The retained REIK root provides **Reality** (direct evidence), **Inference**, an independent **Echo**, and **Knowledge**. In the archived contract, knowledge requires reality and inference and independent Echo, and missing evidence produces HOLD. This audit's new interpreter is an additional local Echo implemented separately, but it is *not* a claim of independent institutional or third-party peer review.

## 3. Exact original-byte parent and chronology

The recovered Experiment 030 ZIP was not regenerated for this audit: it is the original 675,433-byte file recovered in the working container, with actual SHA-256 `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed`. It embeds the identical Experiment 029 ZIP and its successive predecessors down through Experiment 023, as well as pre-023 receipts. `replay031.py` opens the nested ZIPs in memory, rejects duplicate or unsafe entry names, validates archive CRCs, independently hashes each raw file listed by the corresponding manifest, checks exact archive membership and sidecar manifest digests, and compares all original kernel bytes and SHA-256 identifiers. The original kernel SHA-256 is `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` in every inspected kernel-bearing generation.

| Historical Experiment | Reconstructed receipts |
|---|---:|
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
| 030 | 10 |
| **Total inherited** | **280** |

The checker serializes receipt objects to sorted-key, compact ASCII JSON before hashing. For each event i it verifies the declared preceding chain digest, event digest and new chain tip, using `SHA-256(previous_tip_bytes || event_digest_bytes)` for the transition. It checks cross-generation parent-tip and manifest bindings and per-event referenced evidence file digests. The exact inherited tip is `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074`. Ten additional Experiment 031 events are appended to a separately hashed and verified receipt chain, yielding **290 chronological historical-plus-new events**, without editing the 280 inherited events.

Cryptographic hash agreement demonstrates exact consistency with the trusted starting anchors; it does not by itself establish authorship, public anchoring, unforgeable timestamps, a signature, or independence of the original sources.

## 4. Four certificate reconstruction checks

The original resolution proof inputs are **historical internally archived formulae**, not independently sourced third-party SAT competition cases. For each of the four 256-variable UNSAT proof records, the new Experiment 031 implementation verifies: (a) SHA-256 of the associated original CNF JSON bytes against its certificate; (b) that every variable in `1..256` occurs in the input clauses, none exclusively an unused declaration; (c) that assumptions are empty; (d) that every resolution step names previously available parent clauses containing complementary pivot literals; (e) that the listed resolvent is precisely the set-theoretic union of nonpivot literals without tautological pairs or duplicates; and (f) that the concluding inference is the empty clause.

| Certificate | Independently replayed resolution steps |
|---|---:|
| `cycle256_unsat` | 1,023 |
| `cycle256_unsat_perm022` | 1,023 |
| `cycle256_unsat_signed023` | 1,023 |
| `seeded_core_unsat_256` | 7 |
| **Total** | **3,076** |

Because resolution is sound and an empty clause follows, each original *archived finite formula* is UNSAT relative to the checked statement. This is a proof about four individual formulas, not all inputs of size 256, not a solver speed comparison, not a statement about independent public benchmark data, and not a proof of P != NP or P = NP.

## 5. Admission and falsification controls

All eight FIDELITY principles are kept explicit: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, and Uncertainty**. They require exact-byte names and values to match, outside source provenance to remain distinct from generated fixtures, chronological predecessor links not to be skipped, a separate Echo, mathematical conclusions no stronger than the checked objects, persistence of earlier failure records, and unresolved claims not to be converted into accepted ones.

The new `negative_gates031.py` independently performs **16 deterministic negative admission checks**, including rejecting missing source bytes, missing pinned source, incorrect SHA checks, malformed DIMACS, declared-variable mismatch, 255 active variables despite a 256-variable header, absence of independently checked answer certificates, unknown status, wrong package hash, missing executable hash, no proof that executable came from the checked package, missing binary-version verification, absent benchmark pair, absent binary package, and synthetic content. It also sanity-tests two in-memory logical positives to ensure the Boolean gate is nontrivial; these fixtures are **never** promoted to independent acquisitions or benchmark results. This tests an admission predicate, not a SAT algorithm.

Archived Experiment 026–030 control outcomes are hash-verified within their sealed archives. We do not claim that Experiment 026's unavailable standalone runner has been re-executed. The 031 paper and receipt preserve earlier falsification and exclusion controls rather than overwrite them.

## 6. Independent external source discovery and original-byte gate

The SAT Competition 2024 website specifies legitimate DIMACS inputs via `p cnf <variable_count> <clause_count>`, actual occurrences of declared variables, clauses ending in zero, and prohibition of clauses containing both a literal and its negation. It also separately requires answer evidence: SAT assignments and UNSAT proof outputs for the main track. We identified the publisher's SAT Competition 2024 archive at Zenodo DOI `10.5281/zenodo.13379892`, but the listed `benchmarks.zip` is approximately **4.3 GB**, and neither a source-pinned, complete, original-byte fully active 256-variable SAT file nor the corresponding independently certified UNSAT file was acquired into this audit. Consequently **both inputs remain HOLD**.

A previously catalogued pinned GitHub `CNF1.txt` candidate has the declared header `p cnf 256 20864`; the available head lines include two-literal clauses. Declaration does not prove all 256 variables are active, does not prove exact-3-CNF, and does not identify an independently checked SAT/UNSAT pair. The candidate has not been locally admitted as an original-byte 256-SAT or 256-UNSAT benchmark in this experiment. The audit does not quietly change `250` to `256`, clone clauses, transform smaller formulas or relabel synthetic examples as published sources.

**Admission requires actual received original byte strings**, locally computed SHA-256, a pinned publisher or commit, syntactically complete DIMACS parsing, counts of truly active variables equal to 256, labels backed by independent evidence, a clause-checked SAT witness, and a separately checker-validated UNSAT proof. One case per outcome is a minimum, not a statistical performance study.

## 7. CaDiCaL identity: publisher digest versus locally received bytes

The Debian sid AMD64 package download page identifies `cadical_2.1.3-3_amd64.deb` with **467,080 bytes** and published SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`. Public package metadata was verified, but the package could not be received by the working environment. `urllib.request` failed DNS lookup, `container.download` failed, and separate `curl` attempts against Debian's FTP and Fastly endpoints returned DNS failure (`curl` exit 6). These failures are recorded as files inside the evidence bundle. No real `.deb` was acquired, so no received-package SHA-256 could be computed. No binary was extracted, hashed, independently identified, or executed. Z3 and any preinstalled solver cannot substitute for the specifically requested acquired CaDiCaL executable.

**Publisher expected hash is not a received-object hash.** When the package can be acquired safely and locally, the future protocol is: verify exact raw `.deb` SHA-256 and byte count; extract in an isolated unprivileged directory; compute SHA-256 of the resulting executable; check executable identity and dependency/execution constraints; separately install or verify independent proof-checker identity; only then perform bounded, predeclared original-byte SAT and UNSAT runs; validate model/proof independently. The current record cannot represent any such future steps as completed.

## 8. Results, limitations, and interpretation

| Statement | Evidence status |
|---|---|
| Original parent archive recovered with exact user-provided byte digest | PASS |
| Parent manifest, files, original kernel and nested archives | PASS |
| 280 prior chronological linked events | PASS |
| Four inherited resolution certificates / 3,076 steps | PASS |
| Sixteen independent 031 negative source/tool admission checks | PASS |
| CaDiCaL publisher's exact expected package identity | Verified metadata |
| Actual Debian package and executable received and SHA-256 verified | HOLD |
| Independently sourced fully active original-byte 256-variable SAT/UNSAT pair | HOLD |
| Independently checkable SAT witness and UNSAT proof for that pair | HOLD |
| New CaDiCaL benchmark, speedup or novel theoretical bound | NOT PERFORMED |
| Millennium P versus NP determination | HOLD |

No theorem or asymptotic claim follows merely from a successful finite replay. In particular, three-way partial-assignment semantics do not establish a polynomial-size search procedure over all unresolved branches. The latest independent checker is structurally distinct from archived checking scripts but was developed and executed in the same computational environment. Stronger external Echo would involve an independent human team or formally verified proof checker, separately controlled execution, and signed provenance statements, none of which is claimed here.

## 9. Reproduction, continuity, and publication

Extract `millennium_reik_3sat_exp031.zip` into a fresh directory. Using only the Python standard library, run `python replay031.py`, `python negative_gates031.py`, `python verify_integrity031.py`, and `python verify_receipts031.py`. The last two also check the new 031 manifest and events against exact evidence file SHA-256 records. The ZIP includes the full immutable 030 ZIP unchanged, new verifier source, new admission-control source, acquisition evidence and logs, and the full research manuscript. `manifest031.json` includes the SHA-256 of every payload file except the manifest and its own sidecar; `manifest031.sha256` binds the exact manifest bytes. A checksum text file distributed next to the ZIP independently names its outer raw digest.

Any public GitHub manuscript, manifest or receipt is an additional disclosure step; the local evidence archive by itself does not prove a publication, digital signature, trusted timestamp or transfer to a third party. Full original-byte adversarial benchmark evidence and CaDiCaL remains a future task. **Preserve HOLD, no arbitrary version replacement, and one forward append-only successor.**

## 10. Sources

1. Experiment 030 exact immutable nested archive (present in Experiment 031's `source/experiment030_immutable.zip`).
2. Debian package page: <https://packages.debian.org/sid/amd64/cadical/download>.
3. Debian package pool: <https://ftp.debian.org/debian/pool/main/c/cadical/>.
4. SAT Competition 2024 benchmark requirements: <https://satcompetition.github.io/2024/benchmarks.html>.
5. SAT Competition 2024 output and proof requirements: <https://satcompetition.github.io/2024/output.html>.
6. SAT Competition 2024 benchmark collection, DOI 10.5281/zenodo.13379892: <https://zenodo.org/records/13379892>.
7. Pinned potential 256-header case, *not an admitted result*: <https://github.com/domenlusina/SAT_SOLVER_PAJACA/blob/1a8be2a13d9c3a45903ddf07e918205b272baf1d/CNF1.txt>.

**Bounded conclusion:** Original immutable kernel preserved; exact parent and finite lineage PASS; 3,076 resolution steps PASS; independent original 256-variable data and executable HOLD; no novel SAT solver execution; **P versus NP HOLD**.