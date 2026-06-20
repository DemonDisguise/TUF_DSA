# Counter
# Elements are stored as dictionary keys and their counts are stored as dictionary values
# Counts can be +ve, -ve or 0
from collections import Counter
from typing import Counter

c: Counter[str] = Counter("sausage")
print(c)

c2: Counter[str] = Counter({"red": 4, "blue": 2})
print(c2)

c3: Counter[str] = Counter(cats=4, dogs=8)
print(c3)

c4: Counter[str] = Counter("abracadabra")
print(c4.most_common(2))

c5: Counter[str] = Counter(a=4, b=2, c=0, d=-2)
c6: Counter[str] = Counter(a=1, b=2, c=3, d=4)
c5.subtract(c6)
print(c5)
print(c6.total())
print(+c5)
print(-c5)

# c + d - add two counters together
# c - d - subtract (keeping only positive counts)
# c & d - intersection: min(c[x], d[x])
# c | d - union: max(c[x], d[x])
# c == d - equality: c[x] == d[x]
# c <= d - inclusion: c[x] <= d[x]