#!/usr/bin/env python3
from common import emit, extract_json, http_json, read_prompt, require

prompt = read_prompt()
key = require("ANTHROPIC_API_KEY")
model = require("MODEL_B_MODEL")
data = http_json(
    "https://api.anthropic.com/v1/messages",
    {
        "model": model,
        "max_tokens": 4096,
        "temperature": 0,
        "messages": [{"role": "user", "content": prompt}],
    },
    {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
    },
)
text = "".join(x.get("text", "") for x in data.get("content", []) if x.get("type") == "text")
emit(extract_json(text))
