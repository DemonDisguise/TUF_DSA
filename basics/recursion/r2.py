# Pring n to 1 using recursion
# Using forward recursion
def rec1(n: int) -> None:
    if n == 0:
        return
    
    print(n, end=" ")
    rec1(n - 1)

# Using backtracking
def rec2(n: int, curr: int=1) -> None:
    if curr > n:
        return 
    
    rec2(n, curr + 1)
    print(curr, end=" ")

n: int = int(input())
rec1(n)
print()
rec2(n)
print()