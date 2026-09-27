# TCGE — Minimal Truth Table Package

## Core variables

- `BTC` = Bitcoin-side pin valid
- `USD` = dollar-coin-side pin valid
- `POINT` = basket point `•` valid
- `ETH` = derived conversion from the valid point

## Truth table

| BTC | USD | POINT |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Core rule

`POINT = BTC AND USD`

or:

`• = BTC ∧ USD`

## ETH rule

ETH does not define the point.

`ETH = f(•)`

If one point is defined as one USD of basket value and `P_ETH` is the ETH/USD market price:

`ETH_per_point = 1 / P_ETH`

## Boundary

This package defines model logic only. It does not establish a market peg, token issuance, custody, or on-chain execution.
