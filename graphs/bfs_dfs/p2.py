# Rotten oranges
"""  Given an n x m grid, where each cell has the following values :
2 - represents a rotten orange , 1 - represents a Fresh orange , 0 - represents an Empty Cell .

Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten.
Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.. """

import sys
from collections import deque

def solve(grid: list[list[int]]):
    n, m = len(grid), len(grid[0])
    queue = deque([])
    fresh = 0
    time = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
                
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    while queue and fresh > 0:
        level = len(queue)
        for _ in range(level):
            curr_row, curr_col = queue.popleft()
            for row, col in directions:
                nrow = curr_row - row
                ncol = curr_col - col
                
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    queue.append((nrow, ncol))
                    fresh -= 1
        
        time += 1
    
    return time if fresh == 0 else -1

# If input is not to be mutated use a visited set
""" def solve(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    fresh = 0
    time = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
                visited.add((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue and fresh > 0:
        level = len(queue)
        for _ in range(level):
            curr_row, curr_col = queue.popleft()
            for row, col in directions:
                nrow, ncol = curr_row + row, curr_col + col
                if (0 <= nrow < n and 0 <= ncol < m
                        and (nrow, ncol) not in visited
                        and grid[nrow][ncol] == 1):
                    visited.add((nrow, ncol))
                    queue.append((nrow, ncol))
                    fresh -= 1
        time += 1

    return time if fresh == 0 else -1 """

if __name__ == "__main__":
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, line.strip().split())))
    print(solve(grid))

# 0 1 2
# 0 1 1
# 2 1 1   