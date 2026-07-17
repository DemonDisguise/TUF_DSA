# Graph implementation

from __future__ import annotations
from collections import deque
from collections.abc import Hashable, Iterable


class Graph:
    """Base class for graphs, backed by adjacency list."""

    def __init__(self, edges: Iterable[tuple[Hashable, Hashable]] | None = None):
        self.adj: dict[Hashable, list[Hashable]] = {}
        if edges is not None:
            for u, v in edges:
                self.add_edge(u, v)

    
    def __repr__(self) -> str:
        lines = [f"{node}: {neighbours}" for node, neighbours in self.adj.items()]
        return "\n".join(lines) if lines else "(empty graph)"


    def __bool__(self) -> bool:
        return len(self.adj) > 0
    
    def __contains__(self, node: Hashable) -> bool:
        return node in self.adj
    
    @property
    def nodes(self) -> list[Hashable]:
        return list(self.adj.keys())
    
    @property
    def node_count(self) -> int:
        return len(self.adj)
    
    def add_node(self, node: Hashable) -> None:
        """Add a node with no edges, if it doesn't already exist.
        Safe to call on an existing node - no-op, not an error."""
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u: Hashable, v: Hashable) -> None:
        """Overridden by UndirectedGraph and DirectedGraph. Raises here so a bare Graph can't be silently misused as one of its subclasses."""
        raise NotImplementedError("Graph is abstract - use UndirectedGraph or DirectedGraph")
    
    def neighbors(self, node: Hashable) -> list[Hashable]:
        return self.adj.get(node, [])
    
    def degree(self, node: Hashable) -> int:
        """Overridden by DirectedGraph (in-degree vs out-degree).
        Correct as-is for UndirectedGraph, needs no override there."""
        return len(self.adj.get(node, []))
    
    def bfs(self, start: Hashable) -> list[Hashable]:
        if start not in self.adj:
            return []
        visited = {start}
        order = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order
    
    def dfs(self, start: Hashable) -> list[Hashable]:
        if start not in self.adj:
            return []
        visited = {start}
        order = []
        stack = [start]
        while stack:
            node = stack.pop()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return order
    
    def has_path(self, start: Hashable, end: Hashable) -> bool:
        if start not in self.adj or end not in self.adj:
            return False
        return end in self.bfs(start)
    
    def shortest_path(self, start: Hashable, end: Hashable) -> list[Hashable] | None:
        """BFS shortest path by edge count - only correct on unweighted graphs."""
        if start not in self.aj or end not in self.adj:
            return None
        if start == end:
            return [start]
        
        visited = {start}
        parent: dict[Hashable, Hashable] = {}
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    if neighbor == end:
                        path = [end]
                        while path[-1] != start:
                            path.append(parent[path[-1]])
                        return path[::-1]
                    queue.append(neighbor)
        return None
    
    def connected_components(self) -> list[list[Hashable]]:
        """Meaningful as written for UndirectedGraph. On DirectedGraph
        this finds WEAKLY connected components
        """
        visited: set[Hashable] = set()
        components = []
        for node in self.adj:
            if node not in visited:
                component = self.bfs(node)
                visited.update(component)
                components.append(component)
        return components
    
    def component_count(self) -> int:
        return len(self.connected_components())

class _UnionFind:
    """Path compression + union by rank, exactly as in reference doc."""

    def __init__(self, nodes: Iterable[Hashable]):
        self.parent: dict[Hashable, Hashable] = {n: n for n in nodes}
        self.rank: dict[Hashable, int] = {n: 0 for n in nodes}
    
    def find(self, x: Hashable) -> Hashable:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: Hashable, y: Hashable) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True
    
