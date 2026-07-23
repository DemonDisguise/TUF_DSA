# Topological sorting (dfs)
"""
It only works on Directed Acyclic Graph(DAG). Linear ordering of vertices such that if there is an edge between u and v, u appears before v in that ordering
"""


import sys

""" def _dfs(node: int, adj_list: list[list[int]], visited: list[bool], stack: list[int]) -> None:
    visited[node] = True
    
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            _dfs(neighbour, adj_list, visited, stack)
    
    stack.append(node)


def solve(adj_list: list[list[int]]) -> list[int]:
    n = len(adj_list)
    visited = [False] * n
    stack = []
    
    for node in range(n):
        if not visited[node]:
            _dfs(node, adj_list, visited, stack)
    
    return stack[::-1] """

# Iterative dfs (to counter the recursion limit)
def solve(adj_list: list[list[int]]) -> list[int]:
    n = len(adj_list)
    visited = [False] * n
    topo = []

    for start in range(n):
        if visited[start]:
            continue

        stack = [(start, False)] 

        while stack:
            node, processed = stack.pop()

            if processed:
                topo.append(node)
                continue

            if visited[node]:
                continue

            visited[node] = True

            stack.append((node, True))

            for neighbour in reversed(adj_list[node]):
                if not visited[neighbour]:
                    stack.append((neighbour, False))

    return topo[::-1]


if __name__ == "__main__":
    adj_list = []
    for line in sys.stdin:
        adj_list.append(list(map(int, line.strip().split())))
    print(*solve(adj_list))

""" 


3
1
0 1
0 2 
"""        