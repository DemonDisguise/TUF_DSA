# Sieve of eratosthenes - print all primes till n

def solve(n):
    if n < 2:
        return []
    
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i*i:n+1:i] = [False] * (((n - i*i) // i) + 1)
    
    return [i for i in range(2, n + 1) if primes[i]]

if __name__ == "__main__":
    n = int(input())
    print(*solve(n))
    