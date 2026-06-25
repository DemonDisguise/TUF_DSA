# Exactly K Pattern

## When to use

- Exactly K distinct elements
- Exactly K odd numbers
- Exactly K occurrences condition

---

## Key Trick

Convert to:

```text
AtMost(K) - AtMost(K-1)
```

---

## Template

```python
def solve(arr, k):
    return atMost(arr, k) - atMost(arr, k - 1)
```

---

## Why it works

AtMost(K) includes:
- all subarrays with ≤ K constraint

AtMost(K-1) removes:
- those with ≤ K-1 constraint

Remaining:
→ exactly K

---

## Complexity

Time: O(n)  
Space: O(k)