import sympy

primes = list(sympy.primerange(1, 20000))

p1000 = primes[999]
p2000 = primes[1999]

product = p1000 * p2000

print("1000th prime:", p1000)
print("2000th prime:", p2000)
print("Product:", product)
print(f"Flag: cspp{{{product}}}")