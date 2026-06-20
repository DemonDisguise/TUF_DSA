# M Coloring Problem
# undirected graph and number m
# determine if graph can be colored with at most m colors
# such that no two adjacent vertices of graph are colored with same color

def solve(n, m, e, edges):
    graph = [[] for _ in range(n)]
   
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    color = [0] * n
    
    def is_safe(node, clr):
        for nei in graph[node]:
            if color[nei] == clr:
                return False
        return True
    
    def dfs(node):
        if node == n:
            return True
        
        for clr in range(1, m + 1):
            if is_safe(node, clr):
                color[node] = clr
                
                if dfs(node + 1):
                    return True
                
                color[node] = 0
        
        return False
    
    return dfs(0) 

if __name__ == "__main__":
    n, m, e = map(int, input().split())
    edges = []
    for i in range(e):
        edges.append(tuple(map(int, input().split())))
    print(solve(n, m, e, edges))
        