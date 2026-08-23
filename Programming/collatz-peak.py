memo = {1: 1}

def collatz_length(n):
    if n in memo:
        return memo[n]

    original = n
    count = 0

    while n not in memo:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1

    memo[original] = count + memo[n]
    return memo[original]


best_n = 1
best_length = 1

for n in range(1, 1_000_001):
    length = collatz_length(n)

    if length > best_length:
        best_n = n
        best_length = length

print(f"Winner: {best_n}")
print(f"Terms: {best_length}")
print(f"Flag: cspp{{{best_n}_{best_length}}}")