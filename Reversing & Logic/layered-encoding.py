import base64

data = "NjM3MzcwNzA3YjZjNjE3OTY1NzI2NTY0NWYzMzZlNjM2ZjY0Njk2ZTY3N2Q="

# Layer 1: Base64 decode
hex_string = base64.b64decode(data).decode()

# Layer 2: Hex decode
flag = bytes.fromhex(hex_string).decode()

print(flag)