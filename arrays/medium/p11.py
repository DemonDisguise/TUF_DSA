# Set matrix zeroes

def solve(mtrx):
    m = len(mtrx)
    n = len(mtrx)
    
    frst_rw_zro = False
    frst_cl_zro = False
    
    for j in range(n):
        if mtrx[0][j] == 0:
            frst_rw_zro = True
            break
    
    for i in range(m):
        if mtrx[i][0] == 0:
            frst_cl_zro = True
            break
    
    for i in range(1, m):
        for j in range(1, n):
            if mtrx[i][j] == 0:
                mtrx[i][0] = 0
                mtrx[0][j] = 0
    
    for i in range(1, m):
        for j in range(1, n):
            if mtrx[i][0] == 0 or mtrx[0][j] == 0:
                mtrx[i][j] = 0
    
    if frst_rw_zro:
        for j in range(n):
            mtrx[0][j] = 0
    
    if frst_cl_zro:
        for i in range(m):
            mtrx[i][0] = 0

if __name__ == "__main__":
    r, c = map(int, input().split())
    mtrx = []
    for i in range(r):
        mtrx.append(list(map(int, input().split())))
    solve(mtrx)
    for i in range(r):
        print(*mtrx[i])
           