# Painter's partition

def solve(arr, k):
    def can(t):
        curr_t = 0
        splt = 1
        
        for i in arr:
            if curr_t + i <= t:
                curr_t += i
            else:
                splt += 1
                curr_t = i
        
        return splt <= k
    
    l, r = max(arr), sum(arr)
    
    while l <= r:
        mid = l + ((r - l) // 2)

        if can(mid):
            r = mid - 1
        else:
            l = mid + 1
    
    return l
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
    