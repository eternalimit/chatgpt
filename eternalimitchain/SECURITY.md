# Security Policy

## Never commit secrets

Do not commit or paste any of the following:

- seed phrases
- mnemonic recovery words
- private keys
- wallet.dat files
- keystore JSON containing encrypted private keys
- hardware-wallet recovery backups
- exchange API secrets
- signing passwords

## Public data allowed

The registry may contain:

- public receiving addresses
- chain/network names
- transaction IDs
- public signatures used for verification
- derivation-path metadata only when it does not expose secret material

## Ownership verification

Address-format validation proves only that an address is syntactically plausible for a supported chain.

Control should be established separately by a cryptographic challenge-response method appropriate to the chain. Never expose the private key to perform that proof.

## TCGE

A claimed wallet relationship remains `HOLD` until independent evidence validates control.
