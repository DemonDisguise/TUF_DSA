# Binary Trees

## What is a Binary Tree?

A hierarchical structure where each node has **at most two children**.

```
        1
      /   \
     2     3
    / \   /
   4   5 6
```

Each node holds: a value, a left-child reference, a right-child reference.

---

## Terminology

| Term | Meaning |
|---|---|
| Root | Top-most node |
| Parent | A node that has children |
| Child | Node directly below a parent |
| Leaf | Node with no children |
| Internal node | Any non-leaf node |
| Sibling | Nodes sharing the same parent |
| Ancestor | Any node above another, on the path to root |
| Descendant | Any node below another |
| Subtree | The tree formed by any node + everything below it |

---

## Height vs Depth — the distinction that trips people up

**Height of a node** = number of **edges** on the longest path from that node
down to a leaf. A leaf's own height is **0** (zero edges to travel to reach
itself). An empty subtree's height is conventionally **-1**.

**Depth of a node** = number of edges from the **root down to that node**.
Root's depth is **0**.

**Height of the tree** = height of the root.

```
        1
      /   \
     2     3
    /
   4
```
Height of this tree = **2** (path `1 → 2 → 4` has 2 edges). Depth of node `4`
is also `2` here — depth and height often look similar in small examples,
but they're counting different things (root's height counts down to the
*farthest* leaf; a node's depth counts up from the *root*). Don't conflate
them just because they matched in one example.

> Why leaf height is 0 and not 1: it makes the recursive formula
> `1 + max(left_height, right_height)` work correctly at every level,
> including the base case. If you instead called a leaf's height 1, the
> formula would over-count by one at every single node. Empty = -1, leaf =
> 0 — treat this pair as a fixed anchor, not something to re-derive each time.

**Level** = Depth + 1 (root is level 1, its children are level 2, etc.) —
purely a labeling convention, some sources start levels at 0 instead. Check
which convention a problem is using before assuming.

---

## Types of Binary Trees

**Full** — every node has either 0 or 2 children (never exactly 1).

**Complete** — every level fully filled except possibly the last, and the
last level's nodes are pushed as far left as possible.
> Why this matters: this is the exact property that lets Count Nodes in a
> Complete Binary Tree beat plain O(n) — see Patterns below.

**Perfect** — every internal node has 2 children, all leaves on the same
level. Nodes = `2^(h+1) - 1`, leaves = `2^h` (h = height, edges-convention
from above).

**Balanced** — for every node, `|left_height - right_height| <= 1`. This
keeps overall tree height at O(log n) instead of O(n).

**Degenerate** — every node has at most one child; looks and behaves like a
linked list. Worst case for almost every operation, since height = n.

---

## Node Representation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Traversals — DFS family

**Preorder (NLR)**: Root → Left → Right
```
        1
      /   \
     2     3
    / \
   4   5
```
Result: `1 2 4 5 3`

Used for: copying a tree, serializing (you need the parent written down
before its children, so a reader can rebuild top-down).

**Inorder (LNR)**: Left → Root → Right — Result: `4 2 5 1 3`
> On a **BST specifically**, inorder is always sorted ascending. On a plain
> binary tree it has no special meaning beyond "this specific visit order."

**Postorder (LRN)**: Left → Right → Root — Result: `4 5 2 3 1`

Used for: deleting a tree (children must go before the parent, or you lose
your only reference to them), and any "this node's answer depends on its
children's answers" problem (height, diameter, balance — see Patterns).

> The real test for picking a traversal isn't "which one is traditionally
> used for X" — it's: does this node need info from its **ancestors**
> (preorder), from its **descendants** (postorder), or does it not care
> about parent/child at all and only cares about **depth/row** (BFS)? Write
> the recurrence in plain words first and the traversal usually falls out
> on its own.

---

## BFS (Level Order)

Queue-based, processes strictly row by row.

```
1
2 3
4 5
```
Output: `1 2 3 4 5`

Applications: level order, zigzag, all four side-views, vertical/top/bottom
view, minimum depth, count-nodes-in-complete-tree.

> The common thread across every "view" problem: they all care about which
> **row or column** a node lands in, not about the tree's parent/child
> shape directly — that's the tell that says BFS, not DFS.

---

## Recursive DFS Template

