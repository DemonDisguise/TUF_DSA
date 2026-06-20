# Find repeating and missing numbers - in [1, n] array 
# each value appears exactly once, 
# except A which appears twice and B which is missing return that

def solve1(arr):
    """Math method"""
    n = len(arr)
    sn = (n * (n + 1)) // 2
    s2n = (n * (n + 1) * (2*n+1)) // 6
    s, s2 = 0, 0
    
    for i in arr:
        s += i
        s2 += i * i
    
    val1 = s - sn # x - y
    val2 = s2 - s2n
    
    val2 = val2 // val1 # x + y
    x = (val1 + val2) // 2
    y = x - val1
    
    return [x, y]

def solve2(arr):
    """XOR method"""
    n = len(arr)
    
    xr = 0
    
    for i, num in enumerate(arr, start=1):
        xr ^= num
        xr ^= 1
    
    bit = xr & -xr
    
    one, zero = 0, 0
    
    for i, num in enumerate(arr, start=1):
        if num & bit:
            one ^= num
        else:
            zero ^= num
        
        if i & bit:
            one ^= i
        else:
            zero ^= i
    
    cnt = arr.count(one)
    
    return [one, zero] if cnt == 2 else [zero, one]

if __name__ == "__main__": 
    arr = list(map(int, input().split()))
    print(*solve2(arr))
