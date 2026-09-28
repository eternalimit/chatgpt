#!/usr/bin/env bash
set -euo pipefail

NODE="${NODE:-node}"
TMP="${TMPDIR:-/tmp}"

A_PAYLOAD="$TMP/wf379999-a-payloads.json"
B_PAYLOAD="$TMP/wf379999-b-payloads.json"
A_RECEIPT="$TMP/wf379999-a-receipt.json"
B_RECEIPT="$TMP/wf379999-b-receipt.json"

# Freeze payload creation time so two independent executions are directly comparable.
EPOCH="${SOURCE_DATE_EPOCH:-1700000000}"

SOURCE_DATE_EPOCH="$EPOCH" "$NODE" tools/generate-public-payload.js > "$A_PAYLOAD"
SOURCE_DATE_EPOCH="$EPOCH" "$NODE" tools/generate-public-payload.js > "$B_PAYLOAD"

"$NODE" tools/verify-public-payload.js < "$A_PAYLOAD" > "$A_RECEIPT"
"$NODE" tools/verify-public-payload.js < "$B_PAYLOAD" > "$B_RECEIPT"

"$NODE" tools/compare-verification-receipts.js "$A_RECEIPT" "$B_RECEIPT"
