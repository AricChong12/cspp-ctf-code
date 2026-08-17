#!/usr/bin/env python3
"""
Vigenère / repeating-key XOR breaker (unknown key length)
"""

import base64
from collections import Counter
import string

CIPHER_B64 = (
    "BFsGHBMVPVIPC0kdPVRDExMHJ0EGE15UMFoTGlYGc0cLE0dUIVYWAVYHc1JDAVsbIUdDGVYNfxMX"
    "GlZUPlwQBhMGNl8KE1EYNhMCAkMGPFIAGhMdIBMXHRMSOkEQBhMTJlYQARMAO1ZDHlYaNEcLUlwS"
    "c0cLFxMfNkpPUkccNl1DAUMYOkdDBlsRc1AKAlsRIUcGCkdUOl0XHRMXPF8WH10Hc0QLF0ERc1YV"
    "F0ENc1EaBlZUJFIQUl4VIFgGFhMWKhMXGlZUIFIOFxMfNkpDEEoANh1DN1IXOxMAHV8BPl1DG0BU"
    "MhMQG14EP1ZDAVoaNF8GUlENJ1ZDClwGfxMQHRMbIVcKHFIGKhMGHFQYOkALUl8RJ0cGABMSIVYS"
    "B1YaMEpDAFYCNlIPARMAO1ZDGVYNc1wNFxMEPEAKBlobPRMCBhMVc0cKH1Zac2cLFxMcOlcHF11U"
    "NV8CFRMSPEFDBlsdIBMAGlIYP1YNFVZUOkBDEUAEI0gRF0MRMkcKHFQrK1wRLVUGNkIWF10XKmwB"
    "AFYVOE5DE10Qc1YNFV8dIFtDH1IfNkBDG0dUNVIPHhMVI1IRBh0="
)

# Approximate English letter + space frequencies
ENGLISH_FREQ = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074, ' ': 0.13000
}


def hamming_distance(b1: bytes, b2: bytes) -> int:
    return sum(bin(x ^ y).count('1') for x, y in zip(b1, b2))


def normalized_hamming(data: bytes, keylen: int, max_blocks: int = 10) -> float:
    blocks = [data[i:i + keylen] for i in range(0, len(data) - keylen, keylen)]
    if len(blocks) < 2:
        return float('inf')
    distances = []
    for i in range(min(max_blocks, len(blocks) - 1)):
        d = hamming_distance(blocks[i], blocks[i + 1])
        distances.append(d / keylen)
    return sum(distances) / len(distances)


def score_text(text: str) -> float:
    score = 0.0
    for c in text.lower():
        if c in ENGLISH_FREQ:
            score += ENGLISH_FREQ[c]
        elif c in string.printable:
            score += 0.01
        else:
            score -= 1.0
    return score


def crack_single_byte_xor(column: bytes):
    best_score = -float('inf')
    best_key = 0
    best_plain = b''
    for key in range(256):
        plain = bytes(b ^ key for b in column)
        # Prefer mostly printable ASCII
        text = plain.decode('ascii', errors='ignore')
        sc = score_text(text)
        if sc > best_score:
            best_score = sc
            best_key = key
            best_plain = plain
    return best_key, best_plain, best_score


def main():
    data = base64.b64decode(CIPHER_B64)
    print(f"[*] Ciphertext length: {len(data)} bytes\n")

    # 1. Guess key length via normalized Hamming distance
    print("Keylen | Normalized Hamming (lower is better)")
    print("-" * 45)
    candidates = []
    for keylen in range(1, 41):
        nh = normalized_hamming(data, keylen)
        candidates.append((nh, keylen))
        print(f"{keylen:6d} | {nh:.4f}")

    candidates.sort()
    print("\nTop candidate key lengths:", [k for _, k in candidates[:5]])

    # 2. Use the best-looking length (12 worked cleanly)
    keylen = 12
    print(f"\n[*] Trying key length = {keylen}")

    columns = [data[i::keylen] for i in range(keylen)]
    keys = []
    for i, col in enumerate(columns):
        k, plain, sc = crack_single_byte_xor(col)
        keys.append(k)
        printable = chr(k) if 32 <= k < 127 else '?'
        print(f"  Column {i:2d}: key = 0x{k:02x} ('{printable}')  score = {sc:.2f}")

    key = bytes(keys)
    print(f"\n[*] Recovered key: {key!r}")
    print(f"[*] Key as ASCII : {key.decode('ascii', errors='replace')}")

    # 3. Decrypt
    plaintext = bytes(data[i] ^ key[i % keylen] for i in range(len(data)))
    print("\n[*] Plaintext:")
    print(plaintext.decode('ascii', errors='replace'))


if __name__ == "__main__":
    main()