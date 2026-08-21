data = open("note.txt", "r", encoding="utf-8").read()

bits = ""

for char in data:
    if char == "\u200b":
        bits += "0"
    elif char == "\u200c":
        bits += "1"

print("Bits:", bits)

result = ""

for i in range(0, len(bits), 8):
    byte = bits[i:i+8]

    if len(byte) == 8:
        result += chr(int(byte, 2))

print("Decoded:", result)
