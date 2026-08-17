from sympy import integer_nthroot

e = 3
n = 408153948924700642062610499805991826476546742708307680065746291554580>
c = 408153948924700642062610499805991826476546742708307680065746291554580>

m, exact = integer_nthroot(c, 3)

print("Exact cube root:", exact)

flag = m.to_bytes((m.bit_length() + 7) // 8, "big")
print(flag)

