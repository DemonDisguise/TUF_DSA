# Alien dictionary
# Determine the order of characters in an alien language given a sorted list of words from its dictionary.


import sys
from collections import deque


def _build_graph(words_list: list[str], n: int, k: int) -> tuple[list[list[int]], list[int]]:
    graph = [[] for _ in range(k)]
    indegree = [0] * k
    
    for i in range(n - 1):
        s1 = words_list[i]
        s2 = words_list[i + 1]
        
        if len(s1) > len(s2) and s1.startswith(s2):
            return []

        length = min(len(s1), len(s2))
        for j in range(length):
            if s1[j] != s2[j]:
                u = ord(s1[j]) - ord('a')
                v = ord(s2[j]) - ord('a')
                
            if v not in graph[u]: 
                graph[u].append(v)
                indegree[v] += 1
            break  
         
    return graph, indegree
    

def solve(n: int, k: int, words_list: list[str]) -> tuple[str]:
    res = _build_graph(words_list, n, k)
    if not res:
        return ""
    
    graph, indegree = res
    
    q = deque()
    
    for i in range(k):
        if indegree[i] == 0:
            q.append(i)
    
    topo = []
    
    while q:
        node = q.popleft()
        topo.append(node)
        
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                q.append(neighbour)
        
    if len(topo) != k:
        return ""

    return "".join(chr(node + ord('a')) for node in topo)
    

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    n, k = map(int, lines[0].strip().split())
    words_list = list(lines[1].strip().split())
    print(solve(n, k, words_list))
    