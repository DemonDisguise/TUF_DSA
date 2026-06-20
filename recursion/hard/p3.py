# Kth permutation sequence

from math import factorial

def solve(k, n):
    nums = [str(i) for i in range(1, n + 1)]
    k -= 1
    ans = []
    
    for i in range(n, 0, -1):
        fact = factorial(i - 1)
        
        idx = k // fact
        ans.append(nums.pop(idx))
        
        k %= fact
    
    return ''.join(ans)
    
if __name__ == "__main__":
    k = int(input())
    n = int(input())
    print(solve(k, n))
    