# PII Threat

PII threat is the risk that personally identifiable information (PII)—such as full names, addresses, phone numbers, email addresses, government identifiers, financial identifiers, credentials, or other linkable personal data—is exposed, misused, leaked, or correlated in a way that identifies someone.

## GitHub risk areas

Common repository risks include:

- accidental commits of secrets
- personal contact information
- local file paths or usernames
- logs containing identifiers
- screenshots or exported chat data
- API keys and tokens
- metadata that links otherwise separate private information

## Simple threat model

\[
\text{PII THREAT}=\text{EXPOSURE}\times\text{SENSITIVITY}\times\text{ACCESSIBILITY}
\]

## Controls

- minimize stored PII
- redact before committing
- keep secrets out of Git history
- use `.gitignore` and secret scanning
- review diffs before pushes
- rotate anything sensitive that was already exposed
