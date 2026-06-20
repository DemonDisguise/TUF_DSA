# Word Search
# Give m x n of characters and string word
# return if words exists in the grid
# word can be constructed from letters of:
# sequentially adjacent cells, horizontally / vertically neighbouring
# same letter may not be used more than once

import sys
from collections import Counter

def solve(board, word):
    rows = len(board)
    cols = len(board[0])
    
    board_cnt = Counter(ch for row in board for ch in row)
    word_cnt = Counter(word)
    
    for ch, cnt in word_cnt.items():
        if board_cnt[ch] < cnt:
            return False
    
    if board_cnt[word[0]] > board_cnt[word[-1]]:
        word = word[::-1]
    
    def dfs(i, j, idx):
        if idx == len(word):
            return True
        
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'
        
        found = (dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i, j - 1, idx + 1))
        
        board[i][j] = tmp
        
        return found
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    
    return False

if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin if line.strip()]
    word = lines[-1]
    board = [list(row) for row in lines[:-1]]
    print(solve(board, word))
    