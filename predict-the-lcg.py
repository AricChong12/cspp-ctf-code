m = 2147483647

xs = [
    271843891,
    1838558574,
    875370132,
    425435243,
    28174468,
    249123467
]

# Recover a
diff1 = (xs[1] - xs[0]) % m
diff2 = (xs[2] - xs[1]) % m

a = (diff2 * pow(diff1, -1, m)) % m

# Recover c
c = (xs[1] - a * xs[0]) % m

# Verify the recovered LCG
for i in range(len(xs) - 1):
    assert (a * xs[i] + c) % m == xs[i + 1]

# Predict next output
next_output = (a * xs[-1] + c) % m

print("a =", a)
print("c =", c)
print("Next output =", next_output)
print(f"Flag = cspp{{{next_output}}}")