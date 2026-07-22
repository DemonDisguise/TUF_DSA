# Detect cycle in a directed graph
# Given a directed graph with V vertices and E edges, check whether it contains any cycle or not. 


import sys


def _dfs(node: int, adj_list: list[list[int]], visited: list[bool]) -> bool:
    visited[node] = 2
    
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            if _dfs(neighbour, adj_list, visited):
                return True
        elif visited[neighbour] == 2:
            return True
    
    visited[node] = 1
    return False    


def solve(adj_list: list[list[int]]) -> bool:
    n = len(adj_list)
    visited = [0] * n
    
    for node in range(n):
        if not visited[node]:
            if _dfs(node, adj_list, visited):
                return True
            
    return False

if __name__ == "__main__":
    adj_list = []
    for line in sys.stdin:
        adj_list.append(list(map(int, line.strip().split())))
    print(solve(adj_list))

""" 
1
2
3 6
4
5

4
1 8
9
7 
"""