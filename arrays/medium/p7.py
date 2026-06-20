# Rearrange array elements by sign

def solve(arr):
    n = len(arr)
    res = [0] * n
    pos = 0
    neg = 1
    
    for i in range(n):
        if arr[i] >= 0:
            res[pos] = arr[i]
            pos += 2
        else:
            res[neg] = arr[i]
            neg += 2
    
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    