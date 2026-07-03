# N Queens problem
# return all distinct solutions to this puzzle
# every row and col 1 queen
# none of the queens attack each other


def solve(n):
    res = []
    board = [['.'] * n for _ in range(n)]
    mask = (1 << n) - 1
    
    def dfs(row, cols, diag1, diag2):
        if row == n:
            res.append([''.join(r) for r in board])
            return
        
        available = ~(cols | diag1 | diag2) & mask
        
        while available:
            pos = available & -available
            available -= pos

            col = pos.bit_length() - 1
                        
            board[row][col] = 'Q'
            
            dfs(
                row + 1,
                cols | pos,
                ((diag1 | pos) << 1) & mask,
                (diag2 | pos) >> 1
            )
            
            board[row][col] = '.'
    
    dfs(0, 0, 0, 0)
    return res

if __name__ == "__main__":
    n = int(input())
    res = solve(n)
    for i in res:
        for j in i:
            print(j)
        print()