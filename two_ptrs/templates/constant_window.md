# Constant Window

## When to use

Use when the window size is fixed throughout the problem.

Examples:

- Maximum Sum Subarray of Size K
- First Negative Integer in Every Window of Size K
- Count Distinct Elements in Every Window of Size K
- Maximum Average Subarray I

---

## Recognition Pattern

Look for phrases like:

- "window of size k"
- "subarray of length k"
- "substring of length k"
- "every contiguous segment of size k"
- "fixed length"

→ Constant Window

---

## Idea

Instead of recomputing every window:

```text
[1 2 3] 4 5
```

Move the window by:

```text
Remove left element
Add right element
```

```text
[1 2 3] 4 5
sum = 6

remove 1
add 4

1 [2 3 4] 5
sum = 9
```

---

## Generic Template

```python
def solve(arr, k):
    n = len(arr)

    window = sum(arr[:k])

    ans = window

    for r in range(k, n):

        window += arr[r]
        window -= arr[r - k]

        ans = max(ans, window)

    return ans
```

---

## Window Boundaries

```python
left = r - k + 1
right = r
```

Current window:

```python
arr[left:right+1]
```

---

## Complexity

Time: O(n)

Space: O(1)

---

## Example

Input

```text
arr = [2,1,5,1,3,2]
k = 3
```

Windows

```text
[2,1,5] -> 8
[1,5,1] -> 7
[5,1,3] -> 9
[1,3,2] -> 6
```

Answer

```text
9
```

---

## Mental Model

```text
Expand Right
Shrink Left

Window Size Always = K
```