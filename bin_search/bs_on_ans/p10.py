# Split array - largest sum

def solve(arr, k):
    def can(s):
        curr = 0
        splt = 1
        for i in arr:
            if curr + i <= s:
                curr += i
            else:
                splt += 1
                curr = i
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