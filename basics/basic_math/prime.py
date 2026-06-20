# Prime numbers

import math

def get_factors(n: int) -> list[int]:
    factors = []
    for i in range(1, int(math.isqrt(n))):
        if n % i == 0:
            factors.append(i)

            if i != n // i:
                factors.append(n // i)
    return factors

def is_prime(n: int) -> bool:
    return True if len(get_factors(n)) == 2 else False

n: int = int(input())
print(is_prime(n))