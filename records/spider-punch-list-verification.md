# Spider Punch List — Verification Receipt

## Completed
1. Prototype local gate.
2. Protected local storage.
3. Code payload generation.
4. Verification receipt generation.

## Verification implementation

Files:
- `tools/verify-public-payload.js`
- `tools/generate-verification-receipt.sh`

Checks:
- SHA-256 hash matches canonical payload
- schema present
- workflow present
- route present
- public-only marker true
- private-material marker false

Output:
- `verification-receipt-v1`
- PASS only when every generated payload satisfies all checks
- receipt includes its own SHA-256

## Forward rule
- carry verified public state only
- drop unresolved state
- private material stays local
- one forward branch

## Next
5. Independent receipt comparison.
