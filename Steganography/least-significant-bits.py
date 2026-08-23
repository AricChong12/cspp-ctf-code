from PIL import Image

img = Image.open("lsb.png").convert("RGB")

bits = []

for y in range(img.height):
    for x in range(img.width):
        r, g, b = img.getpixel((x, y))
        bits.extend([r & 1, g & 1, b & 1])

result = bytearray()

for i in range(0, len(bits) - 7, 8):
    value = 0

    for bit in bits[i:i+8]:
        value = (value << 1) | bit

    if value == 0:
        break

    result.append(value)

print(result.decode())