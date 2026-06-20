# First and last occurence

def solve(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    last = -1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            last = mid
            l = mid + 1
    
    l, r = 0, n - 1
    frst = -1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            frst = mid
            r = mid - 1
    
    return (frst, last)  
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    trgt = int(input())
    print(*solve(arr, trgt))