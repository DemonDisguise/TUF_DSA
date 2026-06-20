# Minimum bit flips to convert number

from bit_manipulation.bit import bit

def solve(start, goal):
    num = start ^ goal
    
    cnt = 0
    
    while num:
        if num & 1:
            cnt += 1
        num >>= 1
    
    return cnt
        

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(bit(a), bit(b))
    print(solve(a, b))