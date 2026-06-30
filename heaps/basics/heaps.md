# Heaps & Priority Queue

---

# What is a Priority Queue?

A Priority Queue is a data structure where elements are removed according to their priority instead of insertion order.

Normal Queue (FIFO)

10 → 20 → 30

Pop:
10
20
30

Priority Queue (Min Heap)

5
2
8
1

Pop:
1
2
5
8

Highest priority is removed first.

Applications:
- Dijkstra's Algorithm
- Prim's MST
- Huffman Coding
- Merge K Sorted Lists
- Kth Largest/Smallest Element
- Top K Frequent Elements
- CPU Scheduling
- Event Simulation

---

# What is a Heap?

A Heap is a Complete Binary Tree that satisfies Heap Property.

There are two types.

## Min Heap

Parent <= Children

Example

          2
       /     \
      5       7
     / \     /
    8  10   9

Minimum element is always at root.

---

## Max Heap

Parent >= Children

Example

          20
       /      \
     15        18
    /  \      /
   7   10    5

Maximum element is always at root.

---

# Complete Binary Tree

Properties

- Every level is completely filled
- Last level fills from left to right
- No gaps allowed

Valid

        1
      /   \
     2     3
    / \   /
   4  5  6

Invalid

        1
      /   \
     2     3
      \   /
       5 6

Gap exists.

---

# Why Complete Binary Tree?

Because we can store it in an array.

No pointers needed.

---

# Array Representation

Index

        0
      /   \
     1     2
    / \   / \
   3  4  5  6

Formulas

Left Child

2*i + 1

Right Child

2*i + 2

Parent

(i-1)//2

---

# Height

For N nodes

Height = O(log N)

This is why almost every heap operation is O(log N).

---

# Heap vs BST

Heap

✔ Fast min/max

BST

✔ Ordered traversal

Heap

Search

O(N)

BST

Average Search

O(log N)

Heap

Only parent-child relation exists.

BST

Entire left subtree < root < right subtree

---

# Heap Operations

| Operation | Time |
|-----------|------|
| Peek | O(1) |
| Insert | O(log N) |
| Extract Min/Max | O(log N) |
| Heapify | O(log N) |
| Build Heap | O(N) |
| Search | O(N) |

---

# Insert

Step 1

Insert at last position.

Example

4 6 8 10

Insert 2

4 6 8 10 2

Step 2

Bubble Up

4 6 8 10 2

↓

4 2 8 10 6

↓

2 4 8 10 6

Done.

Bubble up until

Parent <= Child

---

# Bubble Up

Repeat

while parent > child

swap

move upward

Time

O(log N)

---

# Heapify (Bubble Down)

Used after removing root.

Example

Remove

        2
      /   \
     4     5
    / \
   8   9

Move last element

        9
      /   \
     4     5
    /
   8

Now fix

↓

        4
      /   \
     9     5
    /
   8

↓

        4
      /   \
     8     5
    /
   9

Done.

Always swap with smaller child (Min Heap).

---

# Extract Min

Step 1

Store root.

Step 2

Move last element to root.

Step 3

Delete last.

Step 4

Heapify.

Time

O(log N)

---

# Peek

Return root.

Min Heap

arr[0]

Time

O(1)

---

# Delete

Delete arbitrary index.

Cannot simply remove it.

Steps

Decrease value to -∞

↓

Bubble Up

↓

Root reached

↓

Extract Min

Time

O(log N)

---

# Decrease Key

Update value

Bubble Up

Time

O(log N)

---

# Build Heap

Given an array

4 10 3 5 1

Do NOT insert one by one.

Instead

Run Heapify from

Last non-leaf

↓

Root

Time

O(N)

NOT O(N log N)

This is an important interview question.

Last non-leaf

(n//2)-1

---

# Python Heap

Python provides only Min Heap.

Import

```python
import heapq
```

---

## Create Heap

```python
heap = []
```

---

## Push

```python
heapq.heappush(heap, x)
```

O(log N)

---

## Pop

```python
heapq.heappop(heap)
```

O(log N)

---

## Peek

```python
heap[0]
```

O(1)

---

## Heapify

```python
heapq.heapify(arr)
```

Time

O(N)

---

## Max Heap

Method 1

Store negatives.

```python
heapq.heappush(heap, -x)
```

Pop

```python
-x
```

---

Method 2 (Python 3.14+)

```python
heapq.heappush_max()
heapq.heappop_max()
```

(if available)

---

# Top K Problems

Use

Min Heap

When keeping K largest elements.

Heap size never exceeds K.

Complexity

O(N log K)

---

# Kth Largest

Maintain Min Heap of size K.

If heap grows

Pop smallest.

Answer

heap[0]

---

# K Closest Points

Heap stores

(distance, point)

---

# Merge K Sorted Lists

Heap stores

(value, list_index, node)

---

# Dijkstra

Heap stores

(distance, node)

Always process smallest distance.

---

# Prim

Heap stores

(weight, node)

---

# Common Interview Questions

✔ Kth Largest Element

✔ Kth Smallest Element

✔ Top K Frequent Elements

✔ Merge K Sorted Lists

✔ Find Median from Data Stream

✔ Task Scheduler

✔ IPO

✔ Sliding Window Maximum (alternative)

✔ Dijkstra

✔ Prim

---

# Common Mistakes

Using Heap for searching

❌ O(N)

Use BST / HashMap instead.

---

Forgetting Heap Property

Heap is NOT sorted.

Example

        1
      /   \
     4     3
    / \
   8   9

Array

1 4 3 8 9

Perfectly valid.

---

Heap vs Sorted Array

Sorted Array

Insert

O(N)

Min

O(1)

Heap

Insert

O(log N)

Min

O(1)

# Patterns

If question says

- Smallest
- Largest
- Top K
- Closest
- Highest Priority
- Stream
- Continuously changing minimum/maximum

Think

→ Heap / Priority Queue