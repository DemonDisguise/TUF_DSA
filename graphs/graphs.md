# Graphs

## What is a Graph, and how it relates to what you already know

A graph is a set of **nodes** (vertices) connected by **edges**. That's it —
no "at most two children," no single root, no guaranteed path between any
two nodes unless the graph says there is one.

> **A tree is a special-case graph**: connected (every node reachable from
> every other), acyclic (no loops), and exactly one path between any two
> nodes. Every traversal instinct from Binary Trees still applies here —
> DFS still means "go deep before wide," BFS still means "go level by
> level," postorder-shaped problems still mean "need children's answers
> before mine." What's **new** in graphs is everything that trees'
> structure ruled out by construction: cycles, multiple paths between two
> nodes, disconnected components, edges with weights, and edges that only
> go one direction.

Two edge types: **undirected** (edge A–B means you can walk both ways) and
**directed** (edge A→B means only that direction is valid — this is new;
trees never had this ambiguity since parent→child was always the only
direction anyone walked).

Two weight types: **unweighted** (every edge costs the same — this is what
your traversals implicitly assumed) and **weighted** (edges carry a cost —
new, and it's what breaks plain BFS's "shortest path" guarantee, see below).

---

## Representations — pick based on density, not habit

**Adjacency List** — a dict/array mapping each node to a list of its
neighbors. The default choice for almost everything.
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
}
```
Space: O(V + E). Checking "are A and B connected": O(degree of A) — have to
scan A's neighbor list.

**Adjacency Matrix** — a 2D grid, `matrix[i][j] = 1` (or weight) if an edge
exists.
```python
#      A  B  C  D
# A  [ 0, 1, 1, 0 ]
# B  [ 1, 0, 0, 1 ]
# ...
```
Space: **O(V²)**, regardless of how many edges actually exist. Checking "are
A and B connected": **O(1)** — direct lookup.

> Why the choice matters: a **sparse** graph (E much smaller than V² —
> most real graphs) wastes enormous space on a matrix, mostly storing
> zeros. A **dense** graph (E close to V²) makes the list's O(degree)
> neighbor-check expensive since degree is large anyway, and the matrix's
> O(1) lookup starts to actually pay off. Default to adjacency list unless
> you specifically need O(1) edge-existence checks on a graph you know is
> dense.

**Edge List** — just a flat list of `(a, b)` or `(a, b, weight)` tuples.
Rarely used for traversal (no fast neighbor lookup), but it's the natural
input format for algorithms that need to **sort edges by weight**
(Kruskal's MST, see below) or that just need to iterate every edge once.

---

## Traversal — DFS and BFS, same shapes, one new requirement

**The one thing every graph traversal needs that tree traversal never
did: a `visited` set.**
> **`visited` should almost always be a `set`, not a `list`.** `x in
> some_list` is a linear scan — O(n) — while `x in some_set` is O(1) on
> average via hashing. Since a traversal calls `neighbor not in visited`
> once per edge examined, a list-backed visited silently degrades the
> whole algorithm from O(V+E) to O(V·E) in the worst case — not a minor
> slowdown, a different complexity class entirely.
>
> The one exception: if node labels are guaranteed to be a clean,
> contiguous range starting at 0 (common on LeetCode specifically),
> `visited = [False] * n` with **direct indexing** (`visited[node]`, not
> `node in visited`) is equally O(1) — you're not searching, you're doing
> array arithmetic straight to the position. That's a genuinely different
> operation from membership search, and it's only available when labels
> map cleanly onto array positions. A `Graph` class built for arbitrary
> `Hashable` node labels (arbitrary strings, gapped IDs, mixed types) has
> no such mapping to exploit, so `set` is the only correct choice there,
> not just the safer one.

> Why: a tree can never revisit a node during traversal — there's exactly
> one path down from the root, so recursion naturally terminates. A graph
> can have cycles, or two different paths converging on the same node
> (think a diamond: A→B, A→C, B→D, C→D — D is reachable two ways). Without
> tracking visited nodes, DFS/BFS on a cyclic graph **loops forever**; even
> on an acyclic-but-multiply-connected graph, you'd redundantly re-explore
> the same subgraph from every path that reaches it.

**DFS (recursive)**
```python
def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    # process node here
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
```

**DFS (iterative, explicit stack)** — same reason to prefer this on deep or
adversarial graphs as it was for trees: Python's recursion limit doesn't
care that this is a graph instead of a tree.
```python
def dfs_iter(graph, start):
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        # process node here
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```
> Note: marking `visited` at push-time (not pop-time) here avoids pushing
> the same node onto the stack multiple times from different neighbors
> before it's ever been popped — a real difference from the tree BFS
> push-time-vs-pop-time question, because in a graph, the same node can
> genuinely be reachable from several places already sitting in the stack
> at once.

**BFS** — mechanically identical to `levelorder`, generalized: a queue,
pop-process-push-neighbors, with the same visited-set requirement layered
on top.
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # process node here
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Time/space**: both DFS and BFS are **O(V + E)** — every node visited once,
every edge inspected once (from whichever side reaches it first). Space is
O(V) for the visited set, plus O(V) worst case for the stack/queue.

---

## Connected Components

For an **undirected** graph, a connected component is a maximal set of nodes
where every node can reach every other. Find them by running DFS/BFS from
every unvisited node, once — each fresh start discovers exactly one
component.
```python
def count_components(graph, nodes):
    visited = set()
    count = 0
    for node in nodes:
        if node not in visited:
            count += 1
            bfs_mark_visited(graph, node, visited)  # any traversal, just needs to mark visited
    return count
