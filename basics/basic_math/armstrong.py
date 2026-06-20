# Armstrong number
# An armstrong number is a number that is equal to sum of its own digits each raised to the power of the number of digits
def is_armstrong(n: int) -> bool:
    n = abs(n)
    tmp = n
    digits = 0
    
    while tmp:
        digits += 1
        tmp //= 10
    
    tmp = n
    res = 0
    while tmp:
        res += (tmp % 10) ** digits
        tmp //= 10
    
    return True if n == res else False 

n: int = int(input())
print(is_armstrong(n))