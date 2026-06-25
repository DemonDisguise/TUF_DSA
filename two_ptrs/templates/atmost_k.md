# At Most K Pattern (Sliding Window Trick)

## When to use

Use when problem asks:

- "at most K distinct"
- "at most K odd numbers"
- "at most K frequency condition"
- "count subarrays with constraint"

---

## Key Insight

Instead of solving "exactly K", we use:

```text
AtMost(K) - AtMost(K-1)
```

---

## Template

```python
def atMostK(arr, k):
    left = 0
    count = 0
    freq = {}

    for right in range(len(arr)):

        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while len(freq) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        count += right - left + 1

    return count


def solve(arr, k):
    return atMostK(arr, k) - atMostK(arr, k - 1)
```

---

## Mental Model

```text
Count all valid windows ending at each index
```

---

## Complexity

Time: O(n)  
Space: O(k)