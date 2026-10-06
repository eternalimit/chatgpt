#!/usr/bin/env python3
import os
from common import emit, extract_json, http_json, read_prompt, require

prompt = read_prompt()
token = require("HF_TOKEN")
model = require("MODEL_B_MODEL")
base = os.getenv("HF_OPENAI_BASE_URL", "https://router.huggingface.co/v1").rstrip("/")
data = http_json(
    base + "/chat/completions",
    {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    },
    {"Authorization": f"Bearer {token}"},
)
emit(extract_json(data["choices"][0]["message"]["content"]))
