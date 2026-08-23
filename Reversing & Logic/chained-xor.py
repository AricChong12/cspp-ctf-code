ciphertext = bytes.fromhex(
    "243a273a2c22277e22217f7644510c13212f202e3e"
)

IV = 0x2a
K = 0x6d

plaintext = []

for i, c in enumerate(ciphertext):
    if i == 0:
        p = c ^ IV ^ K
    else:
        p = c ^ ciphertext[i - 1] ^ K

    plaintext.append(p)

flag = bytes(plaintext).decode()

print(flag)