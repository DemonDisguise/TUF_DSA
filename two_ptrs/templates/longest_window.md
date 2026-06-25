# Longest Window (Variable Size - Expand/Contract)

## When to use

Use when:
- You need the longest subarray/substring satisfying a condition
- Condition depends on frequency, sum, distinct count, etc.
- Window size is NOT fixed

---

## Recognition Pattern

Look for:

- "longest substring..."
- "maximum length such that..."
- "at most / at least K condition"
- "without repeating characters"
- "distinct elements <= k"

→ Variable Sliding Window

---

## Core Idea

We expand right pointer.

If invalid → shrink from left.

Keep track of best answer during valid states.

---

## Template

```python
def solve(arr):
    n = len(arr)

    left = 0
    ans = 0

    window = {}

    for right in range(n):

        # add right element
        window[arr[right]] = window.get(arr[right], 0) + 1

        # shrink while invalid
        while not valid(window):
            window[arr[left]] -= 1
            if window[arr[left]] == 0:
                del window[arr[left]]
            left += 1

        # update answer
        ans = max(ans, right - left + 1)

    return ans
```

---

## Mental Model

```text
Expand right → make invalid → shrink left → become valid again
```

---

## Complexity

Time: O(n)  
Space: O(k)