# Maximum product subarray in an array

def solve1(arr):
    n = len(arr)
    
    pre, suff = 1, 1
    
    ans = float('-inf')
    
    for i in range(n):
        
        if pre == 0:
            pre = 1
        
        if suff == 0:
            suff = 1
        
        pre *= arr[i]
        
        suff *= arr[n - i - 1]
        
        ans = max(ans, pre, suff)

    return ans

def solve2(arr):
    res = arr[0]
    max_prd = arr[0]
    min_prd = arr[0]
    
    for i in range(1, len(arr)):
        curr = arr[i]
        
        if curr < 0:
            max_prd, min_prd = min_prd, max_prd
        
        max_prd = max(curr, max_prd * curr)
        min_prd = min(curr, min_prd * curr)

        res = max(res, max_prd)
    
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve2(arr))
    