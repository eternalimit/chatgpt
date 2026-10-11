# ABC–K4 v0.2: independently coded local audit and bounded K5 falsification

Research date: 2026-10-11. Derived mathematical work only; original REIK/TCGE kernel immutable. The word "independent" below refers to **separate local program implementations** unless an externally administered witness is explicitly specified.

## Input anchors
- Requested v0.1 original ZIP exact SHA-256: `a31bb3ae0c858f7ae1840bef5184dcb04b7e98d01374ba4374409009ef9e5cc0`; local source ZIP rehashed MATCH and six original member hashes verified.
- Requested GitHub parent commit `b04ddc073d56bf1590111510035aa3662e11c00d` fetched and its `research/2026-10-11-abc-k4-3bit-4node-6pair-v01.md` source content read back (blob `71369eeb0c0e9ee7d61676313aa1ef7177fbd300`).
- Original programs re-executed from extracted byte-preserved ZIP: Python **14/14**, Node **14/14**; exact original result SHA-256 MATCH both; eight state rows agree exactly.
- v0.2 full research ZIP `ABC_K4_v02_verified_research.zip`: SHA-256 `92a7d4c2f18ffa10ead4d46c0b4acaea602a9895d91f1b98cddd7462c89c3989` (21,596 bytes, 9 entries). This is a **local conversation artifact**; not uploaded to GitHub by this document. Contains unchanged v0.1 ZIP, research README, both v0.2 source scripts, results, SHA256SUMS, audit receipt, and replay script. Extracted in separate directory, `bash replay.sh` PASS.

## Exact 3-bit theorem and independently enumerated counts
Define `M1={AB,CD}, M2={AC,BD}, M3={AD,BC}`. For `b=(b1,b2,b3)`, set `Phi(b) = union(Mi when bi=1)`. The adjacency matrix is

```text
0 b1 b2 b3
b1 0 b3 b2
b2 b3 0 b1
b3 b2 b1 0
```

Every vertex has equal integer degree `k=b1+b2+b3`, and the edge count is `2k`. Conversely, equal degrees force opposite-edge indicators equal: `AB=CD, AC=BD, AD=BC` (subtract the four integer degree equations). Hence **Phi bijects the eight 3-bit states with all eight labeled regular spanning subgraphs of K4**. All 64 labeled edge subsets were enumerated, so **56** are excluded; degree histogram **1,3,3,1**. This is a labeled set correspondence, not physical dimensional identity or a theorem about all graphs.

- Counterexample single edge AB: degree sequence (1,1,0,0), not encoded.
- Counterexample triangle ABC: degree (2,2,2,0) has identical parity at all vertices but is not degree-regular.

## Coordinate geometry is an independent premise
The four vertices `(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)` have six squared distances equal to 8. Scalar triple product from the first vertex = **-16**, Gram determinant = **256**, tetrahedral volume = **8/3**. A coplanar placement of the same abstract K4 has volume zero, so 3D geometry is not implied by edge labels, graph completeness or the number of bits.

## E1. Falsifiable 4-bit K4 extension (one possible, noncanonical model)
Given `a,b,c,d in {0,1}`, modify only AB: `AB=a XOR d, CD=a, AC=BD=b, AD=BC=c`. This encodes **16 distinct K4 edge subsets** of the 64 possible. Exactly **8** are regular (when `d=0`), 8 nonregular, and 48 edge subsets remain excluded. Four bits do not universally control all six edges.

## E2. Falsifiable 5-node K5 extension
There are `C(5,2)=10` possible edges and `2^10=1024` labeled edge subsets. By the handshake lemma, a 5-vertex regular graph must have even degree, namely 0, 2, or 4. Thus the complete enumeration is **1** empty, **12** Hamiltonian 5-cycles (`4!/2`), and **1** complete: **14** regular graphs. An independent JS implementation also enumerated the 24 anchored cycle permutations and deduplicated reversals to the same 12 cycles. There is no spanning perfect matching on an odd number of vertices. Therefore the naive `2^(n-1)` regular-graph count extrapolation is **false at n=5**: `2^4=16 != 14`.

Concrete noncanonical 4-bit encoding: split K5 into disjoint Hamiltonian cycles `C1=AB,BC,CD,DE,AE` and `C2=AC,CE,BE,BD,AD`. Bits `p,q` select the cycles; `r` toggles AB with XOR, and `s` toggles AC with XOR. Exactly **16** distinct output graphs arise; **4** are regular (when `r=s=0`), **12** are nonregular. Thus only **4/14** regular K5 graphs are covered by this explicit encoding. A partial, arbitrary lookup could assign 14 codewords to the 14 regular K5 graphs and reject two; this is not a natural bijection of all sixteen 4-bit values.

## Actual local execution receipt
- Original source: Python **14/14**, Node **14/14**, result bytes exactly reproduced and manifest intact.
- New Python adjacency-matrix/edge-mask verifier: **23/23 checks PASS** (all K4/K5 edge subsets, both 4-bit encodings, falsifying cases, Gram determinant).
- New Node.js edge-bitset/permutation verifier: **22/22 checks PASS** (complete enumerations, separate cycle listing, tetra triple product, bounded encodings).
- Cross-implementation cardinalities: K4 regular=8; K5 regular=14; 4-bit K4 unique=16 / regular=8; 4-bit K5 unique=16 / regular=4.
- During v0.2 development an initial *test harness assertion* incorrectly excluded any 5-vertex graph containing even one degree-1 vertex. That is not the relevant property. It was corrected to exclude graphs in which **all five vertices** have degree 1; entire 23-check Python suite then passed. Record preserved under Falsification Persistence rather than hiding the failed first attempt.
- Full local receipt SHA-256: `57881e0c402774e1995b4a61518217702df3338e38d81c76f2baf62b73ac02e1`.
- The full v0.2 ZIP itself was rehashed and an **isolated extraction** successfully ran `bash replay.sh`, verifying all original/new source and output hashes. No remote CI or external witness was performed.

## Boundaries, FIDELITY, Echo and HOLD
Historical reported original REIK/TCGE kernel SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` — *not rehashed from original bytes in this work*. Kernel not included, edited, or executed. This audit does not establish physical, cosmological, or other REIK/TCGE assertions and keeps historical Experiment 030/031 lineages separate.

Eight FIDELITY principles preserved: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.

**Independent externally administered Echo: HOLD. Historical original-byte kernel verification: HOLD. DROP U for unsupported generalization; governance state 0 · HOLD.** Local mathematical PASS never upgrades these independent gates.

Next action: independently controlled witness obtain parent ZIP from separately trusted source, verify bytes and GitHub source, execute both independent implementations under separately administered infrastructure, attest original trace and timestamp with independently controlled key, and publish non-secret signed receipt and conflicts. No further epoch advancement merely from same-operator testing.
