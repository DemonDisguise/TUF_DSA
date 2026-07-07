# Binary Trees

## What is a Binary Tree?

A Binary Tree is a hierarchical data structure where each node has **at most two children**.

```
        1
      /   \
     2     3
    / \   /
   4   5 6
```

Each node contains:

- Value
- Left Child
- Right Child

---

# Terminology

## Root

Top-most node.

```
    1
```

---

## Parent

A node having children.

```
1
|
2
```

1 is parent of 2.

---

## Child

Node directly below a parent.

---

## Leaf Node

Node having no children.

```
4 5 6
```

---

## Internal Node

Any non-leaf node.

```
1 2 3
```

---

## Sibling

Nodes with same parent.

```
  2
 / \
4   5
```

4 and 5 are siblings.

---

## Ancestor

Any node above another node.

---

## Descendant

Any node below another node.

---

## Subtree

Tree rooted at any node.

---

# Height vs Depth

## Height of Node

Longest path from node to leaf.

Leaf height = 0

---

## Height of Tree

Height of root.

```
        1
      /   \
     2     3
    /
   4
```

Height = 2

---

## Depth

Distance from root.

Root depth = 0.

---

## Level

```
Level = Depth + 1
```

---

# Types of Binary Trees

## Full Binary Tree

Every node has either

- 0 children
- 2 children

---

## Complete Binary Tree

Every level is full except possibly last.

Last level filled left to right.

Example:

```
        1
      /   \
     2     3
    / \   /
   4   5 6
```

---

## Perfect Binary Tree

All internal nodes have two children.

All leaves on same level.

Nodes

```
2^(h+1)-1
```

---

## Balanced Binary Tree

For every node (height of the tree at max log(n))

```
|left height - right height| <= 1
```

---

## Degenerate Binary Tree

Looks like linked list.

```
1
 \
  2
   \
    3
```

---

# Binary Tree Representation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

# Traversals

## DFS

### Preorder

```
Root
Left
Right
```

Mnemonic

```
NLR
```

Example

```
        1
      /   \
     2     3
    / \
   4   5
```

Result

```
1 2 4 5 3
```

Uses

- Copy Tree
- Serialize Tree

---

### Inorder

```
Left
Root
Right
```

Mnemonic

```
LNR
```

Result

```
4 2 5 1 3
```

Special

For BST

```
Always Sorted
```

---

### Postorder

```
Left
Right
Root
```

Mnemonic

```
LRN
```

Result

```
4 5 2 3 1
```

Uses

- Delete Tree
- Evaluate Expression Tree

---

# BFS

Uses Queue

Level by level.

```
1
2 3
4 5
```

Output

```
1 2 3 4 5
```

Applications

- Level Order
- Zigzag
- Right Side View
- Minimum Depth

---

# Recursive Template

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```

---

# Iterative DFS

Use Stack.

---

# Iterative BFS

Use Queue.

---

# Time Complexity

DFS

```
O(n)
```

BFS

```
O(n)
```

Space

Worst

```
O(n)
```

Balanced DFS recursion

```
O(log n)
```

---

# Diameter

Longest path between any two nodes.

May or may not pass through root.

Solved using

```
Postorder DFS
```

---

# Maximum Depth

```
1 + max(left, right)
```

---

# Minimum Depth

Usually BFS.

---

# Balanced Tree

Check

```
abs(left-right)<=1
```

for every node.

---

# Lowest Common Ancestor (LCA)

Lowest node containing both targets.

General Tree

DFS

BST

Use BST property.

---

# Symmetric Tree

Mirror check.

```
left.left == right.right
left.right == right.left
```

---

# Same Tree

Compare recursively.

---

# Invert Binary Tree

Swap

```
left <-> right
```

---

# Path Sum

Usually DFS.

Maintain running sum.

---

# Root to Leaf Problems

Pattern

```
DFS

↓

Current Path

↓

Backtrack
```

---

# Binary Tree Views

Top View

Bottom View

Left View

Right View

Mostly BFS.

---

# Vertical Traversal

Need

```
column
row
value
```

Usually BFS.

---

# Boundary Traversal

Order

```
Root

↓

Left Boundary

↓

Leaves

↓

Right Boundary (Reverse)
```

---

# Tree Construction

Common combinations

```
Preorder + Inorder

Postorder + Inorder
```

Impossible

```
Preorder + Postorder
```

without extra information.

---

# Serialization

Convert tree

↓

String/List

Deserialize

↓

Original Tree

Usually Preorder.

---

# Morris Traversal

Traversal

WITHOUT

- Stack
- Recursion

Space

```
O(1)
```

Works by temporary threading.

---

# Common Patterns

## DFS

- Height
- Diameter
- Balance
- LCA
- Path Sum

---

## BFS

- Level Order
- Zigzag
- Views
- Minimum Depth

---

## Postorder

Need children's answer first.

Examples

- Diameter
- Balance
- Maximum Path Sum

---

## Inorder

Used for BST.

---

## Preorder

Tree construction.

Serialization.

---

# Make a Unique Binary Tree

- Inorder + (Postorder or Preorder) traversal

---

# Binary Tree vs BST

Binary Tree

```
No ordering
```

BST

```
Left < Root < Right
```

---

# Important Formulae

Perfect Tree

Nodes

```
2^(h+1)-1
```

Leaves

```
2^h
```

Maximum Nodes at Level i

```
2^i
```

---

# Cheat Sheet

```
Height
→ DFS

Depth
→ DFS

Level Order
→ BFS

Diameter
→ Postorder DFS

Balanced
→ Postorder DFS

LCA
→ DFS

Views
→ BFS

Vertical
→ BFS

Serialization
→ Preorder

BST Sorted
→ Inorder

Delete Tree
→ Postorder

Copy Tree
→ Preorder
```

---

# Python Templates

## DFS

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```

---

## BFS

```python
from collections import deque

q = deque([root])

while q:
    node = q.popleft()

    if node.left:
        q.append(node.left)

    if node.right:
        q.append(node.right)
```

---

# Revision Tips

1. Master recursive DFS first.
2. Learn iterative traversals.
3. Solve every traversal problem recursively before iterative.
4. Remember:
   - Preorder = Root Left Right
   - Inorder = Left Root Right
   - Postorder = Left Right Root
5. Most medium tree problems are just modified DFS.
6. When unsure:
   - Need parent before children? → Preorder
   - Need children before parent? → Postorder
   - Need sorted order (BST)? → Inorder
   - Need level-wise? → BFS