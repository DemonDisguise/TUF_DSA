# Search in sorted 2D matrix
# eg:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

def solve(n, m, mtrx, trgt):
    if len(mtrx) == 0: return False
    
    l, r = 0, (n * m) - 1
    
    while l <= r:
        mid = l +((r - l) // 2)
        
        if mtrx[mid//m][mid%m] == trgt:
            return True
        if mtrx[mid//m][mid%m] < trgt:
            l = mid + 1
        else:
            r = mid - 1
    
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtrx = []
    for i in range(n):
        mtrx.append(list(map(int, input().split())))
    target = int(input())
    print(solve(n, m, mtrx, target))
    