MOD = 10**10
n = 1_000_000

a, b = 0, 1

for _ in range(n):
    a, b = b, (a + b) % MOD

print(f"F({n}) =", a)
print(f"Flag: cspp{{{a:010d}}}")