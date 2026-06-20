# Find smallest divisor given a threshold

def solve(arr, lmt):
    def can(div):
        ans = 0
        for i in arr:
            ans += (i + div - 1) // div
            if ans > lmt:
                return False
        
        return True
       
    l, r = 1, max(arr)
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
    lmt = int(input())
    print(solve(arr, lmt))
    