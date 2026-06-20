# Finding sqrt of a number in binary search

def solve(n):
    if n < 2:
        return n
    
    l, r = 1, n // 2
    ans = 0
    
    while l <= r:
        mid = (l + r) >> 1
        
        if mid * mid <= n:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return ans

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
    