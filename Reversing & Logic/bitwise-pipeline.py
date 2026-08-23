hex_data = "41c1d9d98149d3f9e111c171a0d911d97139112971b1"

def ror8(x, n):
    return ((x >> n) | (x << (8 - n))) & 0xff

flag = ""

for i in range(0, len(hex_data), 2):
    byte = int(hex_data[i:i+2], 16)

    # Reverse XOR
    byte ^= 0x5A

    # Reverse rotate-left 3 → rotate-right 3
    byte = ror8(byte, 3)

    flag += chr(byte)

print(flag)