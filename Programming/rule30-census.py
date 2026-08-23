WIDTH = 201
GENERATIONS = 100

# Initial state: one ON cell in the middle
row = [0] * WIDTH
row[WIDTH // 2] = 1

total = 0

for generation in range(GENERATIONS):
    # Count current generation
    total += sum(row)

    # Generate next generation
    new_row = [0] * WIDTH

    for i in range(WIDTH):
        left = row[i - 1] if i > 0 else 0
        center = row[i]
        right = row[i + 1] if i < WIDTH - 1 else 0

        # Rule 30: left XOR (center OR right)
        new_row[i] = left ^ (center | right)

    row = new_row

print("Total ON cells:", total)
print(f"Flag: cspp{{{total}}}")