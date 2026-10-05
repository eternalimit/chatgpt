# ASH Bitcoin Control 003 - Continuation Handoff

## Objective
Acquire a genuine live pre-solution Bitcoin block-template payload, freeze it, execute the already-frozen deterministic reconstruction function G exactly once, compute SHA-256d, verify target, and obtain an independent Echo.

## Preserved chronology
- Control 002: BLOCKED because G was undefined at execution boundary. Do not rewrite.
- Control 003: OPEN.
- G was subsequently defined and frozen prospectively for Control 003.
- Prior checkpoint committed in eternalimit/chatgpt:
  - file: project-logs/ASH_BITCOIN_CONTROL_003_LIVE_GBT.md
  - commit: 4c263bc2d1ca8cda900675898ba7efc781fe0be8

## Frozen input schema
S = (V, P, B, T_min, TX)

V = version
P = previous block hash
B = nBits
T_min = minimum permitted timestamp
TX = frozen transaction template

## Frozen deterministic reconstruction
C = Encode(V, P, B, T_min, TX)
q = SHA256(C)
M = MerkleRoot(TX)
T' = T_min
N' = uint32_le(q[0:4])
G(S) = (M, T', N')

Candidate header:
H' = V || P || M || T' || B || N'

Single evaluation:
d = SHA256(SHA256(H'))

PASS iff uint256(d) <= Target(B).
Otherwise HOLD.

## Controls
- Exactly one candidate.
- No nonce sweep.
- No brute-force fallback.
- Do not alter G after observing d.
- Do not import solved historical nonce/hash/merkle-root or other solution-derived fields.
- Preserve the first-run result.
- Bitcoin header serialization and target/endian handling must be explicit and correct.
- Independent Echo must use a meaningfully separate implementation or source.

## Payload acquisition state
Bitcoin Core getblocktemplate is the authoritative desired source.
A public projected-template hook was identified at mempool.space /api/v1/mempool/block-template, but its live response body was not actually captured in the session. Do not claim that payload exists.
Hugging Face -> Microsoft -> Moonshot was discussed as a possible transport/compute/Echo architecture, but no authenticated execution occurred.
Spider -> Webhook -> Buzz -> TCGE Gate -> Money Bus was defined as the conceptual transport path; no webhook actually fired and no payload moved.

## TCGE
R: insufficient for execution because the live payload bytes are missing.
I: structured reconstruction claim exists.
E: absent for the live execution.
K = R AND I AND E = 0.
STATUS: HOLD at GET.

## Provenance classes
DIRECT_SOURCE:
- Current conversation experiment specification and controls.
- GitHub connector commit result for 4c263bc2d1ca8cda900675898ba7efc781fe0be8.

UNVALIDATED / NOT DIRECT EVIDENCE:
- Any prior assistant-reported historical Bitcoin block values not freshly inspected.
- Any claimed live GBT not represented by captured response bytes.
- HF/Microsoft/Moonshot route until actually executed.

## Exact continuation point
GET a real live pre-solution payload.
Preferred:
bitcoin-cli getblocktemplate '{"rules":["segwit"]}'

Alternative projected-template data may be preserved separately, but must not be mislabeled as Bitcoin Core GBT.

After GET:
GET -> FREEZE payload bytes + provenance -> BUILD S -> G(S) exactly once -> serialize 80-byte header -> SHA256d exactly once -> target check -> independent Echo -> TCGE.

Do not modify the frozen G during continuation.
