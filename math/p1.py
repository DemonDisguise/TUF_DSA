# Print divisors of a number

import math

def solve(n):
    res = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
        
    return sorted(res)

if __name__ == "__main__":
    n = int(input())
    print(*solve(n))
    