p = 40000000000000000000000027
q = 50000000000000000000000029
n = 2000000000000000000000002510000000000000000000000783
assert p * q == n

e = 65537
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)   # modular inverse

c = 1628026776350107437414439262812310188137971661810558
m = pow(c, d, n)

flag = m.to_bytes((m.bit_length() + 7) // 8, "big")
print(flag)   # b'cspp{rsa_not_so_hard}'