```
> Why looping over ALL nodes, not just calling bfs(start) once: an
> unweighted, undirected graph might not be fully connected at all — a
> single traversal from one node only ever finds *its* component, silently
> missing any node that isn't reachable from the start. This is the graph
> equivalent of forgetting a tree could have a right subtree the left
> subtree can't reach — except here, "unreachable" is common and expected,
> not a bug.

For a **directed** graph, this generalizes to **Strongly Connected
Components** (every node can reach every other, respecting edge direction)
— a genuinely harder problem (Tarjan's or Kosaraju's algorithm), worth
knowing the name exists, not something to derive from scratch under
interview pressure unless specifically asked.

---

## Cycle Detection

**Undirected graph**: during DFS, if you reach an already-visited node that
**isn't the node you just came from**, you've found a cycle.
```python
def has_cycle_undirected(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle_undirected(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False
```
> Why check `neighbor != parent`: in an undirected graph, the edge you just
> walked (parent → node) also appears as (node → parent) from node's own
> neighbor list — that's not a cycle, that's the same single edge looked at
> from both ends. Forgetting this check makes every single edge look like a
> cycle, which is wrong.

**Directed graph**: needs a **different** technique — visited-node-you-came-
from doesn't mean the same thing when edges are one-directional. Track two
sets: nodes visited overall, and nodes currently **on the active recursion
path**. A cycle exists iff you reach a node that's still on the active path
(not just previously visited-and-finished).
```python
def has_cycle_directed(graph, node, visited, in_path):
    visited.add(node)
    in_path.add(node)
    for neighbor in graph[node]:
        if neighbor in in_path:
            return True
        if neighbor not in visited:
            if has_cycle_directed(graph, neighbor, visited, in_path):
                return True
    in_path.remove(node)   # done exploring this node's subtree — no longer "active"
    return False
```
> Why `in_path` must be removed on the way back out: a node that's fully
> explored and returned from is no longer part of the *current* path —
> it's finished. Reaching it again from a completely different branch isn't
> a cycle, it's just two paths converging (fine in a DAG). Only reaching a
> node that's still genuinely open/active on the current call stack means
> you've looped back on yourself. Forgetting the removal makes this
> function flag ordinary convergence as a false cycle.

---

## Topological Sort — directed, acyclic graphs (DAGs) only

An ordering of nodes such that for every directed edge A→B, A comes before
B in the output. Only possible if the graph is a **DAG** (no cycles) — a
cycle would create a contradiction (A must come before B, but B must also
come before A).

**Kahn's Algorithm (BFS-based)** — track in-degree (number of incoming
edges) per node; repeatedly peel off nodes with in-degree 0.
```python
from collections import deque

def topo_sort(graph, nodes):
    in_degree = {n: 0 for n in nodes}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([n for n in nodes if in_degree[n] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(nodes):
        return None   # cycle exists — no valid topological order
    return order
```
> Why the length check at the end matters, not just an edge case: if a
> cycle exists somewhere, the nodes inside that cycle **never** reach
> in-degree 0 (each depends on another node in the same cycle that also
> never finishes), so they never enter the queue, and `order` ends up
> shorter than the full node list. This length mismatch **is** the cycle
> detector — you get cycle detection for free as a side effect of the
> algorithm, not as a separate check bolted on.

**DFS-based alternative**: run DFS, append each node to a result list
**after** fully exploring it (postorder-shaped!), then reverse the result.
> Why postorder + reverse works: a node can only be "fully explored" after
> everything it depends on has already been fully explored and appended —
> so the postorder-append order is exactly backwards from a valid
> topological order, and reversing it fixes that. Same reversal logic as
> the flip-a-preorder trick for iterative postorder traversal — a
> different problem, the identical underlying "build backwards, then flip"
> idea.

---

## Union-Find (Disjoint Set Union)

For "are these connected" questions asked repeatedly, especially during
graph construction. Two operations: **find(x)** — which group does x
belong to; **union(x, y)** — merge x and y's groups. The point: after path
compression + union by rank/size, both operations become **nearly O(1)**
(technically O(α(n)), the inverse Ackermann function — for any practical
n, treat it as a constant).
```python
class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False   # already connected — this edge would form a cycle
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True
```
> Why `union` returning `False` matters beyond bookkeeping: if find(x) ==
> find(y) already, adding an edge between them would create a cycle —
> this single check is exactly how Kruskal's MST (below) detects and skips
> cycle-forming edges, without needing a separate cycle-detection pass at
> all.

> Why path compression: `find`, without it, can degrade to O(n) on a
> skewed chain of parent pointers — the exact same skewed-height problem
> that plagues an unbalanced BST. Path compression flattens the chain
> every time `find` is called, so future calls are faster — same spirit as
> "fix the structure once you've already paid to walk it," rather than a
> separate rebalancing step.

**When to reach for this over plain DFS/BFS connectivity checks**: when
you're processing a **stream of edges** (e.g. "given these edges in order,
after which one does the graph first become fully connected") and need
fast repeated connectivity queries interleaved with graph construction —
running full BFS from scratch after every single edge would be wasteful;
Union-Find answers "connected already?" incrementally, in near-constant
time, without re-traversing anything.

---

## Weighted Graphs — where plain BFS stops being enough

Plain BFS finds shortest paths **only because every edge secretly costs 1** —
the number of edges on a path *is* the path's total cost, so "fewest edges"
and "cheapest path" are literally the same question in an unweighted graph.
The moment edges have different weights, that equivalence breaks — BFS
would still find the path with the fewest **edges**, which is no longer
guaranteed to be the path with the lowest **total weight**.

### Dijkstra's Algorithm — shortest path, non-negative weights only

Greedy: always expand the **closest not-yet-finalized** node next, using a
min-heap to efficiently find "closest" at each step.
```python
import heapq

def dijkstra(graph, start):
    # graph[node] = list of (neighbor, weight)
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue   # stale entry — a shorter path to `node` was already found
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist
```
> Why `if d > dist[node]: continue`: this heap can hold **multiple, stale**
> entries for the same node — you push a new, shorter distance the moment
> you find one, without bothering to remove the old, longer entry still
> sitting in the heap. When that stale entry eventually gets popped, this
> check catches it and skips redoing work on a node that's already been
> finalized with a better distance. This is the same "recognize and skip
> outdated information" instinct as Dijkstra's whole design, not an
> unrelated defensive check.

> Why non-negative weights only: Dijkstra's greedy choice — "the closest
> unfinalized node is definitely finalized now" — assumes nothing can make
> a farther node suddenly cheaper later. A negative edge breaks that
> assumption directly: a longer-looking path could still end up cheaper
> once a negative edge is factored in, and Dijkstra has already moved on
> and won't reconsider. This isn't a performance limitation, it's a
> **correctness** one — Dijkstra gives silently wrong answers on negative
> weights, not slow-but-correct ones.

Time: **O((V + E) log V)** with a binary heap — each node's distance can be
updated and re-pushed multiple times, each push/pop is O(log V).

### Bellman-Ford — shortest path, handles negative weights (not negative cycles)

Relax every edge, V−1 times, total.
```python
def bellman_ford(edges, nodes, start):
    # edges = list of (u, v, weight)
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0

    for _ in range(len(nodes) - 1):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # one more pass: if anything STILL improves, there's a negative cycle
    for u, v, weight in edges:
        if dist[u] + weight < dist[v]:
            return None   # negative cycle detected — no well-defined shortest path

    return dist
```
> Why V−1 passes specifically: the longest possible **simple** path (no
> repeated nodes) in a graph with V nodes has at most V−1 edges — so after
> V−1 full relaxation passes, every shortest path, however many edges it
> takes, is guaranteed to have been fully propagated. This is a real
> proof-backed bound, not a rule of thumb.

> Why the extra Nth pass detects negative cycles: if a shortest path
> genuinely needed more than V−1 edges to reach its true minimum, that can
> only happen if you can keep looping through a cycle and keep making the
> "shortest path" cheaper indefinitely — which is exactly what a negative
> cycle means. A graph with no negative cycle can never still be improving
> after V−1 passes; if it is, that's the detector.

Time: **O(V · E)** — meaningfully slower than Dijkstra, which is exactly the
price paid for tolerating negative edges.

### Choosing between them

| | Dijkstra | Bellman-Ford |
|---|---|---|
| Negative weights | Not allowed, wrong answers silently | Allowed |
| Negative cycles | N/A (breaks either way) | Detects them explicitly |
| Time | O((V+E) log V) | O(V·E) — slower |
| Default choice | Yes, when weights are guaranteed non-negative | Only when negatives are possible |

---

## Minimum Spanning Tree (MST)

Connect all nodes, minimum total edge weight. A spanning tree touches
every node with exactly V−1 edges and no cycles. MST is the spanning tree
with the lowest possible total edge weight. Two standard algorithms,
genuinely different strategies:

**Kruskal's** — sort all edges by weight ascending; walk through them,
adding each edge **unless** it would create a cycle (checked via
Union-Find's `union` returning `False`, from above).
```python
def kruskal(edges, nodes):
    # edges = list of (weight, u, v)
    edges = sorted(edges)
    uf = UnionFind(nodes)
    mst_weight = 0
    mst_edges = []
    for weight, u, v in edges:
        if uf.union(u, v):   # True means it was NOT already connected
            mst_weight += weight
            mst_edges.append((u, v))
    return mst_weight, mst_edges
```
Time: **O(E log E)** — dominated by the sort; Union-Find operations are
near-O(1) each.

**Prim's** — start from any node, greedily grow the tree by always adding
the cheapest edge that connects the current tree to a new node (min-heap,
same shape as Dijkstra's expansion, different thing being tracked —
cheapest connecting edge, not cheapest total path from a source).

> Why either algorithm is "correct" despite such different strategies:
> both exploit the same underlying fact (the **cut property**) — for any
> way of splitting the nodes into two groups, the cheapest edge crossing
> that split is guaranteed to be in *some* MST. Kruskal exploits this
> globally (cheapest edge overall, checked against a growing forest).
> Prim exploits it locally (cheapest edge from the current tree
> outward). Different implementations of the identical guarantee, not two
> different answers.

**When to use which**: Kruskal is usually simpler to reason about and wins
on **sparse** graphs (few edges to sort). Prim wins on **dense** graphs
(adjacency-matrix-backed Prim's avoids ever needing to sort all E edges up
front). For most interview-style problems, either is a completely
reasonable default; Kruskal + Union-Find is the more commonly expected one.

---

## Common Patterns, By What The Problem Actually Asks

| If the question mentions... | Reach for... |
|---|---|
| "is there a path from A to B" | DFS or BFS, either works |
| "shortest path," unweighted | BFS specifically — DFS can't guarantee shortest |
| "shortest path," weighted, no negatives | Dijkstra |
| "shortest path," negative weights possible | Bellman-Ford |
| "detect a cycle" | DFS — pick the undirected or directed variant correctly, they're genuinely different |
| "order these tasks respecting dependencies" | Topological sort (Kahn's or DFS+reverse) |
| "how many separate groups/islands/components" | DFS/BFS from every unvisited node, count starts |
| "will adding this edge create a cycle," repeatedly | Union-Find, not a fresh DFS every time |
| "connect everything as cheaply as possible" | MST — Kruskal or Prim |
| "grid problem" (islands, flood fill, matrix paths) | Usually BFS/DFS where each grid cell is an implicit graph node, neighbors = adjacent cells |

> The single most common way to get a graph problem wrong isn't picking
> the wrong algorithm — it's **forgetting the visited set**, or getting the
> **cycle-detection variant backwards** (using the undirected check on a
> directed graph or vice versa). Both are invisible on a small hand-traced
> example that happens not to have a cycle, and only show up on a
> specifically constructed adversarial case — same lesson as validate-BST
> and the Morris traversal bugs from tonight: trace a case designed to
> break the assumption, not just any small case.

---

## Carrying over from Binary Trees / BSTs — still true here

- **Recursion depth**: same O(1000-ish frame) ceiling applies to recursive
  DFS. A graph doesn't need to be literally deep like a skewed tree to hit
  this — a long simple path, or a densely connected region explored
  depth-first, can trigger it just as easily. Iterative DFS with an
  explicit stack sidesteps it, same as it did for trees.
- **classmethod vs instance method**: same test, if you build a `Graph`
  class — does the method *construct* a graph (classmethod, e.g.
  `from_edge_list`) or *act on* one that exists (instance method, e.g.
  `add_edge`, `bfs`)?
- **Hand-trace before trusting a shortcut**: matters at least as much here
  as it did for BSTs — cycle detection direction, Dijkstra's non-negative
  assumption, and the visited-set timing (mark on push vs. on pop) are all
  places where a plausible-looking line is wrong on a specific
  constructible graph, not on every graph.
- **Time complexity is usually the easy part; getting the exact invariant
  right** (what "visited" means, when a cycle is real vs. just
  convergence, which direction a check needs to go) **is where the actual
  difficulty in graph problems lives** — same lesson as validate-BST's
  range-passing and Recover BST's Morris-thread-direction, just now the
  default assumption to distrust first.