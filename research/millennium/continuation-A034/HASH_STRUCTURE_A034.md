# REIK/TCGE A034 — Hash Structure and Provenance Boundary
**Date:** 2026-10-09  
**Research attribution and first-party ownership claim:** Richard Stein (not an independent legal ownership determination)  
**State:** 0 · HOLD for unverified claims.

## Original unchanged kernel
- Source: `kernel001.py`, 4,299 bytes; five prior archived sources rechecked (no execution, no modification).
- Original SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`
- FIDELITY: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.
- REIK public root gate: `K=R AND I AND E` where `E` must be independently validated. Kernel semantics are not redefined.

## Parent 029 exact inherited archive identifiers
- ZIP SHA-256: `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`
- Manifest SHA-256: `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`
- 270-linked receipt tip: `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`

## Five physically distinct experiment variants (never join chains)
| Independent archive | Events | Full ZIP SHA-256 | Manifest SHA-256 | Receipt tip SHA-256 |
|---|---:|---|---|---|
| 030/280 | 280 | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` |
| 030/282 | 282 | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` |
| 031/290 (from 030/280) | 290 | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768` |
| 031/A294 (from 030/282) | 294 | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384` |
| 031/B294 (from 030/282) | 294 | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f` |

## A032/A033 Git object references (not historical original ZIP digests)
- A033 paper commit: `7829497d17678b81bc5c131bb9bb8f319db99339`
- A033 hash structure commit: `66f782331b9126d07b6c3d05c1d28d26046e465b`
- A033 receipt commit: `dd8be7f0bf92f25d84a93db1b536309b121bd3da`
- A032 paper Git blob SHA-1: `4f2f483d5115a758a1fe22410ef85d0ddc57a1aa`
- A032 corrected hash Git blob SHA-1: `988410e53bdfd9ae2851756d3c73781e5de1327c`
- A032 receipt Git blob SHA-1: `c9ef247e61921af4885fd81cbe7db52109d3a411`

## A034 new EXTERNAL original SAT acquisition and witness
- Independent external source: [16-Queens pinned original](https://github.com/andricicezar/sat-solver-dafny/blob/418e5cbb1e7a311fec2c15913c0c504ec603ca91/benchmarks/queens16.cnf)
- Git blob SHA-1 (content identity): `85b9071d8399839eff2352bb22315b5940bcda7c`
- SHA-256 recomputed from exact **71,945 ASCII source bytes**: `c5177c8e6523ddd9378b3b864d52fcf73b81c0a92a033433cc37e5450fa1fcd5`
- DIMACS `p cnf 256 6336`: all variable IDs 1..256 active; 6,320 binary clauses; 16 16-literal clauses.
- Complete model TRUE IDs: `[1, 19, 37, 50, 77, 89, 110, 124, 143, 150, 176, 183, 196, 219, 232, 250]`; every other variable FALSE.
- 6,336/6,336 clauses independently satisfied; mutation of variable 1 rejected by original CNF.
- Source bytes retrieved fully from fixed GitHub refs in three repos; no copy of original file included in the public research ledger. The original is CNF but **not a 3-SAT-only instance**. Git blob SHA-1 is different from SHA-256.

## A034 local adapter independent test results
- Previously published A033 adapter exact source SHA-256: `884e7ee3e54b336c3d68b8a1f8eea782038b6f15bbcbd2e9afecef15ca436d52`
- Independent A034 black-box audit source SHA-256: `5228c0e15d07be3ecd3d762373728075e68fa7b639ce02e50fa885e1377ab6e2`
- Independent A034 audit result SHA-256: `4fab058d8becd971d06feddd41981556844301145c4fba32287920d3f908cc10`
- Original archive A034 replay receipt SHA-256: `ba32ffaf4415da4228f510c8f1adede8e550588b412de659062e303828301e86`
- A033 adapter unchanged rerun output SHA-256: `2c954ada9ad272aeeb16da4308098407b9d44ab1df505441e14e7aed15f9cb9c`
- Eight Boolean gate rows, four positive cases, 10 negative mutations, conflicts and missing evidence checked.
- **Falsification/limitation:** an actor can self-assert `independent_attestation=true` with different source/checker origin strings; the adapter then emits `CONFIRMED` without independently authenticating the checker. The adapter is an evidence-state model, **not an independent third-party Echo authenticator**. Remains HOLD.

## CaDiCaL 2.1.3-3 AMD64: publisher metadata only
- Exact Debian package: `cadical_2.1.3-3_amd64.deb` 467,080 bytes.
- Debian publisher expected SHA-256: `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`.
- Actual package and executable bytes not obtained: DNS resolution failed. No executable SHA-256 and no CaDiCaL run. [Debian publisher URL](https://packages.debian.org/sid/amd64/cadical/download).

## Explicit HOLD
- External original-byte 256-variable UNSAT CNF with independently checked unsatisfiability proof: NOT ACQUIRED.
- A new fair CaDiCaL benchmark: NOT RUN.
- Claimed general SAT algorithm/P versus NP solution, crypto signing/Bitcoin anchor, externally certified Echo or OpenAI/community adoption: NO independent evidence.
- Never substitute synthesized or relabeled examples or unpublished original ZIPs. Preserve `0 · HOLD`.
