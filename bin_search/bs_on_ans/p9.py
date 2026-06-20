# Allocate minimum number of pages

def solve(arr, m):
    if m > len(arr):
        return -1
    
    def can(p):
        stdnt_cnt = 1
        curr_pgs = 0
        
        for i in arr:
            if curr_pgs + i <= p:
                curr_pgs += i
            else:
                stdnt_cnt += 1
                curr_pgs = i
        
        return stdnt_cnt <= m
            
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
    m = int(input())
    print(solve(arr, m))