class UndirectedGraph(Graph):
    """A graph where every edge is bidirectional"""   

    def add_edge(self, u: Hashable, v: Hashable) -> None:
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def edge_count(self) -> int:
        """Each undirected edge is stored twice -- divide by 2"""
        total_degree= sum(len(neighbors) for neighbors in self.adj.values())
        return total_degree // 2
    
    def has_cycle(self) -> bool:
        """Parent-tracking DFS, checked across every component."""
        visited: set[Hashable] = set()
        for start in self.adj:
            if start in visited:
                continue
            
            stack: list[tuple[Hashable, Hashable | None]] = [(start, None)]
            visited.add(start)
            while stack:
                node, parent = stack.pop()
                for neighbor in self.adj[node]:
                    if neighbor in self.adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append((neighbor, node))
                        elif neighbor != parent:
                            return True
        return False
    
    def is_bipartite(self) -> bool:
        """BFS 2-coloring, checked across every component."""
        color: dict[Hashable, int] = {}
        for start in self.adj:
            if start in color:
                continue
            color[start] = 0
            queue = [start]
            while queue:
                node = queue.pop()
                for neighbor in self.adj[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True


class DirectedGraph(Graph):
    """A graph where edge (u, v) means only u->v is walkable, not v->u cause of direction"""
    
    def add_edge(self, u: Hashable, v: Hashable) -> None:
        self.add_node(u)  
        self.add_node(v)
        self.adj[u].append(v)
    
    def edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj.values())
    
    def out_degree(self, node: Hashable) -> int:
        return len(self.adj.get(node, []))
    
    def in_degree(self, node: Hashable) -> int:
        """O(V + E) per call -- adjacency lists tract outgoing changes naturally, not incoming"""
        count = 0
        for neighbors in self.adj.values():
            count += neighbors.count(node)
        return count
    
    def degree(self, node: Hashable) -> int:
        """Overrides  the base class's ambiguous degree() with in+out,
        rather than silently reusing the undirected meaning."""
        return self.in_degree(node) + self.out_degree(node)
    
    def has_cycle(self) -> bool:
        """Visited + in_path tracking"""
        visited: set[Hashable] = set()
        in_path: set[Hashable] = set()

        def _dfs(node: Hashable) -> bool:
            visited.add(node)
            in_path.add(node)
            for neighbor in self.adj[node]:
                if neighbor in in_path:
                    return True
                if neighbor not in visited:
                    if _dfs(neighbor):
                        return True
            in_path.remove(node)
            return False
        
        for start in self.adj:
            if start not in visited:
                if _dfs(start):
                    return True
        
        return False

    def topological_sort(self) -> list[Hashable] | None:
        """Kahn's algorithm. Length mismatch at the end IS the cycle detector,
        not a bolted-on check."""
        in_degree: dict[Hashable, int] = {node: 0 for node in self.adj}
        for node in self.adj:
            for neighbor in self.adj[node]:
                in_degree[neighbor] += 1
        
        queue = deque([node for node in self.adj if in_degree[node] == 0])
        order: list[Hashable] = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != len(self.adj):
            return None
        return order
    
    def topological_sort_dfs(self) -> list[Hashable] | None:
        """DFS-based: postorder-append, then reverse."""
        visited: set[Hashable] = set()
        in_path: set[Hashable] = set()
        result: list[Hashable] = set()
        has_cycle = False

        def _dfs(node: Hashable) -> None:
            nonlocal has_cycle
            visited.add(node)
            in_path.add(node)
            for neighbor in self.adj[node]:
                if neighbor in in_path:
                    has_cycle = True
                    return
                if neighbor not in visited:
                    _dfs(neighbor)
                    if has_cycle:
                        return
            in_path.remove(node)
            result.append(node)
        
        for start in self.adj:
            if start not in visited:
                _dfs(start)
                if has_cycle:
                    return None
        
        return result[::-1]
    
    def reverse(self) -> DirectedGraph:
        """Every edge u->v becomes v->u. Setup step for Kosaraju's SCC"""
        reversed_graph = DirectedGraph()
        for node in self.adj:
            reversed_graph.add_node(node)
        for u in self.adj:
            for v in self.adj[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph


class WeightedGraph:
    """A graph where every edge carries a numeric cost. directed=False (default) stores each edge on both endpoints; directed=True stores it on one."""

    def __init__(self, edges=None, directed: bool = False):
        self.adj: dict[Hashable, list[tuple[Hashable, float]]] = {}
        self.directed = directed
        if edges is not None:
            for u, v, weight in edges:
                self.add_edge(u, v, weight)

    def add_edge(self, u, v, weight: float = 1) -> None:
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))
    
        