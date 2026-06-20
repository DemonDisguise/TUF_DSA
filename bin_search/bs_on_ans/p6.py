# Capacity to ship packages withing d days

def solve(arr, d):
    def can(cap):
        days = 1
        curr = 0
        
        for i in arr:
            if curr + i <= cap:
                curr += i
            else:
                days += 1
                curr = i
        
        return days <= d      
    
    l, r = max(arr), sum(arr)
    ans = r
    
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
    d = int(input())
    print(solve(arr, d))