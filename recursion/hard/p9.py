# Sudoku Solver
# every row the numbers 1 through 9 must appear exactly once
# every column the numbers 1 through 9 must appear exactly once
# each of the grid's nine 3x3, the numbers 1 through 9 must appear exactly once

import sys

def solve(board):
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    
    empty = []
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == '-':
                empty.append((r, c))
            else:
                digit = int(board[r][c]) - 1
                bit = 1 << digit
                
                rows[r] |= bit
                cols[c] |= bit
                
                box = (r // 3) * 3 + (c // 3)
                boxes[box] |= bit
    
    def dfs(idx):
        if idx == len(empty):
            return True

        r, c = empty[idx]
        
        box = (r // 3) * 3 + (c // 3)
        
        used = rows[r] | cols[c] | boxes[box]
        available = (~used) & 0x1FF
        
        while available:
            bit = available & -available
            available -= bit
            
            digit = bit.bit_length() - 1
            
            board[r][c] = str(digit + 1)
            
            rows[r] |= bit
            cols[c] |= bit
            boxes[box] |= bit
            
            if dfs(idx + 1):
                return True
            
            rows[r] ^= bit
            cols[c] ^= bit
            boxes[box] ^= bit
            
            board[r][c] = '-'
        return False

    dfs(0)
    return board
            
if __name__ == "__main__":
    board = [list(line.strip().split()) for line in sys.stdin if line.strip()]
    res = solve(board)
    for row in res:
        print(*row)
        