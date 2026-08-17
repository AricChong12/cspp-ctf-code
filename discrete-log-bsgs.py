from math import isqrt

p = 100003
g = 2
h = 17309

m = isqrt(p) + 1

baby = {}
cur = 1

for j in range(m):
    baby[cur] = j
    cur = (cur * g) % p

factor = pow(pow(g, m, p), -1, p)
gamma = h

for i in range(m):
    if gamma in baby:
        x = i * m + baby[gamma]

        if pow(g, x, p) == h:
            print(f"cspp{{{x}}}")
            break

    gamma = (gamma * factor) % p