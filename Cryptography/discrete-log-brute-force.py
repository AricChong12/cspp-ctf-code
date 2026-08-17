p = 100003
g = 2
h = 17309

for x in range(p):
    if pow(g, x, p) == h:
        print(f"cspp{{{x}}}")
        break