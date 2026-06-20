# Minimum days to make M bouquets

def solve(arr, m, n):
    if m * n > len(arr):
        return -1
    
    def can(d):
        flwrs = 0
        bqts = 0
        
        for i in arr:
            if i <= d:
                flwrs += 1
                
                if flwrs == n:
                    bqts += 1
                    flwrs = 0
            else:
                flwrs = 0

        return bqts >= m
    
    l, r = min(arr), max(arr)
    
    ans = -1
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if can(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    m, n = map(int, input().split())
    print(solve(arr, m, n))
    