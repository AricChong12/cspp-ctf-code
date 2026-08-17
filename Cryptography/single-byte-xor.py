cipher = bytes.fromhex("21313232393a72301d312b2c252e271d203b36271d29273b3f")

for key in range(256):
    plain = bytes(b ^ key for b in cipher)
    try:
        text = plain.decode()
    except UnicodeDecodeError:
        continue

    if all(32 <= b < 127 for b in plain):
        print(f"Key 0x{key:02x} ({key}): {text}")