```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
```
This particular ordering (nothing between the two recursive calls, nothing
before them either) isn't any of the three named traversals by itself —
where you place your actual "do something" line relative to these two calls
is *what determines* whether you've written pre/in/postorder. Put it before
both calls: preorder. Between them: inorder. After both: postorder.

**Iterative DFS** → explicit stack, replacing the call stack by hand.
**Iterative BFS** → queue (`collections.deque`), same as above.

---

## Complexity

DFS and BFS are both **O(n) time** — every node visited exactly once,
regardless of which traversal.

**Space is the one to actually think about, not assume**:
- BFS: O(n) worst case (a very wide tree can have almost all nodes in one
  queue at once — think the last level of a complete tree).
- DFS (recursive): O(h) for the call stack, h = height. **O(log n) only if
  the tree happens to be balanced.** A skewed tree makes DFS's "O(h)" become
  O(n), and — this is the part worth internalizing, not just noting —
  Python's default recursion limit (~1000 frames) means a sufficiently
  skewed tree doesn't just get slow, it **crashes** with `RecursionError`.
  This isn't a rare edge case to shrug off; sorted-ish or adversarial input
  produces exactly this shape.

---

## Diameter

Longest path between **any** two nodes, in edges — may or may not pass
through the root.

```
diameter_at_node = left_height + right_height + 2
answer = max of that value across every node in the tree
```

Solved with a single postorder pass that computes height and updates a
running best simultaneously — **not** by calling a separate height()
function from inside a diameter check, which silently becomes O(n²)
(recomputing subtree heights over and over). One pass, track height and
the running max together.

---

## Maximum Depth / Height of Tree

```
1 + max(height(left), height(right))
```
Empty subtree = -1, matching the height convention above.

## Minimum Depth

Shortest root-to-**leaf** path. Usually solved with BFS — the moment you
first pop a leaf off the queue, that's your answer, no need to explore
further. (A DFS version has to explore every branch to be sure it found
the true minimum, unless you add extra pruning — BFS gets the early-exit
for free because of the order it visits nodes in.)

---

## Balanced Tree Check

Check `abs(left_height - right_height) <= 1` at **every** node, not just
the root.

> Why checking only the root isn't enough: a tree can be locally fine at
> the top while some subtree deep inside is badly skewed. Same shape of
> mistake as checking a BST only against the immediate parent — a property
> that must hold everywhere can't be verified by checking only one spot.

**The efficient version** computes height and checks balance in the *same*
postorder pass (return `(is_balanced, height)` together), rather than
calling height() separately at each node — same O(n²) trap as diameter above,
same fix.

---

## Lowest Common Ancestor (LCA)

**General binary tree**: postorder DFS — search both subtrees, if one call
returns "found p" and the other returns "found q", the current node is the
LCA. O(n), because nothing tells you which side to search, so you check both.

**BST specifically**: no searching needed — the ordering tells you directly
which side both targets are on. O(h), not O(n). Same problem name, different
complexity, purely because of the BST property (see the BST reference file).

---

## Symmetric Tree

Check whether a tree is a mirror image of itself. Compare **two** subtrees
at once (not one tree against itself) — the outer pair and the inner pair,
crossed:

```
is_mirror(left, right):
    if both None: True
    if exactly one None: False
    if left.val != right.val: False
    return is_mirror(left.left, right.right)   # outer edges, crossed
       and is_mirror(left.right, right.left)    # inner edges, crossed
```

> Why it's "crossed" and not `left.left` vs `right.left`: a mirror means the
> *far-left* of one side matches the *far-right* of the other — picture
> folding the tree down the middle. Comparing `left.left` to `right.left`
> would check if both sides lean the same way, which is a **same-tree**
> check, not a **mirror** check. These are genuinely different comparisons;
> don't reuse one for the other.

---

## Same Tree

Compare two separate trees node-by-node, structure and values both:

```
same(a, b):
    if both None: True
    if exactly one None: False
    if a.val != b.val: False
    return same(a.left, b.left) and same(a.right, b.right)
```
**Not crossed** — this is comparing each side straight-across, which is
exactly what distinguishes it from Symmetric Tree above.

---

## Invert Binary Tree

Swap `left` and `right` at every node, recursively.

---

## Path Sum

