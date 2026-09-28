# Spider Punch List — Independent Receipt Comparison

## Completed
1. Prototype local gate.
2. Protected local storage.
3. Code payload generation.
4. Verification receipt generation.
5. Independent receipt comparison.

## Comparison implementation

Files:
- `tools/compare-verification-receipts.js`
- `tools/run-independent-receipt-comparison.sh`

Method:
- generate two independent payload sets
- freeze payload creation time with `SOURCE_DATE_EPOCH`
- verify each set independently
- normalize both receipts
- compare all deterministic verification fields
- ignore nondeterministic receipt timestamp and receipt self-hash
- emit `independent-receipt-comparison-v1`
- PASS only when normalized receipts match exactly

## Forward rule
- carry verified public state only
- drop unresolved state
- private material stays local
- one forward branch

## Next
6. Sanitized delivery artifact.
