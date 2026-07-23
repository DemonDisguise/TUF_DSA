# Topological sorting (bfs) Kahn's algorithm
""" Given a Directed Acyclic Graph (DAG) with V vertices labeled from 0 to V-1.The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Find any Topological Sorting of that Graph.

In topological sorting, node u will always appear before node v if there is a directed edge from node u towards node v(u -> v). """


import sys
from collections import deque


def solve(adj_list: list[list[int]]) -> list[int]:
    order = []
    n = len(adj_list)
    indegree = [0] * n
    
    for node in range(n):
        for neighbour in adj_list[node]:
            indegree[neighbour] += 1
    
    q = deque()
    
    for node in range(n):
        if not indegree[node]:
            q.append(node)
    
    while q:
        node = q.popleft()
        order.append(node)
        
        for neighbour in adj_list[node]:
            indegree[neighbour] -= 1
            
            if not indegree[neighbour]:
                q.append(neighbour)
    
    return order

if __name__ == "__main__":
    adj_list = []
    for line in sys.stdin:
        adj_list.append(list(map(int, line.strip().split())))
    print(*solve(adj_list))
    