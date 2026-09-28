# Spider Punch List — Forward State

## Completed
1. Prototype local gate.

## Active
2. Protected local storage.

Implementation:
- `.gitignore` excludes local private material.
- `tools/protected-local-store.sh` stores encrypted objects under `.private/`.
- Encryption uses local GPG symmetric AES-256.
- Passphrases are entered locally and are not passed as command-line arguments.
- Private plaintext is not committed.

## Next
3. Code payload generation.

Forward rule:
- verified public implementation only
- private material stays local
- one forward branch
