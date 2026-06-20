# Find out how many times the array has benn rotated

def solve(arr):
    n = len(arr)
    
    l, r = 0, n - 1
    
    while l < r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid
    
    return l

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))