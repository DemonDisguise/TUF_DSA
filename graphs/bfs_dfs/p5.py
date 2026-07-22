# Detect cycle in an undirected graph (using dfs)
"""
 Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not using DFS.
"""


import sys
from graphs.graphs import UndirectedGraph


def solve(adj_dict: dict[int, list[int]]) -> bool:
    visited = set()
    
    for start in adj_dict:
        if start in visited:
            continue
        
        stack = [(start, None)]
        visited.add(start)
        while stack:
            node, parent = stack.pop()
            for neighbour in adj_dict[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append((neighbour, node))
                elif neighbour != parent:
                    return True
    return False

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    v, e = map(int, lines[0].strip().split())
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