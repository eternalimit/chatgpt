#!/usr/bin/env python3
import os
from common import emit, extract_json, http_json, read_prompt, require

prompt = read_prompt()
host = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
model = require("MODEL_B_MODEL")
data = http_json(
    host + "/api/chat",
    {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
    },
)
emit(extract_json(data["message"]["content"]))
