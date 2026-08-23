# Fibonacci sequence
a, b = 1, 1

for _ in range(2, 30):
    a, b = b, a + b

print(f"cspp{{{b}}}")