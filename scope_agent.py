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
