# Rat in a maze
# grid dimensions n x n. rat placed at (0, 0) and has to reach (n-1, n-1)
# it can go up, down, left, right
# In grid: 0 - blocked, 1 - unblocked

def solve(n, grid):
    res = []
    dir = [
        (1, 0, 'D'),
        (0, -1, 'L'),
        (0, 1, 'R'),
        (-1, 0, 'U')
    ]
    
    def dfs(row, col, curr):
        if row == n - 1 and col == n - 1:
            res.append(''.join(curr))
            return
        
        grid[row][col] = 0
        
        for dr, dc, mv in dir:
            nr = dr + row
            nc = dc + col
            
            if (
                -1 < nr < n and
                -1 < nc < n and
                grid[nr][nc] == 1
            ):
                curr.append(mv)
                dfs(nr, nc, curr)
                curr.pop()
        
        grid[row][col] = 1
    
    dfs(0, 0, [])
    return res
        
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(*solve(n, grid))
    