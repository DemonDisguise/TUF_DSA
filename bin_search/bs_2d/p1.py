# Find the row with the maximum number of 1's

def solve(n, m, mtrx):
    ans = -1
    mx_ones = 0
    
    for i in range(n):
        l, r = 0, m - 1
        
        ind = -1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            
            if mtrx[i][mid] == 1:
                ind = mid
                r = mid - 1
            else:
                l = mid + 1
        
        if ind != -1:
            if m - ind > mx_ones:
                mx_ones = m - ind
                ans = i
    
    return ans              

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtrx = []
    for i in range(n):
        mtrx.append(list(map(int, input().split())))
    print(solve(n, m, mtrx))
    