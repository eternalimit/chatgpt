# ABC-K4 model v0.1 — 1 unit, 3 bits, 4 nodes, 6 pairs

Research date: 2026-10-11. Derived mathematical model; separate from and does not modify any REIK/TCGE historical kernel.

## Definition
Let V={A,B,C,D}. K4 has six unordered edges AB,AC,AD,BC,BD,CD. Define the three disjoint perfect-matchings M1={AB,CD}, M2={AC,BD}, M3={AD,BC}. For each b=(b1,b2,b3) in {0,1}^3, Phi(b) selects the union of Mi whose corresponding bit is 1.

## Theorem
Phi is a bijection between the eight 3-bit Boolean states and the eight labeled spanning **regular** simple subgraphs of K4. Every vertex has degree k=b1+b2+b3 and each graph has 2k active edges. The 64 possible edge subsets of K4 include 56 nonregular graphs not represented by this constrained encoding.

Proof: Each selected perfect matching contributes exactly one incident edge at each vertex, so the forward map yields equal integer degrees and is injective because matching edge sets are disjoint. Conversely, write edge-indicators x=AB, y=AC, z=AD, u=BC, v=BD, w=CD. Equal vertex degrees imply (y-v)+(z-u)=0; (x-w)+(z-u)=0; (x-w)+(y-v)=0. Over integers this forces x=w, y=v, z=u. Therefore any regular subgraph is a union of the three opposite-edge matchings and lies in the image. This is **integer degree** equality, not parity alone.

## Exhaustive state table
|Bits|Active edges|Count|Vertex degree|
|---|---|---:|---:|
|000|none|0|0|
|001|AD BC|2|1|
|010|AC BD|2|1|
|011|AC AD BC BD|4|2|
|100|AB CD|2|1|
|101|AB AD BC CD|4|2|
|110|AB AC BD CD|4|2|
|111|AB AC AD BC BD CD|6|3|

The degree histogram is 1,3,3,1 for k=0,1,2,3. One-edge graph AB is a counterexample to universal representability; it has degrees (1,1,0,0). The result is label-dependent and contains only four unlabeled isomorphism classes.

## Distinguish graph from geometry
K4 is planar as a graph and cannot alone establish 3D Euclidean space. Assigning A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1) separately realizes a genuine regular tetrahedron: all six squared edge lengths are 8, and determinant of the three edge vectors based at A is -16, giving volume 8/3. Its four boundary triangular faces satisfy 4-6+4=2. Graph and coordinate statements have separate premises.

## Locally executed evidence
- Python 3.13 constructive/matching-based implementation: **14/14 assertions PASS**.
- Node.js 22 exhaustive/filter-based implementation: **14/14 assertions PASS**.
- Cross-implementation equality: **8/8 state rows identical**.
- Exhaustive four-vertex enumeration: **64 labeled edge subsets**, **8 regular**, **56 excluded**.
- ZIP with source scripts, result JSON, original local paper, SHA256SUMS and receipt: SHA-256 `a31bb3ae0c858f7ae1840bef5184dcb04b7e98d01374ba4374409009ef9e5cc0`.
- Original Python script SHA-256 `8930ccc41262b65c3f226c1c33d9668cf288cfdb8d0a23ce3962de8d536e7579`.
- Original Node script SHA-256 `2dcfaf62b6981c646b21710f0dc00b32fea0e023f7bb31663c8a9f36c82b4baa`.
- Local receipt SHA-256 `79de0a48e5a0ec6d827d1ae8f946b4573a540f2868c23c0ab15f33fe3bbb7ddc`.
All local SHA256SUMS and compressed ZIP entries passed verification. Scripts/results remain in a locally delivered ZIP, and are not implied to exist in GitHub by this report.

## Governance and evidence boundaries
Historical original REIK/TCGE kernel SHA-256 **reported, not rehashed here**: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.

Preserve eight FIDELITY principles: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. This record does not modify the kernel or conflate unrelated experiment branches. Local implementations are not independently administered external Echo. **External Echo = HOLD, original-byte kernel revalidation = HOLD, DROP U for unsupported extensions; state 0 · HOLD.** No physical/cosmic/sacred-geometry or historical copying claim follows from the theorem.

Next gate: independently controlled witness obtains original public source bytes, reproduces calculations on separate infrastructure with independent trust root, checks provenance and conflicting-source evidence, and reports signed/dated receipt. Do not advance before evidence.
