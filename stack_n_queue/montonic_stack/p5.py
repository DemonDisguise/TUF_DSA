# Trapping Rain water
#  Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain .

def solve1(arr):
    """Prefix/Suffix Max arrays"""
    n = len(arr)
    
    lft_mx = [0] * n
    rgt_mx = [0] * n
    
    lft_mx[0] = arr[0]
    for i in range(1, n):
        lft_mx[i] = max(lft_mx[i - 1], arr[i])
    
    rgt_mx[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        rgt_mx[i] = max(rgt_mx[i + 1], arr[i])
    
    water = 0
    
    for i in range(n):
        water += min(lft_mx[i], rgt_mx[i]) - arr[i]
    
    return water

def solve2(arr):
    """Monotonic stack"""
    water = 0
    stk = []
    
    for i in range(len(arr)):
        while stk and arr[stk[-1]] < arr[i]:
            btm = stk.pop()

            if not stk: break
            
            lft = stk[-1]
            
            wdth = i - lft - 1
            
            bounded_hgt = min(arr[lft], arr[i]) - arr[btm]
            
            water += wdth * bounded_hgt
        
        stk.append(i)
    
    return water

def solve3(arr):
    """Two pointers"""
    l, r = 0, len(arr) - 1
    
    lft_mx = rgt_mx = 0
    water = 0
    
    while l < r:
        if arr[l] < arr[r]:
            lft_mx = max(lft_mx, arr[l])
            water += lft_mx - arr[l]

            l += 1
        else:
            rgt_mx = max(rgt_mx, arr[r])
            water += rgt_mx - arr[r]
            
            r -= 1
    
    return water

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve3(arr))

    # 0 1 0 2 1 0 1 3 2 1 2 1