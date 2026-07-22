# Number of enclaves
""" You are given an N x M binary matrix grid, where 0 represents a sea cell and 1 represents a land cell. 
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid. Find the number of land cells in the grid for which we cannot walk off the boundary of the grid in any number of moves.. """


import sys
from collections import deque


# DFS solution
"""
def dfs(sr: int, sc: int, grid: list[list[int]], visited: list[list[bool]]) -> None:
    n, m = len(grid), len(grid[0])
    visited[sr][sc] = True
    stack = [(sr, sc)]
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    
    while stack:
        row, col = stack.pop()
        
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                stack.append((nrow, ncol))
 

def solve(grid: list[list[int]]) -> int:
    if not grid: return
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    enclave_cnt = 0
    
    def process(row: int, col: int) -> None:
        if grid[row][col] == 1 and not visited[row][col]:
                dfs(row, col, grid, visited)
    
    for j in range(m):
        process(0, j)
        process(n - 1, j)
            
    for i in range(1, n - 1):
        process(i, 0)
        process(i, m - 1)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                enclave_cnt += 1
    
    return enclave_cnt
"""


# Multi-source BFS solution
def solve(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    q = deque()
    visited = [[False] * m for _ in range(n)]
    enclave_cnt = 0
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    
    def process(row: int, col: int) -> None:
        if grid[row][col] == 1 and not visited[row][col]:
            visited[row][col] = True
            q.append((row, col))
    
    for j in range(m):
        process(0, j)
        process(n - 1, j)
    
    for i in range(1, n - 1):
        process(i, 0)
        process(i, m - 1)
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            
            if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                q.append((nrow, ncol))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                enclave_cnt += 1
    
    return enclave_cnt
                

if __name__ == "__main__":
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, line.strip().split())))
    print(solve(grid))
 

""" 
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0   
"""