# Count the nubmer of set bits
# Brain Kernighan's algo

from bit_manipulation.bit import bit

def solve(n):
    cnt = 0
    
    while n:
        n &= (n - 1)
        cnt += 1
    
    return cnt

if __name__ == "__main__":
    n = int(input())
    print(bit(n))
    print(solve(n))
    