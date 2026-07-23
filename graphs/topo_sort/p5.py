# Find Eventual safe states (bfs, topo sort)
""" There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order. """


import sys
from collections import deque


def solve(adj_list: list[list[int]]) -> list[int]:
    n = len(adj_list)
    adj_rev = [[] for _ in range(n)]
    indegree = [0] * n
    
    for node in range(n):
        for neighbour in adj_list[node]:
            adj_rev[neighbour].append(node)
            indegree[node] += 1
    
    q = deque()
    for node in range(n):
        if not indegree[node]: q.append(node)
    
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        
        for neighbour in adj_rev[node]:
            indegree[neighbour] -= 1
            if not indegree[neighbour]:
                q.append(neighbour)
    
    return topo[::-1]


# dfs solution
""" def _dfs(node: int, adj_list: list[list[int]], visited: list[int]) -> bool:
    visited[node] = 2
    
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            if _dfs(neighbour, adj_list, visited):
                return True
        elif visited[neighbour] == 2:
            return True
    
    visited[node] = 1
    return False


def solve(adj_list: list[list[int]]) -> list[int]:
    n = len(adj_list)
    visited = [0] * n
    
    for node in range(n):
        if not visited[node]:
            _dfs(node, adj_list, visited)
    
    return [i for i, state in enumerate(visited) if state == 1] """


if __name__ == "__main__":
    adj_list = []
    for line in sys.stdin:
        adj_list.append(list(map(int, line.strip().split())))
    print(*solve(adj_list))


"""
1
2
3
4 5
6
6
7

1 9
10
8
9
"""