DFS, maintaining a running sum as you descend. Whether you need "any root-to-
leaf path" vs "any path at all" (not necessarily root-to-leaf, not necessarily
ending at a leaf) changes the shape a lot — the second version is the same
family as Diameter and Max Path Sum: track a running best via postorder,
clamp negative contributions to zero before folding them into a parent's sum
(see: the max path sum trace where naively adding a negative child's
contribution silently breaks a 2-node example).

## Root-to-Leaf Problems

Pattern: DFS down, carrying the current path so far → at a leaf, do
whatever the problem needs with that path → backtrack (undo the last
append) before returning to the parent, so sibling branches don't see a
path that isn't actually theirs.

---

## Binary Tree Views (Top / Bottom / Left / Right)

All BFS. The trick in every one of them: track **row or column** alongside
each node as you push it into the queue, and decide, per row or column,
whether the **first** arrival wins (top view, left view) or the **last**
arrival wins (bottom view, right view).

> Why first-vs-last works at all: BFS guarantees non-decreasing depth as
> you process the queue, and — for left/right specifically — processes each
> row strictly left-to-right if you always push left before right. "First
> write wins" and "last write wins" are just exploiting those two ordering
> guarantees in different combinations. Get the push order backwards (right
> before left) and first/last silently flips which side you're actually
> keeping.

---

## Vertical Order Traversal

Needs three things tracked per node: **column**, **row**, **value**.
Group by column, then within each column sort by row, then break same-
row-same-column ties by value. BFS is the natural walk; the sorting happens
after the walk, not during it.

---

## Boundary Traversal

```
Root → Left Boundary (top to bottom, excl. leaves)
     → Leaves (left to right)
     → Right Boundary (bottom to top, excl. leaves)
```
Reversed for the clockwise direction — and reversing means **the leaf order
flips too** (right-to-left in clockwise), not just which edge comes first.
Cleanest implementation: build the whole thing in one fixed direction
(anticlockwise), then produce clockwise by reversing everything *except* the
root, in one shot, rather than trying to reverse each of the three pieces
separately and hoping they agree.

---

## Tree Construction from Traversal Pairs

**Preorder + Inorder** → works. Preorder's first element is always the
subtree's root; inorder tells you how to split everyone else into
left-subtree-values and right-subtree-values, using that root.

**Postorder + Inorder** → works, mirrored. Postorder's *last* element is the
root. Reading postorder backwards gives root-right-left — so you build the
**right** subtree first, then left, which is the reverse of the
preorder+inorder build order. (Getting this swap backwards is a very easy
mistake — the pointer direction and the build order both have to flip
together, not just one of them.)

**Preorder + Postorder alone** → **not enough**, in general, to reconstruct
a unique tree.
> Why: both preorder and postorder tell you who a subtree's root is, but
> neither tells you *which side* an only-child belongs on. If a node has
> exactly one child, preorder+postorder can't distinguish "that child is the
> left child" from "that child is the right child" — multiple different
> trees produce the identical preorder+postorder pair. Inorder is what
> breaks that ambiguity, because it directly encodes left-vs-right
> positioning; preorder and postorder don't.

Optimal implementation for either working pair: precompute a value→index
map for the inorder array (avoids repeated linear search), and track
position via a single ever-advancing pointer into preorder/postorder
instead of slicing new sub-lists at every call (avoids O(n) copies per
call). Correct-but-naive version is O(n²); this version is O(n).

---

## Serialization / Deserialization

Tree ↔ string or list, usually via preorder (root written before children,
so a reader can reconstruct top-down) with an explicit marker for missing
children (e.g. `"N"` or `null`), or via level-order with the same marker
convention.

---

## Morris Traversal

Traversal with **zero** extra stack or recursion — genuine O(1) auxiliary
space — by temporarily threading a subtree's rightmost node's `.right`
pointer back to the current node, walking through it, then removing the
thread to restore the tree exactly as it was.

> The one sharp edge worth remembering: thread to the node you actually need
> to get back to (`curr`) directly — not to some other pointer that merely
> *currently equals* it (like `curr.right`), since an ancestor's own
> threading can silently change what that other pointer holds before you
> get to use it. This exact bug is easy to write and easy to have survive a
> full LeetCode test suite; it only shows up on specific multi-level tree
> shapes, and the only reliable way to catch it is testing against ground
> truth on many random trees, not eyeballing a small example.

