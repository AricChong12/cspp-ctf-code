hex_data = "47c7dfdf87cfddffa6ff1f772fa69f27cfb7"

def rotate_right(byte, bits):
    return ((byte >> bits) | (byte << (8 - bits))) & 0xff

plaintext = []

for i in range(0, len(hex_data), 2):
    byte = int(hex_data[i:i+2], 16)

    # Undo XOR
    byte ^= 0x5C

    # Undo rotate-left 3 → rotate-right 3
    byte = rotate_right(byte, 3)

    plaintext.append(byte)

print(bytes(plaintext).decode())