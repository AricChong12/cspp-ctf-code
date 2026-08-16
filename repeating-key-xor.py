ct_hex = "28362951303d695314326855231a387e277537462e37064a2e3c24"
ct = bytes.fromhex(ct_hex)

# Known plaintext prefix
known = b"cspp{"

# Recover keystream (and thus the repeating 4-byte key)
keystream = bytes(c ^ k for c, k in zip(ct, known))
key = keystream[:4]          # KEY!

# Decrypt
pt = bytes(c ^ key[i % 4] for i, c in enumerate(ct))
print(pt.decode())

