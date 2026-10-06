# Model B Runtime Adapters

These adapters complete the runtime layer for the Cross-Model Echo Reviewer.

Supported lanes:

- openai-compatible: any OpenAI-compatible chat-completions server
- anthropic: Anthropic Messages API
- gemini: Google Gemini generateContent API
- huggingface: Hugging Face OpenAI-compatible router
- ollama: local Ollama
- lmstudio: local LM Studio
- llamacpp: local llama.cpp server

All adapters:

1. read the frozen Model B prompt from stdin
2. call exactly one configured reviewer model
3. require a JSON reviewer response
4. emit that JSON to stdout
5. fail closed as HOLD when credentials, transport, or parsing fail

No API key is committed. Secrets are environment variables only.

## Required variables

All runtimes require:

MODEL_B_MODEL=<reviewer model id>

Provider-specific:

- openai-compatible: MODEL_B_BASE_URL, optional MODEL_B_API_KEY
- anthropic: ANTHROPIC_API_KEY
- gemini: GEMINI_API_KEY
- huggingface: HF_TOKEN
- ollama: optional OLLAMA_HOST
- lmstudio: optional MODEL_B_API_KEY
- llamacpp: optional MODEL_B_API_KEY

## Wiring into Model B

Example:

MODEL_B_REVIEWER_CMD="python3 gethub/core/model-b/runtimes/runtime_selector.py gemini" \
MODEL_B_MODEL="<independent model id>" \
GEMINI_API_KEY="<secret>" \
python3 gethub/core/model-b/model_b.py packet.json

The primary model identity and reviewer model identity in the packet must differ meaningfully.

A configured adapter is not itself Echo. Echo exists only after a genuinely independent runtime executes the frozen review and returns a valid TCGE review.
