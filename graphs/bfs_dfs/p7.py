# Surrounded Regions
"""
 Given a matrix mat of size N x M where every element is either 'O' or 'X'. Replace all 'O' with 'X' that is surrounded by 'X'. 
 An 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 'X' at locations just below, just above just left, and just right of it. no diagonals
"""

import sys


def dfs(sr: int, sc: int, mtrx: list[list[str]], visited: list[list[bool]]) -> None:
    n, m = len(mtrx), len(mtrx[0])
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited[sr][sc] = True
    stack = [(sr, sc)]

    while stack:
        row, col = stack.pop()
        
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            
            if 0 <= nrow < n and 0 <= ncol < m and mtrx[nrow][ncol] == 'O' and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                stack.append((nrow, ncol))


def solve(mtrx: list[list[str]]) -> None:
    if not mtrx: return 
    n, m = len(mtrx), len(mtrx[0])
    visited = [[False] * m for _ in range(n)]
    
    def process(row: int, col: int) -> None:
        if mtrx[row][col] == 'O' and not visited[row][col]:
            dfs(row, col, mtrx, visited)
    
    for j in range(m):
        process(0, j)
        process(n - 1, j)
        
    for i in range(n):
        process(i, 0)
        process(i, m - 1)
    
    for i in range(n):
        for j in range(m):
            if mtrx[i][j] == 'O' and not visited[i][j]:
                mtrx[i][j] = 'X'


if __name__ == "__main__":
    mtrx = []
    for line in sys.stdin:
        mtrx.append(list(line.strip().split()))
    solve(mtrx)
    for row in mtrx:
        print(*row)

""" 
X X X X
X O O X
X X O X
X O X X 
"""