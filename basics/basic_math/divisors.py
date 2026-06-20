# Divisors

import math

def get_factors(n: int) -> list[int]:
    factors: list[int] = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)

            if i != n // i:
                factors.append(n // i)
    return factors

n: int = int(input())
print(get_factors(n))