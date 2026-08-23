term = "1"

for i in range(1, 30):
    result = ""
    j = 0

    while j < len(term):
        count = 1

        while j + count < len(term) and term[j + count] == term[j]:
            count += 1

        result += str(count) + term[j]
        j += count

    term = result

print("30th term length:", len(term))
print(f"Flag: cspp{{{len(term)}}}")