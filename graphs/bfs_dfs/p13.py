# Bipartite graph
""" There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite. """
# Any graph which is linear or has even length cycle is always bipartite
# If it has odd length cycle in graph is not bipartite


import sys
from collections import deque


# using BFS
def _bfs(start: int, adj_list: list[list[int]], color: list[int]) -> bool:
    q = deque([start])
    color[start] = 0
    
    while q:
        node = q.popleft()
        
        for neighbour in adj_list[node]:
            if color[neighbour] == -1:
                color[neighbour] = not color[node]
                q.append(neighbour)
            elif color[neighbour] == color[node]:
                return False

    return True

def solve(adj_list: list[list[int]]) -> bool:
    n = len(adj_list)
    color = [-1] * n
    
    for node in range(n):
        if color[node] == -1:
            if not _bfs(node, adj_list, color):
                return False
    
    return True
    

# DFS solution
""" def _dfs(start: int, adj_list: list[list[int]], color: list[int]) -> bool:
    stack = [start]
    color[start] = 0
    
    while stack:
        node = stack.pop()
        
        for neighbour in adj_list[node]:
            if color[neighbour] == -1:
                color[neighbour] = not color[node]
                stack.append(neighbour)
            elif color[neighbour] == color[node]:
                return False
    
    return True


def solve(adj_list: list[list[int]]) -> bool:
    n = len(adj_list)
    color = [-1] * n
    
    for node in range(n):
        if color[node] == -1:
            if not _dfs(node, adj_list, color):
                return False

    return True """


if __name__ == "__main__":
    adj_list = []
    for line in sys.stdin:
        adj_list.append(list(map(int, line.strip().split())))
    print(solve(adj_list))

# 1 2 3
# 0 2
# 0 1 3
# 0 2   