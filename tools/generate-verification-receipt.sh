#!/usr/bin/env bash
set -euo pipefail

NODE="${NODE:-node}"

"$NODE" tools/generate-public-payload.js > /tmp/wf379999-payloads.json
"$NODE" tools/verify-public-payload.js < /tmp/wf379999-payloads.json > /tmp/wf379999-verification-receipt.json

cat /tmp/wf379999-verification-receipt.json
