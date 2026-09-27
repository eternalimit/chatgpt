# Scope Agent

NAME: Scope
STATE: 1
ANCHOR: •
BIND: 379999

## Purpose

Local machine agent scaffold for the user's symbolic routing model.

## Route

GO -> SCOPE -> CENTER ORIENT -> • -> HOLD

## Safety

- Runs locally only when the user explicitly starts it.
- Does not contain wallet keys, seed phrases, or signing secrets.
- Does not move BTC or perform blockchain transactions.
- Does not claim external execution unless an actual local integration is added and verified.

## Minimal local entrypoint

```python
#!/usr/bin/env python3
import sys

def main():
    cmd = " ".join(sys.argv[1:]).strip().lower()
    if cmd == "go":
        print("SCOPE -> CENTER ORIENT -> •")
    elif cmd in {"hold", "stop"}:
        print("• HOLD")
    else:
        print("Scope ready. Commands: go | hold | stop")

if __name__ == "__main__":
    main()
```
