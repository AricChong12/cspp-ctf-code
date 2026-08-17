#!/usr/bin/env python3
"""
Bacon's Cipher decoder
Uppercase = 1, lowercase = 0
5 bits per letter (a=00000 ... z=11001)
Ignores spaces and punctuation.
"""

def bacon_decode(ciphertext: str) -> str:
    # Keep only letters and convert case to bits
    bits = ''.join(
        '1' if c.isupper() else '0'
        for c in ciphertext
        if c.isalpha()
    )

    # Group into 5-bit chunks (ignore incomplete final group)
    groups = [bits[i:i+5] for i in range(0, len(bits) - len(bits) % 5, 5)]

    # Map binary → letter (a=00000, b=00001, ...)
    plaintext = ''.join(
        chr(ord('a') + int(group, 2))
        for group in groups
        if int(group, 2) <= 25          # ignore invalid values
    )

    # Strip trailing 'a's (common zero-bit padding)
    return plaintext.rstrip('a')


if __name__ == "__main__":
    cipher = """the qUick brown Fox JUMps OVeR The LaZy DOg wHILe ClevEr RaVens watch every single move tonight"""
    
    decoded = bacon_decode(cipher)
    print(decoded)                 # baconswork
    print(f"cspp{{{decoded}}}")    # cspp{baconswork}