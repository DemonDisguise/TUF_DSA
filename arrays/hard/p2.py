# Majority Element 
# - Find elements that appears more than N / 3 times in array

def solve(arr):
    n = len(arr)
    cnt1, cnt2 = 0, 0
    
    el1, el2 = float('-inf'), float('-inf')
    
    for num in arr:
        if cnt1 == 0 and el2 != num:
            cnt1 = 1
            el1 = num
        elif cnt2 == 0 and el1 != num:
            cnt2 = 1
            el2 = num
        elif num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    
    cnt1, cnt2 = 0, 0
    
    for num in arr:
        if num == el1:
            cnt1 += 1
        if num == el2:
            cnt2 += 1
    
    mini = n // 3 + 1
    res = []
    
    if cnt1 >= mini:
        res.append(el1)
    
    if cnt2 >= mini and el1 != el2:
        res.append(el2)
    
    return res
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))