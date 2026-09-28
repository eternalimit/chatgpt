#!/usr/bin/env python3
"""Compare a file's SHA-256 digest with an expected 64-character hex digest."""

import argparse
import hashlib
import re
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="File to verify")
    parser.add_argument("expected_sha256", help="Expected SHA-256 hex digest")
    args = parser.parse_args()

    expected = args.expected_sha256.lower()
    if not re.fullmatch(r"[0-9a-f]{64}", expected):
        parser.error("expected_sha256 must be exactly 64 hexadecimal characters")

    try:
        actual = sha256_file(args.file)
    except OSError as error:
        parser.exit(2, f"Cannot read {args.file}: {error}\n")

    matched = actual == expected
    print(f"STATE = {int(matched)}")
    print(f"EXPECTED = {expected}")
    print(f"ACTUAL   = {actual}")
    return 0 if matched else 1


if __name__ == "__main__":
    raise SystemExit(main())
