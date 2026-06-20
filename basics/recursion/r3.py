# Sum of first n numbers
def rec1(n: int) -> int:
    if n == 0:
        return 0
    
    return n + rec1(n - 1)

n: int = int(input())
print(rec1(n))
    