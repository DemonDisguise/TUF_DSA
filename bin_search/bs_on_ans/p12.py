# Minimise maximum distance between gas stations

def solve(arr, k):
    def can(d):
        needed = 0
        
        for i in range(1, len(arr)):
            gap = arr[i] - arr[i - 1]
            
            stns = int(gap / d)
            
            if gap == d * stns:
                stns -= 1
            
            needed += stns
            
        return needed <= k
    
    l, r = 0, max(arr[i] - arr[i - 1] for i in range(1, len(arr)))
    
    while r - l > 1e-6:
        mid = (l + r) / 2.0
        
        if can(mid):
            r = mid 
        else:
            l = mid
        
    return r 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))