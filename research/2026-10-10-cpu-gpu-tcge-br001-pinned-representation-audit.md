# CPU / GPU / TCGE — BR-001 Exact-Byte Handoff Audit
**Research originator/project owner:** Richard Stein  
**Date:** 2026-10-10 (Pacific)  
**Research state:** **0 · HOLD / DROP U**  
**Scope:** exact saved byte identity and evidence-gate controls, NOT physical GPU hardware or scientific Echo.

## Frozen source and explicit boundary
1. Historical `eternalimit/chatgpt` September 24 continuity commit `fe19e72e86ce15d204d8998917810cd4216bceae`, file `research/PRE_TCGE_TO_2026-09-24_EXPERIMENTAL_CONTINUITY.md`, Git blob SHA-1 `aa3d3f64ab5060705de4e0f20e5d356453dacc38`. This is explicitly a **retrospective continuity reconstruction**, not a verbatim original execution log. It reports a September 23 CPU-oriented sequence `DESIGN -> FREEZE -> BUILD -> BLOCKED`, then image-generation routing after `Geelneratw an image`. Do not overwrite CPU BLOCKED by GPU routing.
2. The same pinned repository tree contains the saved `GETHUB_dynamic_gpu_artifact.html` and external `.sha256` sidecar. **This is a saved HTML representation**. The original Sept. 23 generated-image bytes and source input/execution trace have **not** been recovered, and no original prompt/image linkage to this HTML has been established.
3. The later `eternalimit/clarity` comparison commit `99439a1b1e0a12c3a9ac087a0aeff869c466edc5` is dated later and cannot retroactively serve as September 23 execution evidence.

## New independently reproduced source-byte checks
Pinned source: `https://github.com/eternalimit/chatgpt/blob/fe19e72e86ce15d204d8998917810cd4216bceae/GETHUB_dynamic_gpu_artifact.html`.

- Exact artifact size: **2,988 UTF-8 bytes**.
- Original sidecar's reported SHA-256: `64706f78f09b4374efb6b0053332def5fed6dd50ac477be947a85a029537ea7b`.
- Independently recomputed SHA-256 over the recovered exact HTML bytes: **MATCH**.
- Git blob SHA-1 over `b"blob " + ascii(len(bytes)) + b"\0" + bytes`: `3d7420d7b8ac274f196384233b2b681927b71136` — **MATCH** against pinned GitHub blob.
- Sidecar Git blob SHA-1 from pinned GitHub: `0bcdaf77b3bc8a70475b1817101475f71ce4cfd1`. Different object and algorithm from the HTML SHA-256.
- The HTML explicitly defines the GPU path as a **functional representation role**, not proof of hardware execution, external provenance, knowledge, or Echo. It distinguishes GETHUB from GitHub.
- Bounded local verifier `verify_cpu_gpu_tcge_handoff.py`: **14/14 PASS**, including source mutation rejection, substituted SHA-256 rejection, altered Git-blob rejection, 37-character SHA-1 incompleteness, missing provenance, unavailable independent Echo, and historical CPU BLOCKED preservation.
- Local verifier SHA-256: `c45517763b85e2cd89c6f95e35afd5e7d50f8c7517cb7b56449a9a8abd1e3f78` (script not embedded in this Git commit).
- Local results JSON SHA-256: `67d92d9891a0c78c5094db52179489bbde6e41e69af290e1ff8d2710c0d3f607`.
- Local paper SHA-256: `de6a8e5a9abc50fbdbbf92bccdcbc1f7893189a86aacb32b5ba9247f3e52e889`.
- Local categorized ledger SHA-256: `b7978e94f524288621bca2015aa3d95c57f9ea18d87749b9f2798dbf765ec9ff`.

### Short independent reproduction
Fetch the **exact raw file pinned at the historic commit** and its sidecar, then run:
```python
import hashlib
from pathlib import Path
b = Path("GETHUB_dynamic_gpu_artifact.html").read_bytes()
assert len(b) == 2988
assert hashlib.sha256(b).hexdigest() == "64706f78f09b4374efb6b0053332def5fed6dd50ac477be947a85a029537ea7b"
git_blob = hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()
assert git_blob == "3d7420d7b8ac274f196384233b2b681927b71136"
```

## Claim-specific CPU / GPU / TCGE evidence gate
- **CPU:** deterministic byte digest computation and type checks succeeded for the archived HTML file only. This does not establish original historical CPU execution.
- **GPU:** exact saved HTML representation bytes were checked. Rendering, image generation, and actual physical GPU invocation were **not** verified. The frozen 2026-09-23 image-output artifact remains missing.
- **TCGE:** `R = direct evidence; I = inference; E = independently obtained validation; K = R AND I AND E; H = I AND NOT K`. R is satisfied narrowly for file-byte identity; no independent third-party Echo supports historical correspondence or physical claims. **K remains unadmitted for those claims**.
- Same-environment digest agreement is not independent Echo. Communication is not execution. Representation is not reality. Source hash is not proof of scientific validity.

## Historical hashes / branch boundaries
- Original immutable REIK/TCGE `kernel001.py` **historical** SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`; original kernel not rehashed or modified during this test.
- REIK root Git blob SHA-1 `f6cf9d97ab2be5322336857b7624978acec75f51` (GitHub read).
- Preserve the **distinct** experiment histories `030/280`, `030/282`, `031/290`, `031/A294`, `031/B294` without merging.
- Incomplete historical 37-character SHA-1 `3db9e3f67f447bb57c5831e76d51d7688e9da` and the distinct, unrecovered **40:40** correlation acceptance rule remain **HOLD**; CORE•40 orientation is a separate symbolic construction.
- Preserve all eight FIDELITY principles: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**.
- Spider -> TCGE Gate -> Monkey Bus -> Hook -> Web/Net -> Receipt -> Echo is a declared interface contract. No wallet access, transaction, signing, hook dispatch, or third-party delivery was performed.

## Falsification and next gate
The 14 controls are local logical/byte tests; they **do not** constitute independent scientific Echo. The strongest supported conclusion is exact digital preservation of one historically committed representation file. We cannot infer original GPU behavior, exact CPU/GPU pair equivalence, cross-lane hardware execution, a universal correspondence theorem, or physical-universe inheritance.

Next: obtain actual original September 23 CPU input/output and GPU prompt/output bytes with independently fixed timestamps; freeze a true pair before comparison; separately verify hardware tool trace and representation meaning; run mutation, false reconstruction, contradictory output, order-dependence and missing-witness controls; seek genuinely independent external Echo. Until then **0 · HOLD**. Do not rewrite any earlier blocked or negative result.
