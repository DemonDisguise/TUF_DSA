# Highest and Lowest frequency

from collections import Counter

def get_high_freq(arr: list[int]) -> int:
    return Counter(arr).most_common(1)[0][0]

def get_low_freq(arr: list[int]) -> int:
    c = Counter(arr)
    m = min(c.values())
    return next(x for x, y in c.items() if y == m)

arr: list[int] = list(map(int, input().split()))
print(f"Highest frequency element: {get_high_freq(arr)}")
print(f"Lowest frequency element: {get_low_freq(arr)}")
    