#!/usr/bin/env python3
"""Offline public-address verifier for EternalimitChain.

This tool validates address format/checksum only. It never asks for or handles
private keys, seed phrases, or signing secrets.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
B58_MAP = {c: i for i, c in enumerate(B58)}
BECH32_CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
BECH32_MAP = {c: i for i, c in enumerate(BECH32_CHARSET)}


def b58decode(value: str) -> bytes:
    n = 0
    for ch in value:
        if ch not in B58_MAP:
            raise ValueError("invalid base58 character")
        n = n * 58 + B58_MAP[ch]
    out = b"" if n == 0 else n.to_bytes((n.bit_length() + 7) // 8, "big")
    pad = len(value) - len(value.lstrip("1"))
    return b"\x00" * pad + out


def valid_base58check(address: str, allowed_versions: set[int]) -> bool:
    try:
        raw = b58decode(address)
    except ValueError:
        return False
    if len(raw) < 5:
        return False
    payload, checksum = raw[:-4], raw[-4:]
    digest = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return checksum == digest and payload[0] in allowed_versions


def bech32_polymod(values: list[int]) -> int:
    generators = [0x3B6A57B2, 0x26508E6D, 0x1EA119FA, 0x3D4233DD, 0x2A1462B3]
    chk = 1
    for v in values:
        top = chk >> 25
        chk = ((chk & 0x1FFFFFF) << 5) ^ v
        for i, g in enumerate(generators):
            if (top >> i) & 1:
                chk ^= g
    return chk


def hrp_expand(hrp: str) -> list[int]:
    return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]


def bech32_decode(addr: str):
    if not addr or any(ord(x) < 33 or ord(x) > 126 for x in addr):
        return None
    if addr.lower() != addr and addr.upper() != addr:
        return None
    addr = addr.lower()
    pos = addr.rfind("1")
    if pos < 1 or pos + 7 > len(addr):
        return None
    hrp = addr[:pos]
    data_chars = addr[pos + 1 :]
    try:
        data = [BECH32_MAP[c] for c in data_chars]
    except KeyError:
        return None
    pm = bech32_polymod(hrp_expand(hrp) + data)
    if pm == 1:
        enc = "bech32"
    elif pm == 0x2BC830A3:
        enc = "bech32m"
    else:
        return None
    return hrp, data[:-6], enc


def convertbits(data, frombits: int, tobits: int, pad: bool = True):
    acc = 0
    bits = 0
    ret = []
    maxv = (1 << tobits) - 1
    max_acc = (1 << (frombits + tobits - 1)) - 1
    for value in data:
        if value < 0 or value >> frombits:
            return None
        acc = ((acc << frombits) | value) & max_acc
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)
    if pad:
        if bits:
            ret.append((acc << (tobits - bits)) & maxv)
    elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
        return None
    return ret


def valid_segwit(address: str, expected_hrp: str) -> bool:
    decoded = bech32_decode(address)
    if not decoded:
        return False
    hrp, data, enc = decoded
    if hrp != expected_hrp or not data:
        return False
    version = data[0]
    if version > 16:
        return False
    program = convertbits(data[1:], 5, 8, False)
    if program is None or not 2 <= len(program) <= 40:
        return False
    if version == 0 and len(program) not in (20, 32):
        return False
    if version == 0 and enc != "bech32":
        return False
    if version != 0 and enc != "bech32m":
        return False
    return True


def valid_bitcoin(address: str) -> bool:
    return (
        valid_base58check(address, {0x00, 0x05})
        or valid_segwit(address, "bc")
    )


def valid_litecoin(address: str) -> bool:
    return (
        valid_base58check(address, {0x30, 0x32, 0x05})
        or valid_segwit(address, "ltc")
    )


def valid_ethereum(address: str) -> bool:
    # Shape validation only. EIP-55 mixed-case checksum requires Keccak-256,
    # which is intentionally not reimplemented here with SHA3-256.
    return bool(re.fullmatch(r"0x[a-fA-F0-9]{40}", address))


def valid_solana(address: str) -> bool:
    try:
        raw = b58decode(address)
    except ValueError:
        return False
    return len(raw) == 32


VALIDATORS = {
    "bitcoin": valid_bitcoin,
    "litecoin": valid_litecoin,
    "ethereum": valid_ethereum,
    "evm": valid_ethereum,
    "solana": valid_solana,
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_addresses.py <wallet-registry.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    failures = 0

    for entry in data.get("registry", []):
        chain = str(entry.get("chain", "")).lower()
        address = entry.get("public_address")

        if not address:
            print(f"{chain}: HOLD (no public address)")
            continue

        validator = VALIDATORS.get(chain)
        if not validator:
            print(f"{chain}: HOLD (no validator implemented)")
            failures += 1
            continue

        ok = validator(address)
        print(f"{chain}: {'FORMAT_VALID' if ok else 'INVALID'}")
        failures += 0 if ok else 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
