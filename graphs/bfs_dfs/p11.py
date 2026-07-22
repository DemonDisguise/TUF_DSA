# Number of islands
""" Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. """


import sys
from collections import deque


def solve(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    islands = 0
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] == True
                islands += 1
                q.append((i, j))
                
                while q:
                    row, col = q.popleft()
                    
                    for dr, dc in directions:
                        nrow = row + dr
                        ncol = col + dc
                        
                        if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                            visited[nrow][ncol] = True
                            q.append((nrow, ncol))
    
    return islands


if __name__ == "__main__":
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, line.strip().split())))
    print(solve(grid))

# 0 1 1 0
# 0 1 1 0
# 0 0 1 0
# 0 0 0 0
# 1 1 0 1  