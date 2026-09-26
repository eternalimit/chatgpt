# Connect Webs Main

Status: ACTIVE
Branch: main

## Purpose

Establish a governed web-verification mesh across the repository's available public-data interfaces.

## Connected paths

1. GitHub repository evidence
   -> commit / tree / file verification

2. blockchain.explorer.main
   -> public blockchain address / TXID lookup path
   -> Blockscout submodule reference: scout/blockscout

3. COINBASE_CONNECTOR_MAIN.md
   -> repository-side Coinbase adapter boundary
   -> live authenticated Coinbase account connection remains unavailable / HOLD

## Mesh

INPUT
-> BUZZ / TCGE
-> SOURCE SELECT
   -> GITHUB
   -> BLOCKCHAIN EXPLORER
   -> COINBASE ADAPTER BOUNDARY
-> GET
-> INDEX
-> VERIFY
-> CORRELATE
-> REPORT

## Link rule

A web link is a transport/reference path, not proof by itself.

Each claimed fact must preserve:
- source identity
- retrieved evidence
- provenance
- verification state
- correlation target

K = R AND I AND E

Verified link -> PASS / 1
Missing or unverified link -> HOLD / 0

## Security boundary

Public data only unless an explicitly supported authenticated connector is actually connected.

Do not store or transmit:
- seed phrases
- private keys
- recovery phrases
- wallet passwords
- PINs
- API secrets
- access tokens

No exchange trade, wallet signing, transaction broadcast, or account access is implied by this mesh.
