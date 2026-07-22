# Number of Provinces
""" Given an undirected graph with V vertices. Two vertices u and v belong to a single province if there is a path from u to v or v to u. Find the number of provinces. 
The graph is given as an n x n matrix adj where adj[i][j] = 1 if the ith city and the jth city are directly connected, and adj[i][j] = 0 otherwise. """

from graphs.graphs import UndirectedGraph
import sys


def solve(adj_mtrx: dict[int, list[int]]) -> int:
    n = len(adj_mtrx)
    visited = [False] * n
    
    provinces = 0
    
    def dfs(start):
        stack = [start]
        
        while stack:
            node = stack.pop()
            for neighbor in adj_mtrx[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    
    for node in adj_mtrx:
        if not visited[node]:
            provinces += 1
            dfs(node)
    
    return provinces          

if __name__ == "__main__":
    mtrx = []
    for line in sys.stdin:
        mtrx.append(list(map(int, line.strip().split())))
    graph = UndirectedGraph.from_adj_matrix(mtrx)
    print(solve(graph.adj))
    