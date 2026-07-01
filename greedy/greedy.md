# Greedy Algorithms

## What is Greedy?

A Greedy algorithm makes the **best possible choice at the current step** without reconsidering previous decisions.

It hopes that these local optimal choices lead to a globally optimal solution.

Unlike DP, Greedy **never backtracks**.

---

# When can Greedy be used?

A problem should satisfy:

### 1. Greedy Choice Property

A locally optimal choice leads to a globally optimal solution.

### 2. Optimal Substructure

The optimal solution can be built from optimal solutions of subproblems.

If either property is missing, Greedy usually fails.

---

# Greedy vs Dynamic Programming

| Greedy | Dynamic Programming |
|---------|---------------------|
| Makes local optimal choice | Explores all possibilities |
| No reconsideration | Stores previous results |
| Usually faster | Usually slower |
| Easier to implement | Harder |
| Doesn't always work | Always works if recurrence exists |

---

# How to Identify a Greedy Problem

Ask yourself:

- Can I always choose the best option right now?
- After making one choice, does the remaining problem stay the same?
- Is there a sorting hint?
- Is there an interval scheduling hint?
- Does the question ask for:
  - Maximum number of...
  - Minimum cost...
  - Earliest finish...
  - Largest profit...
  - Smallest resource...

If yes, think Greedy first.

---

# Common Greedy Patterns

## 1. Sorting

Sort first, then process.

Examples:

- Assign Cookies
- Meetings in One Room
- Non-overlapping Intervals
- Job Sequencing
- Fractional Knapsack

---

## 2. Earliest Finish Time

Always choose the interval finishing first.

Examples:

- Activity Selection
- Meetings in One Room

---

## 3. Smallest / Largest First

Use Heap.

Examples:

- Connect Ropes
- Huffman Coding
- Merge Files

---

## 4. Largest Profit First

Choose highest profit.

Examples:

- Job Sequencing

---

## 5. Highest Ratio

Sort by value/weight.

Examples:

- Fractional Knapsack

---

## 6. Jump Greedily

Maintain the farthest reachable index.

Examples:

- Jump Game
- Jump Game II

---

## 7. Reachability

Maintain current range.

Examples:

- Gas Station
- Minimum Refueling Stops

---

## 8. Frequency Based

Choose most frequent / least frequent.

Examples:

- Task Scheduler
- Reorganize String

---

# Famous Greedy Algorithms

## Huffman Coding

Repeatedly merge the two smallest frequencies.

Data Structure:

```
Min Heap
```

Time:

```
O(n log n)
```

---

## Kruskal's Algorithm

Sort edges by weight.

Use DSU.

Time:

```
O(E log E)
```

---

## Prim's Algorithm

Grow MST one edge at a time.

Uses Priority Queue.

Time:

```
O(E log V)
```

---

## Dijkstra's Algorithm

Always visit the nearest unvisited node.

Works only with non-negative weights.

Uses Priority Queue.

---

# Problems That Look Greedy But Aren't

These require DP instead.

- House Robber
- Coin Change (minimum coins)
- Partition Equal Subset Sum
- Longest Increasing Subsequence
- Edit Distance

---

# Exchange Argument

Many greedy proofs use the exchange argument.

Idea:

Suppose another optimal solution exists.

Show that replacing one choice with the greedy choice never makes it worse.

Eventually both become identical.

---

# Greedy + Heap

Pattern:

```
Sort

↓

Priority Queue

↓

Take best candidate
```

Examples

- Connect Ropes
- Task Scheduler
- IPO
- Maximum Performance of Team
- Furthest Building You Can Reach

---

# Greedy + Sorting

Pattern:

```
Sort

↓

Single pass
```

Examples

- Meetings
- Cookies
- Merge Intervals
- Erase Overlap
- Job Sequencing

---

# Greedy + Two Pointers

Examples

- Boats to Save People
- Rescue Boats
- Advantage Shuffle

---

# Greedy + Stack

Examples

- Remove K Digits
- Remove Duplicate Letters
- Monotone Increasing Digits

---

# Time Complexities

| Operation | Complexity |
|-----------|------------|
| Sorting | O(n log n) |
| Heap Push | O(log n) |
| Heap Pop | O(log n) |
| Heapify | O(n) |

Most greedy problems are:

```
O(n log n)
```

or

```
O(n)
```

---

# Proof Checklist

If asked why Greedy works:

- Greedy Choice Property
- Optimal Substructure
- Exchange Argument

These three justify almost every greedy algorithm.

---

# Interview Tips

When you see a problem, ask in order:

```
Can I sort?

↓

Can I always take the current best?

↓

Can I prove it never hurts?

↓

If no,
think Dynamic Programming.
```

---

# Rule of Thumb

If a problem asks:

- Maximum number of intervals
- Minimum total cost by repeatedly choosing
- Earliest finishing
- Largest profit
- Highest ratio
- Smallest element repeatedly
- One-pass decisions

Think:

```
Greedy
```

If you're forced to ask:

> "Should I take this now or later?"

Think:

```
Dynamic Programming
```