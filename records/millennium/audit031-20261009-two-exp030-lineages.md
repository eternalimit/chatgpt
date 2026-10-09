# REIK/TCGE Evidence Audit 031 — two Experiment 030 archives

Date: 2026-10-09. Canonical status: **0 · HOLD** for unresolved external or general claims.
Scope: historical Block -1 reference, unchanged REIK/TCGE kernel, Experiment 019–029 receipt lineage, both original Experiment 030 archive variants, and October 9 Clarity Pi Math working paper.
Attribution: Richard Stein / REIK/TCGE; technical read-only verification with AI assistance.

## Exact original-byte audit (local, read-only)
The auditor independently calculated SHA-256 from **original local Library ZIP bytes**, checked ZIP CRCs and declared file hashes, replayed ledger events using its own code, and verified four finite UNSAT resolution certificates. It did **not** run archived Python scripts or publish private ZIP payloads.

- Unchanged `kernel001.py` SHA-256 **MATCH**: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Experiment 029 original ZIP (580,916 bytes) SHA-256 **MATCH**: `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`.
- Parent 029 manifest SHA-256 **MATCH**: `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`. Parent 270-event tip **REPLAY PASS**: `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`.
- **Candidate A: 282-event archive**, Library filename `millennium_reik_3sat_exp030(1).zip` (602,740 bytes). ZIP SHA-256 **MATCH**: `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942`. Manifest SHA-256 **MATCH**: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`. 12 new receipt events **REPLAY PASS**, final tip `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5`. Public summary: https://github.com/eternalimit/chatgpt/commit/b5578bc70bfc6333c7ea1eba84c404979760edc8.
- **Candidate B: 280-event archive**, Library filename `millennium_reik_3sat_exp030.zip` (675,433 bytes). ZIP SHA-256 **MATCH**: `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed`. Manifest SHA-256 **MATCH**: `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`. 10 new receipt events **REPLAY PASS**, final tip `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074`. Public summary: https://github.com/eternalimit/chatgpt/commit/8b580d46eb310398591fde1c16b316fe5c82c31a. The published manifest at `research/millennium/experiment030/manifest030.json` was independently rehashed and matches.

**Reconciliation:** Both 030 archives embed identical exact Experiment 029 bytes. A and B have different event genesis hashes and are **sibling archive successors**, not a verified A→B or B→A receipt chain. GitHub commit ancestry places the A summary before B, but public commit chronology does not change original archive parentage. Preserve both without splicing their receipt tips.

## Finite proof, chronology, negative controls
- Recomputed all 270 inherited event links: 019=42, 020=24, 021=36, 022=40, 023=36, 024=24, 025=20, 026=12, 027=12, 028=12, 029=12. Verified genesis digests, event sequence, event SHA-256, chained hash tips, parent manifest links and declared member digests.
- Independently checked four archived fully-active 256-variable **finite** UNSAT resolution derivations: `cycle256_unsat` (1023), `cycle256_unsat_perm022` (1023), `cycle256_unsat_signed023` (1023), `seeded_core_unsat_256` (7). **3076 resolution steps PASS**. This proves only those finite archived formula instances UNSAT.
- Seven in-memory falsification controls **PASS**: edited event, swapped event order, corrupted event hash, corrupted genesis parent, wrong final resolvent, wrong pivot, changed input problem bytes. The archives' own 12/16 admission-control suites were **not independently re-executed**.
- Auditor and machine report created locally but **not uploaded**: SHA-256 script `d2d684df5b7d674a3df6025d149af2ba8802e9986578566ecb4a40ada63b36aa`; machine-readable results `fa156d496e056abca351f2f6c4f99da7807bf207eb9be6b1060adf25e602716f`; full public-safe report `76e73f378aa4a56633a00d6d120a59809d16d2cbde392a7a244efeb759f6cb3b`.

## Semantic and external boundaries
- The Block -1 reference is an index/pre-genesis marker; no authenticated original pre-genesis artifact was established.
- Canonical Clarity root: https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md. `K = R AND I AND E` with independent Echo required. This is not a new proof of equivalence to the preserved CNF kernel's `0/U/1` semantics.
- Clarity Pi Math paper: https://github.com/eternalimit/chatgpt/blob/main/research/2026-10-09-clarity-pi-reik-hash-ledger-working-paper.md. `sqrt(pi)/sqrt(pi)=1` is exact; deriving evidentiary validity from this identity requires a separate formal bridge, currently **HOLD**.
- Preserve **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**.
- **HOLD:** original independent fully-active 256-variable SAT/UNSAT pair and independently checked source/certificates; actual CaDiCaL 2.1.3-3 AMD64 acquisition and executable verification; fair dedicated solver benchmark; externally replicated methods and independent Echo; general polynomial-time SAT algorithm, P vs NP; any blockchain transaction, external signing, or OpenAI adoption.
- A signed Git commit is versioned publication, not scientific proof. No private keys, private archive contents or fabricated external actions are included. **No evidence → no advance.**
