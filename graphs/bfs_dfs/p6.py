# Distance of nearest cell having 1
"""
Given a binary grid of N*M. Find the distance(only rows and columns, no diagonals) of the nearest 1 in the grid for each cell.
"""


import sys
from collections import deque


def solve(grid: list[list[int]]) -> list[list[int]]:
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    q: list[tuple[int]] = deque()
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    
    while q:
        row, col = q.popleft() 
       
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
           
            if 0 <= nrow < n and 0 <= ncol < m:
                if dist[nrow][ncol] == -1:
                    dist[nrow][ncol] = dist[row][col] + 1
                    q.append((nrow, ncol))
        
    return dist      

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    grid = []
    for line in lines:
        grid.append(list(map(int, line.strip().split())))
    res = solve(grid)
    for row in res:
        print(*row)

"""
2 1 2
1 0 1
0 1 0  
"""  