Postorder via Morris additionally needs a dummy node above the real root
(so the true root's own right-edge gets processed at all) and, on each
thread removal, reverses-collects-restores the right-edge chain between the
threaded nodes rather than just tearing the thread down and moving on.

---

## Common Patterns, By Traversal

**DFS in general**: height, diameter, balance, LCA (plain tree), path sum.

**BFS**: level order, zigzag, all four views, vertical traversal, minimum
depth, count-nodes-in-complete-tree.

**Postorder specifically**: anything where "this node's answer needs its
children's answers first" — height, balance, diameter, max path sum. If
you're writing `something = f(left_result, right_result)` where both are
themselves recursive calls, that's postorder, and you didn't have to choose
it — the recurrence forced it.

**Preorder specifically**: tree construction, serialization, anything
passing accumulated context (like "path so far") down to children.

**Inorder specifically**: BST-sorted-output problems. Rarely the natural
choice on a plain (non-BST) tree.

---

## Count Nodes in a Complete Binary Tree

The one place a **complete** tree's guarantee buys you sub-O(n) time:

```
left_height = walk .left repeatedly from root, counting steps
right_height = walk .right repeatedly from root, counting steps

if left_height == right_height:
    return 2^left_height - 1     # provably perfect, closed-form, no counting
else:
    return 1 + count(root.left) + count(root.right)
```
> Why the equal-heights check is safe here specifically: this shortcut
> relies entirely on completeness. On an arbitrary tree, matching left/right
> heights says nothing about whether the middle is filled in — completeness
> is what rules out any gap hiding between the two edges. Because the tree
> is complete, at least one child is *always* provably perfect at every
> recursive call, which is what makes this O(log² n) instead of O(n).

---

## Binary Tree vs BST

| | Binary Tree | BST |
|---|---|---|
| Ordering | none | left < root < right, everywhere |
| Search | must check both children | check one side only |
| Inorder result | no particular meaning | always sorted |
| LCA | O(n), postorder, searches both sides | O(h), exploits ordering directly |

---

## Cheat Sheet

| Need | Reach for |
|---|---|
| Height / Depth | DFS (postorder for height specifically) |
| Level order | BFS |
| Diameter | Postorder DFS, single pass |
| Balanced check | Postorder DFS, single pass |
| LCA (plain tree) | Postorder DFS, search both sides |
| Any of the 4 views | BFS, track row/column, first-or-last-wins |
| Vertical traversal | BFS, track column+row+value |
| Serialization | Preorder (or level order), with a missing-child marker |
| BST sorted output | Inorder |
| Delete a tree | Postorder (children before parent) |
| Copy a tree | Preorder (parent must exist before attaching children) |
| Zero extra space | Morris traversal (thread to `curr`, not `curr.right`) |

---

## Revision Tips

1. Get recursive DFS solid first — the iterative/Morris versions are all
   variations on the same underlying visit order, easier to learn once the
   recursive shape is second nature.
2. For every traversal problem, work out the recursive version first, then
   the iterative one — trying to skip straight to iterative makes the
   "what am I even trying to replicate" question harder to answer.
3. The three orderings, once more, since they're worth having cold:
   Preorder = Root Left Right · Inorder = Left Root Right ·
   Postorder = Left Right Root.
4. Most medium-difficulty tree problems are DFS with one extra piece of
   bookkeeping (a running max, a range, a path list) — the traversal itself
   is rarely the hard part once you've picked the right one.
5. The actual decision rule, not a lookup table to memorize:
   - Node needs info from **ancestors**? → Preorder.
   - Node needs info from **descendants**? → Postorder.
   - Sorted order, and it's a **BST**? → Inorder.
   - Care about **depth/row**, not parent/child shape? → BFS.
6. Before trusting any shortcut (a formula, an early-exit condition, a
   "just check node.val" simplification) — hand-trace it against a small
   3–4 node example first. Nearly every subtle bug in this whole file (the
   diameter O(n²) trap, the symmetric-tree crossing direction, the Morris
   thread-to-`curr.right` corruption) is invisible on a 1-2 node example and
   only shows up once you deliberately pick a slightly bigger one.