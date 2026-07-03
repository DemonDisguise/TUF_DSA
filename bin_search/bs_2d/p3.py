# Search in row and column wise sorted matrix: return the index of the target
# eg.(rows sorted, columns sorted separately)
# 1 4 7 11 15
# 2 5 8 12 19
# 3 6 9 16 22
# 10 13 14 17 24
# 18 21 23 26 30

def solve(n: int, m: int, mtrx: list[list[int]], target: int) -> list[int]:
    row, col = 0, m - 1 # or row = n - 1, col = 0
    
    while row < n and col >= 0:
        if mtrx[row][col] == target:
            return [row, col]
        if mtrx[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return [-1, -1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtrx = []
    for i in range(n):
        mtrx.append(list(map(int, input().split())))
    target = int(input())
    print(*solve(n, m, mtrx, target))