# Find the two numbers appearing odd number of times

def solve(arr):
    xor = 0
    
    for i in arr:
        xor ^= i
    
    r = (xor & (xor - 1)) ^ xor
    
    x1, x2 = 0, 0
    
    for i in arr:
        if i & r:
            x1 ^= i
        else:
            x2 ^= i
    
    return [x1, x2] if x1 < x2 else [x2, x1]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    