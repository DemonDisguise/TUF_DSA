# Find peak element - II (2 adjacent cells are not same)

def solve(n, m, mtrx):
    l, r = 0, m - 1
    
    def get_mx_cl(col):
        mx = float("-inf")
        rw = -1
        for i in range(n):
            if mx < mtrx[i][col]:
                mx = mtrx[i][col]
                rw = i
        return rw
    
    while l <= r:
        mid = (l + r) >> 1
        
        row = get_mx_cl(mid)
        
        left = -1 if mid - 1 < 0 else mtrx[row][mid - 1]
        right = -1 if mid + 1 >= m else mtrx[row][mid + 1]
        
        if mtrx[row][mid] > left and mtrx[row][mid] > right:
            return [row, mid]
        elif mtrx[row][mid] < left:
            r = mid - 1
        else:
            l = mid + 1
    return [-1, -1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtrx = []
    for i in range(n):
        mtrx.append(list(map(int, input().split())))
    print(*solve(n, m, mtrx))
    