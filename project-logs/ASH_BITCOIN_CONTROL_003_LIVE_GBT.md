# ASH Bitcoin Control 003

Status: HOLD at live GBT acquisition

## Preserved chain

002: BLOCKED
003: OPEN

GET -> FREEZE -> G(S) -> ONE CANDIDATE -> SHA256d -> VERIFY

## Frozen reconstruction function

Permitted pre-solution state:

S = (V, P, B, T_min, TX)

Canonicalization:

C = Encode(V, P, B, T_min, TX)

q = SHA256(C)

Reconstruction:

M = MerkleRoot(TX)
T' = T_min
N' = uint32_le(q[0:4])

G(S) = (M, T', N')

Candidate header:

H' = V || P || M || T' || B || N'

Proof test:

d = SHA256(SHA256(H'))

PASS iff uint256(d) <= Target(B)
Otherwise HOLD.

## Live payload requirement

The next admissible artifact is a genuine Bitcoin Core getblocktemplate response captured before the candidate is evaluated.

Example:

```bash
bitcoin-cli getblocktemplate '{"rules":["segwit"]}'
```

Required template fields include at minimum:
- version
- previousblockhash
- bits
- mintime
- curtime
- transactions
- height

Do not substitute solved historical nonce, solved block hash, solved merkle root, or other answer-derived fields.

## TCGE

R = live payload actually captured
I = structured reconstruction claim
E = independent verification path
K = R AND I AND E

Current status: HOLD until a real live GBT payload is acquired.
