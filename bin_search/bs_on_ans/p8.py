# aggressive cows

def solve(arr, k):
    arr.sort()
    
    def can(d):
        cnt = 1
        lastPos = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] - lastPos >= d:
                cnt += 1
                lastPos = arr[i]
            
            if cnt >= k:
                return True
        
        return False
    
    l, r = 1, arr[-1] - arr[0]
    
    ans = 0
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if can(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1

    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))