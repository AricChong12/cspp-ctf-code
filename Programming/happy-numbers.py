def is_happy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))

    return n == 1


count = 0

for n in range(1, 10_001):
    if is_happy(n):
        count += 1

print("Happy numbers:", count)
print(f"Flag: cspp{{{count}}}")