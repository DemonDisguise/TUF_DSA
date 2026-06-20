# Count digits

def count_digits(n: int) -> int:
    digits = 0
    
    while n > 0:
        digits += 1
        n //= 10
    
    return digits

n: int = int(input())
print(count_digits(n))