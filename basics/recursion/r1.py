# Print 1 to n using recursion
# Using forward recursion
def rec1(n, curr=1):
    if curr > n:
        return
    
    print(curr, end=" ")
    rec1(n, curr + 1)

# Using backtracking
def rec2(n):
    if n == 0:
        return
    
    rec2(n - 1)
    print(n, end=" ")

n: int = int(input())
rec1(n)
print()
rec2(n)
print()