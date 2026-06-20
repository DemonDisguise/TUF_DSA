# Median of row wise sorted matrix

import bisect

def solve(n, m, mtrx):
    def count_less_equal(row, mid):
        return bisect.bisect_right(row, mid)

    rows = n
    cols = m
    
    low = min(row[0] for row in mtrx)
    high = max(row[-1] for row in mtrx)
    
    while low < high:
        mid = (low + high) >> 1
        cnt = 0
        
        for row in mtrx:
            cnt += count_less_equal(row, mid)
        
        if cnt < (rows * cols + 1) // 2:
            low = mid + 1
        else:
            high = mid
    
    return low

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtrx = []
    for i in range(n):
        mtrx.append(list(map(int, input().split())))
    print(solve(n, m, mtrx))
