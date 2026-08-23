import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


prev = 2
n = 3

while True:
    if is_prime(n):
        gap = n - prev

        if gap >= 100:
            print("Previous prime:", prev)
            print("Next prime:", n)
            print("Gap:", gap)
            print(f"Flag: cspp{{{prev}}}")
            break

        prev = n

    n += 2