# Bitcoin / Ethereum — Proposed Binding Record

## Git source anchor

Source Git commit:

ebd4e14764e46dbd2287c774fa7c971773511a7d

Bound source record:

N_domino = 9 → 0

## Proposed binding

G = ebd4e14764e46dbd2287c774fa7c971773511a7d

G → H(G) → {
  Bitcoin transaction,
  Ethereum transaction
}

H(G) must be defined as an exact deterministic commitment before an on-chain transaction is claimed.

## Required completion evidence

A completed Bitcoin binding requires a verifiable Bitcoin transaction identifier:

TXID_BTC

A completed Ethereum binding requires a verifiable Ethereum transaction hash:

TXHASH_ETH

The corresponding transaction data must independently establish the intended commitment to H(G).

## Current state

GITHUB = BOUND
BITCOIN = UNBOUND
ETHEREUM = UNBOUND

## Boundary

GIT COMMIT ≠ BITCOIN TRANSACTION ≠ ETHEREUM TRANSACTION

Writing or committing this proposed binding does not itself broadcast a blockchain transaction.

No Bitcoin TXID or Ethereum transaction hash is asserted by this record.

"Stereum" is not silently treated as "Ethereum." If Stereum is intended as a distinct system, its binding requires a separate definition.
