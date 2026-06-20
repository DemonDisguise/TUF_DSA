# Floor and ceil in sorted array

def solve(arr, x):
    n = len(arr)
    l, r = 0, n - 1
    flr, cil = -1, -1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] <= x:
            flr = arr[mid]
            l = mid + 1
        else:
            r = mid - 1
    
    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] >= x:
            cil = arr[mid]
            r = mid - 1
        else:
            l = mid + 1
    
    return (flr, cil)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())
    print(*solve(arr, x))