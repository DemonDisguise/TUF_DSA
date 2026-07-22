# Number of distinct islands
""" Given a boolean 2D matrix grid of size N x M. 
You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. 
Two islands are considered to be distinct if and only if one island is equal to another (not rotated or reflected). """


import sys


def _dfs(sr: int, sc: int, grid: list[list[int]], visited: list[list[bool]], path: list[tuple[int]]) -> None:
    n, m = len(grid), len(grid[0])
    visited[sr][sc] = True
    stack = [(sr, sc)]
    path.append((0, 0))
    directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
    
    while stack:
        row, col = stack.pop()
        
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            
            if  0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                stack.append((nrow, ncol))
                path.append((nrow - sr, ncol - sc))


def solve(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    distinct_islands = set()
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                path = []
                _dfs(i, j, grid, visited, path)
                distinct_islands.add(tuple(path))
    return len(distinct_islands)


if __name__ == "__main__":
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, line.strip().split())))
    print(solve(grid))
