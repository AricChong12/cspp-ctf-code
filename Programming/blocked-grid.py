import math

# Total paths from (0,0) to (20,20)
total = math.comb(40, 20)

# Paths that pass through (10,10)
to_blocked = math.comb(20, 10)
from_blocked = math.comb(20, 10)
blocked = to_blocked * from_blocked

# Valid paths
count = total - blocked

print("Total paths:", total)
print("Blocked paths:", blocked)
print("Valid paths:", count)
print(f"Flag: cspp{{{count}}}")