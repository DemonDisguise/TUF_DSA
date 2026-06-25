# Minimum Window (Substring / Subarray)

## When to use

- "minimum substring containing..."
- "smallest window that satisfies..."
- "cover all characters"
- "minimum length valid window"

---

## Core Idea

Expand right until valid  
Then shrink left to minimize window

---

## Template

```python
def solve(s):
    need = {}
    have = {}

    left = 0
    best = float('inf')

    required = len(need)  # or condition-based

    formed = 0

    for right in range(len(s)):

        ch = s[right]
        have[ch] = have.get(ch, 0) + 1

        # update formed if condition satisfied
        if have[ch] == need.get(ch, 0):
            formed += 1

        while formed == required:

            best = min(best, right - left + 1)

            have[s[left]] -= 1
            if have[s[left]] < need.get(s[left], 0):
                formed -= 1

            left += 1

    return best if best != float('inf') else 0
```

---

## Mental Model

```text
Expand → satisfy condition → shrink → optimize
```

---

## Complexity

Time: O(n)  
Space: O(k)