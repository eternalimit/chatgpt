# Coinbase Connector Main

Status: DEPLOYED / NOT CONNECTED

## Purpose

Repository-side interface for a future authenticated Coinbase connector.

## Flow

COINBASE ACCOUNT
-> CONNECTOR
-> BUZZ / TCGE
-> BALANCE OR TRANSACTION RECORD
-> PUBLIC TXID / ADDRESS CROSS-CHECK WHEN APPLICABLE
-> REPORT

## Current state

- Repository adapter: deployed.
- Live Coinbase account connector in ChatGPT: unavailable / not connected.
- Coinbase balance access: HOLD.
- Coinbase transaction access: HOLD.

## Security

Never commit or send:
- seed phrase
- private key
- recovery phrase
- password
- PIN
- API secret
- access token

Public addresses and TXIDs may be used for public-chain verification.

## TCGE

K = R AND I AND E

No live account evidence -> HOLD / 0.
