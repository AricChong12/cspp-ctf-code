total = 0

for n in range(1, 1_000_001):
    gray = n ^ (n >> 1)
    total += gray

print("Sum:", total)
print(f"Flag: cspp{{{total}}}")