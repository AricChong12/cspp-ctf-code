total = 0

for n in range(100):  # rows 0 through 99
    odd_count = 2 ** n.bit_count()
    total += odd_count

print("Total odd entries:", total)
print(f"Flag: cspp{{{total}}}")