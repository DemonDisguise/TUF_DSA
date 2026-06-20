# Print the matrix in spiral manner

def solve(mtrx):
    m = len(mtrx)
    n = len(mtrx[0])
    
    res = []
    
    top, btm = 0, m - 1
    lft, rgt = 0, n - 1
    
    while top <= btm and lft <= rgt:
        # left -> right
        for j in range(lft, rgt + 1):
            res.append(mtrx[top][j])
        top += 1
        
        # top -> bottom
        for i in range(top, btm + 1):
            res.append(mtrx[i][rgt])
        rgt -= 1
        
        # right -> left
        for j in range(rgt, lft - 1, -1):
            res.append(mtrx[btm][j])
        btm -= 1
        
        # bottom -> top
        for i in range(btm, top - 1, -1):
            res.append(mtrx[i][lft])
        lft += 1
    
    return res   

if __name__ == "__main__":
    m, n = map(int, input().split())
    mtrx = []
    for i in range(m):
        mtrx.append(list(map(int, input().split())))
    res = solve(mtrx)
    print(*res)
