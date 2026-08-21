data = open("blob.bin", "rb").read()

start = data.find(b"\xff\xd8\xff")
end = data.find(b"\xff\xd9", start)

if start == -1 or end == -1:
    print("JPEG markers not found")
else:
    jpeg = data[start:end + 2]

    with open("carved.jpg", "wb") as f:
        f.write(jpeg)

    print(f"[+] JPEG starts at offset: {start}")
    print(f"[+] JPEG ends at offset:   {end + 1}")
    print(f"[+] JPEG size:             {len(jpeg)} bytes")
    print("[+] Saved as carved.jpg")
