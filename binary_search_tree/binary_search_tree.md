# Binary Search Trees (BST)

## Definition

A BST is a Binary Tree where, for **every** node — not just direct children:
- left subtree = only smaller values
- right subtree = only larger values

> Why "every node" and not just children: a node 3 levels down can still break
> a rule set by an ancestor way above it, even if it looks fine next to its
> own parent. This is the #1 BST bug — see **Validate BST** below.

Duplicates: usually not allowed. If they are, pick one rule (e.g. "duplicates
go left") and use it everywhere in that problem — don't switch mid-solution.

---

## Time Complexity

| Operation | Balanced | Skewed (worst) |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Min / Max | O(log n) | O(n) |

> Why there's a worst case at all: nothing about "being a BST" guarantees
> balance. Insert 1,2,3,4,5 in that order and every node only has a right
> child — height = n, same speed as a linked list. "BST is fast" secretly
> means "*balanced* BST is fast."

All core ops are really **O(h)**, h = tree height. O(log n) is just what O(h)
becomes *if* h happens to be log n.

---

## Properties

- Inorder traversal → always sorted, ascending.
- Smallest value → leftmost node (go left until you can't).
- Largest value → rightmost node (go right until you can't).
- Successor → next value up (smallest thing bigger than target).
- Predecessor → next value down (largest thing smaller than target).

> Why inorder is sorted: inorder visits left-root-right, and the BST
> property *is* "left is smaller, right is bigger" — so visiting in that
> order can't help but come out ascending. Almost every trick below is just
> this one fact applied to a specific question.

---

## Traversals (same as plain trees — nothing BST-specific here)

- Preorder: root → left → right
- Inorder: left → root → right ← **the one that matters most for BSTs**
- Postorder: left → right → root
- Level order: BFS, row by row

---

## Search

```
target == node.val   → found
target < node.val    → go left
target > node.val    → go right
```
Time: O(h)

> Why you only ever check one side: the BST property already tells you
> which half the value would be in — you're never guessing, so you never
> need to check both children like you would on a plain tree.

---

## Insert

Walk down like Search, following the same left/right rule, until you hit a
`None` slot — that's where the new value goes.

Time: O(h)

---

## Delete — 3 cases, this is the one to slow down on

**Case 1 — leaf.** Just remove it.

**Case 2 — one child.** The node's single child takes its place directly.

**Case 3 — two children.** You can't just remove it — pick its
**inorder successor** (smallest value in its right subtree) *or* **inorder
predecessor** (largest value in its left subtree), copy that value into the
node, then delete the successor/predecessor from where it originally sat.

> Why this never gets stuck in an infinite Case-3 loop: the successor is
> defined as the *leftmost* node of the right subtree — by definition it
> can't have a left child (if it did, that child would be even smaller, and
> would be the real successor instead). So deleting the successor always
> lands in Case 1 or Case 2, never back in Case 3. That's what makes the
> recursion actually finish.

---

## Minimum

Go left until `left is None`. That node is the minimum.

## Maximum

Go right until `right is None`. That node is the maximum.

---

## Floor (largest value ≤ target)

```
target < node.val   → go left  (this node is too big, ignore it)
target >= node.val   → this node is a valid answer, STORE it, then go right
                        (there might be something even closer, further right)
```

## Ceil (smallest value ≥ target)

```
target > node.val   → go right (this node is too small, ignore it)
target <= node.val   → this node is a valid answer, STORE it, then go left
                        (there might be something even closer, further left)
```

> Why you keep going after finding a candidate: the first node you land on
> that qualifies isn't necessarily the *closest* one. Storing-and-continuing
> is what finds the tightest possible bound instead of just any bound.

---

## Validate BST — the trap

**Wrong instinct**: check each node only against its direct children. This
misses violations from non-adjacent ancestors (see Definition above).

**Correct**: pass a valid `(low, high)` range down as you recurse.

```
start:            (-∞, +∞)
going left:       (low, node.val)      ← tightens the ceiling
going right:      (node.val, high)     ← tightens the floor
node is valid iff  low < node.val < high
```

> Why range-passing fixes it: every node now gets told the exact window
> its value is allowed in, based on *every* ancestor above it, not just its
> parent. That closes exactly the gap the wrong instinct misses.

Alternative: inorder traversal, check the output is strictly increasing.
Equally correct, sometimes simpler to write.

---

## Kth Smallest

Inorder traversal, stop at the k-th node visited. Time: O(h + k) — you only
walk as far as the k-th element, not the whole tree.

## Kth Largest

Same idea, reversed: right → root → left, stop at the k-th node.

---

## Lowest Common Ancestor (LCA)

```
p < root and q < root   → go left  (both live in the left subtree)
p > root and q > root   → go right (both live in the right subtree)
otherwise                → current node is the LCA (this is the split point)
```
Time: O(h)

> Why this is simpler than LCA on a plain tree: the BST property tells you
> which direction *both* targets are in without searching — a plain tree
> gives no such hint, so plain-tree LCA generally needs to search both
> subtrees and combine results afterward (O(n), not O(h)).

---

## BST Iterator

Keep a stack of the current node's entire left-chain (push every `.left`
until `None`). `next()` pops the top, then if that node has a right child,
push that child's entire left-chain onto the stack too.

Time: O(1) amortized per `next()` call · Space: O(h)

---

## Recover BST (exactly two nodes swapped)

Inorder traversal should be sorted — it won't be, exactly twice, at the two
swapped spots. Find those two inversions, swap the *values* back.

Time: O(n) · Space: O(h) (O(1) with a Morris inorder instead of recursion)

---

## Build Balanced BST from Sorted Array

Pick the **middle** element as root, recurse on the left half and right half.

> Why the middle specifically: it splits remaining elements evenly on both
> sides every time, which is exactly what "balanced" means — this is a
> guaranteed-log-n-height BST by construction, not by luck.

Time: O(n)

## Convert Sorted Linked List to BST

Either: slow/fast pointer to find the middle directly on the list, or:
convert to an array first and reuse the algorithm above. Second option is
simpler to get right; first is the "no extra array" version.

---

## Trim BST (keep only values within [low, high])

```
node.val < low    → this whole node + its left subtree is too small,
                      discard, recurse into node.right instead
node.val > high   → this whole node + its right subtree is too big,
                      discard, recurse into node.left instead
otherwise          → keep node, trim both children recursively
```

## Range Sum BST

DFS, but skip subtrees you can prove are entirely outside `[low, high]` —
same pruning idea as Trim BST above, just summing instead of rebuilding.

---

## Two Sum IV (find two nodes summing to target)

Three valid approaches, pick based on constraints:
- HashSet while walking the tree (any traversal order)
- Inorder → sorted array → two-pointer
- Two BST Iterators, one from each end

## Merge Two BSTs

Either: inorder both into two sorted arrays, merge like merge-sort. Or: two
BST Iterators advancing in lockstep, O(h1 + h2) space instead of O(n).

---

## Pattern → What To Reach For

| If the question mentions... | Reach for... |
|---|---|
| smallest, largest, kth smallest/largest | Inorder (or reverse-inorder) |
| sorted output | Inorder — it's already sorted, no extra sort needed |
| closest value, floor, ceil | Floor/Ceil walk, store-and-continue |
| a range of values | Prune branches outside the range (Trim / Range Sum) |
| successor, predecessor | Inorder property |
| "build a balanced BST" | Middle-of-sorted-array-as-root |
| lowest common ancestor | Exploit ordering — don't search both sides blindly |

If a question says any of: **smallest / largest / kth smallest / sorted /
successor / predecessor / floor / ceil / range / closest** — think **BST
property** first, before reaching for a generic binary-tree algorithm.

---

## Still true from plain Binary Trees — don't re-derive these

- Recursion depth is still bounded by tree *height*, not node count, and a
  BST is **not automatically safe** from this — sorted-ish input (very
  common!) produces the worst-case skewed shape.
- classmethod vs instance method: same test — does it *build* a tree
  (classmethod) or *act on* one that exists (instance method)?
- `TreeNode | None` hints, `from __future__ import annotations` — same as before.
- `__bool__` / truthiness: check `node is None` explicitly inside methods.
- Hand-trace a small 3–4 node example before trusting a shortcut — this
  matters *more* for BSTs, not less, since almost every "obviously correct"
  BST shortcut (Validate BST especially) has a small counterexample that
  breaks it.