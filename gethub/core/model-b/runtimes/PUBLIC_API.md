# Public API Adapter

This adapter tests an unauthenticated/public HTTP reviewer endpoint without assuming any specific provider.

## ASH mapping

POINT = configured public endpoint
STATE = current adapter condition
SKILL = HTTP JSON transport capability
ACTION = POST frozen reviewer prompt
RESULT = reviewer response
VERIFY = structural + TCGE verification

This preserves the ASH rule:

SKILL != ACTION

The existence of HTTP transport is only capability. Echo is not earned until an actual review action produces a valid independently sourced result.

## Environment

MODEL_B_PUBLIC_URL=https://example.org/review
MODEL_B_MODEL=optional-model-id

No API key is required by this adapter.

## Request

POST JSON:

{
  "prompt": "<frozen Model B prompt>",
  "response_format": "json",
  "model": "<optional>"
}

## Accepted response

Direct reviewer object or {"result": <reviewer object>}.

Required reviewer fields:

status, R, I, E, K

PASS is rejected unless K=1.

## Evidence boundary

A local mock test proves adapter behavior only. It does not prove that any specific third-party public inference endpoint exists, remains available, or qualifies as independent Echo.
