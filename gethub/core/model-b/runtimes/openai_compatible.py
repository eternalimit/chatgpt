#!/usr/bin/env python3
import os
from common import emit, extract_json, http_json, read_prompt, require

prompt = read_prompt()
base = require("MODEL_B_BASE_URL").rstrip("/")
key = os.getenv("MODEL_B_API_KEY", "")
model = require("MODEL_B_MODEL")
headers = {}
if key:
    headers["Authorization"] = f"Bearer {key}"
data = http_json(
    base + "/chat/completions",
    {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "response_format": {"type": "json_object"},
    },
    headers,
)
emit(extract_json(data["choices"][0]["message"]["content"]))
