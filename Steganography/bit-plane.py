from PIL import Image

img = Image.open("planes.png").convert("RGB")

out = Image.new("L", img.size)

pixels = img.load()
result = out.load()

for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixels[x, y]

        # Extract Blue channel LSB
        bit = b & 1

        # 0 = black, 1 = white
        result[x, y] = 255 if bit else 0

out.save("blue_lsb.png")

print("Saved blue_lsb.png")