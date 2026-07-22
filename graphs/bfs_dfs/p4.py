# Detect cycle in an undirected graph (using bfs)
"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not
"""

import sys
from collections import deque
from graphs.graphs import UndirectedGraph


def solve(adj_dict: dict[int, int]) -> bool:
    visited = set()
    
    for start in graph.adj:
        if start in visited:
            continue
        visited.add(start)
        q = deque([(start, None)])
        
        while q:
            node, parent = q.popleft()
            for neighbour in graph.adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((neighbour, node))
                elif neighbour != parent:
                    return True
    
    return False


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    edges = []
    for line in lines[1:]:
        edges.append(tuple(map(int, line.strip().split())))
    graph = UndirectedGraph(edges)
    print(solve(graph.adj))

""" 
8 6
1 2
2 3
4 5
5 6
6 4
7 8  
"""   