# Nth root of a number using binary search

def solve(n, m):
    ans = -1
    l, r = 1, m
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m:
                break
        
        if ans == m:
            return mid
        elif ans > m:
            r = mid - 1
        else:
            l = mid + 1
            
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solve(n, m))
    