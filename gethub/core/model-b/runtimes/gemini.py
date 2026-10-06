#!/usr/bin/env python3
import urllib.parse
from common import emit, extract_json, http_json, read_prompt, require

prompt = read_prompt()
key = require("GEMINI_API_KEY")
model = require("MODEL_B_MODEL")
url = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    + urllib.parse.quote(model, safe="")
    + ":generateContent?key="
    + urllib.parse.quote(key, safe="")
)
data = http_json(
    url,
    {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0,
            "responseMimeType": "application/json",
        },
    },
)
parts = data["candidates"][0]["content"]["parts"]
text = "".join(p.get("text", "") for p in parts)
emit(extract_json(text))
