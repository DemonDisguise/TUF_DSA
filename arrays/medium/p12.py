# Rotate n x n matrix by 90 degree

def solve(mtrx):
    m = len(mtrx)
    n = len(mtrx[0])
    
    # transpose
    for i in range(0, m - 1):
        for j in range(i, n):
            mtrx[i][j], mtrx[j][i] = mtrx[j][i], mtrx[i][j]
    
    for i in mtrx:
        i.reverse()

if __name__ == "__main__":
    m, n = map(int, input().split())
    mtrx = []
    for i in range(m):
        mtrx.append(list(map(int, input().split())))
    solve(mtrx)
    for i in range(m):
        print(*mtrx[i])