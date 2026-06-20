# Fibonacci number
# def rec1(n: int, a: int = 0, b: int = 1) -> int:
#     if n == 0:
#         return a
#     return rec1(n - 1, b, a + b)

def rec2(n: int) -> int:
    if n <= 1:
        return n
    
    return rec2(n - 1) + rec2(n - 2)

n: int = int(input())
print(rec2(n))