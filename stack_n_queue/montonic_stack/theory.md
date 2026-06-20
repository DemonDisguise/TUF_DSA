# Monotonic Stack

A monotonic stack is a normal stack that maintains a specific order.

- Monotonic Increasing Stack
- Monotonic Decreasing Stack

---

# Monotonic Increasing Stack

Maintains:

```text
Bottom -> Top

1
3
5
8
```

Before pushing `curr`, remove all larger elements.

```python
while stk and stk[-1] > curr:
    stk.pop()

stk.append(curr)
```

---

# Monotonic Decreasing Stack

Maintains:

```text
Bottom -> Top

8
5
3
1
```

Before pushing `curr`, remove all smaller elements.

```python
while stk and stk[-1] < curr:
    stk.pop()

stk.append(curr)
```

---

# Next Greater Element (NGE)

Find the first greater element on the right.

```text
arr = [2, 1, 5, 3, 4]

ans = [5, 5, -1, 4, -1]
```

## Backward Traversal

Maintain a Monotonic Decreasing Stack.

```python
for i in range(n - 1, -1, -1):

    while stk and stk[-1] <= arr[i]:
        stk.pop()

    ans[i] = stk[-1] if stk else -1

    stk.append(arr[i])
```

---

# Next Smaller Element (NSE)

Find the first smaller element on the right.

```text
arr = [4, 8, 5, 2, 25]

ans = [2, 5, 2, -1, -1]
```

## Backward Traversal

Maintain a Monotonic Increasing Stack.

```python
for i in range(n - 1, -1, -1):

    while stk and stk[-1] >= arr[i]:
        stk.pop()

    ans[i] = stk[-1] if stk else -1

    stk.append(arr[i])
```

---

# Previous Greater Element (PGE)

Find the first greater element on the left.

```text
arr = [2, 5, 3, 7]

ans = [-1, -1, 5, -1]
```

## Forward Traversal

Maintain a Monotonic Decreasing Stack.

```python
for i in range(n):

    while stk and stk[-1] <= arr[i]:
        stk.pop()

    ans[i] = stk[-1] if stk else -1

    stk.append(arr[i])
```

---

# Previous Smaller Element (PSE)

Find the first smaller element on the left.

```text
arr = [4, 8, 5, 2]

ans = [-1, 4, 4, -1]
```

## Forward Traversal

Maintain a Monotonic Increasing Stack.

```python
for i in range(n):

    while stk and stk[-1] >= arr[i]:
        stk.pop()

    ans[i] = stk[-1] if stk else -1

    stk.append(arr[i])
```

---

# Traversal Pattern

## Looking Right

```python
for i in range(n - 1, -1, -1):
```

Used for:

- Next Greater Element
- Next Smaller Element

---

## Looking Left

```python
for i in range(n):
```

Used for:

- Previous Greater Element
- Previous Smaller Element

---

# Stack Type Cheat Sheet

| Problem | Stack Type |
|----------|----------|
| Next Greater Element | Decreasing |
| Previous Greater Element | Decreasing |
| Next Smaller Element | Increasing |
| Previous Smaller Element | Increasing |

---

# Circular Next Greater Element

```python
for i in range(2 * n - 1, -1, -1):
```

Access element:

```python
arr[i % n]
```

Used in:

- Next Greater Element II (LeetCode 503)

```python
for i in range(2 * n - 1, -1, -1):

    while stk and stk[-1] <= arr[i % n]:
        stk.pop()

    if i < n:
        ans[i] = stk[-1] if stk else -1

    stk.append(arr[i % n])
```

---

# Complexity

```text
Time  : O(n)
Space : O(n)
```

Reason:

```text
Each element is pushed once.
Each element is popped once.
```