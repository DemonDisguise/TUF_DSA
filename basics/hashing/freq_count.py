# Frequency count

from collections import Counter

def get_freq(arr: list[int]) -> dict[int, int]:
    freq: dict[int, int] = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

def py_freq(arr: list[int]) -> dict[int, int]:
    return dict(Counter(arr))

arr: list[int] = list(map(int, input().split()))
print(get_freq(arr))
print(py_freq(arr))