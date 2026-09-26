# Crypto-to-Forex Map

Date: 2026-09-26
Assignment: code.core.main / FACTS
Status: CONNECTOR MAP

## Purpose

Connect the existing cryptocurrency map to a conventional FX quote layer without treating crypto assets as sovereign fiat currencies.

## Core routing

CRYPTO ASSET
-> NATIVE / HOST CHAIN CONNECTOR
-> PUBLIC MARKET PRICE SOURCE
-> BASE FIAT QUOTE
-> FOREX CROSS-RATE
-> TARGET FIAT
-> VERIFY
-> ECHO
-> K

## Canonical forex bridge

| Layer | Symbol | Role |
|---|---|---|
| Crypto asset | BTC, ETH, SOL, etc. | Digital asset being valued |
| Bridge fiat | USD | Default crypto market quote bridge |
| Forex source | FX | Converts bridge fiat into target fiat |
| Target fiat | EUR, GBP, JPY, CHF, CAD, AUD, NZD, CNY, HKD, SGD, INR, MXN, BRL, ZAR, SEK, NOK, DKK, PLN, TRY, KRW | Conventional currency output |

## Formula

For crypto asset C and target fiat F:

C/F = (C/USD) * (USD/F)

If the market source supplies a direct C/F pair, that direct quote may be used instead, subject to source validation.

## Connector families

- crypto-market: obtains public market price for a crypto asset.
- fx-usd-cross: obtains USD -> target-fiat exchange rate.
- direct-pair: optional direct crypto/fiat pair when independently available.
- verifier: cross-checks source identity, timestamp, units, and quote direction.
- echo: independent source or second market feed.

## Stability separation

Three different meanings of stability must remain separate:

1. Chain settlement stability
   - finality / confirmations / validator settlement.

2. Market-price stability
   - price volatility of the crypto asset.

3. Forex stability
   - movement of the fiat cross-rate.

A stable blockchain does not imply a stable market price.
A stablecoin peg does not imply zero issuer, reserve, custody, or host-chain risk.

## TCGE rule

GET
-> CRYPTO CONNECTOR
-> MARKET QUOTE
-> FX CONNECTOR
-> CROSS-RATE
-> VERIFY
-> ECHO
-> K

K = R ∧ I ∧ E

If a live market quote, FX rate, or independent Echo is missing:

K = 0 -> HOLD

## Ownership boundary

This map values assets. It does not establish wallet ownership, balances, transaction authority, or exchange execution.
