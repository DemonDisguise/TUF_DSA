# Factorial of n numbers
def rec1(n: int) -> int:
    if n == 1:
        return 1
    
    return n * rec1(n - 1)

n: int = int(input())
print(rec1(n))