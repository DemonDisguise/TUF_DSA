# Count subarray sum equals k

def solve(arr, k):
    n = len(arr)
    prfx_cnt = {0: 1} 
    prfx_sm = 0
    cnt = 0
    
    for i in arr:
        prfx_sm += i
        if prfx_sm - k in prfx_cnt:
            cnt += prfx_cnt[prfx_sm - k]
        prfx_cnt[prfx_sm] = prfx_cnt.get(prfx_sm, 0) + 1
    
    return cnt      

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
