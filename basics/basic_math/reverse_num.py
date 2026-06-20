# Reverse the number

def reverse_num(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev_num = 0
    while n:
        rev_num = rev_num * 10 + n % 10
        n //= 10
    
    return sign * rev_num

n: int = int(input())
print(reverse_num(n))