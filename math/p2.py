# Prime Factors of a number

def solve(n):
    res = []
    
    while not n & 1:
        res.append(2)
        n //= 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            res.append(i)
            n //= i
        i += 2 
    
    if n > 1:
        res.append(n)
    
    return res
    
if __name__ == "__main__":
    n = int(input())
    print(*solve(n))
    