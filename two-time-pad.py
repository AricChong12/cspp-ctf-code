c1 = bytes.fromhex("f16d20200861e559b9d35fba386420a9f517b60a9c643d024b3ceb9176ef22ac7033")
c2 = bytes.fromhex("e67635700224f84a8d9858b124673cecf2159158936423176775f7b875fc76ac3c22")

# XOR the ciphertexts -> equals p1 XOR p2
x = bytes(a ^ b for a, b in zip(c1, c2))

# crib-dragged plaintext (the ordinary English message)
p1 = b"the quick brown fox jumps over a l"

# recover the other plaintext (the flag) by XOR-ing the crib against x
flag = bytes(a ^ b for a, b in zip(x, p1))
print(flag.decode())