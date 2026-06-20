# single element in a sorted array

def solve(arr):
    n = len(arr)
    l, r = 1, n - 2
    
    if n == 1:
        return arr[0]

    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        if (not mid & 1 and arr[mid] == arr[mid + 1]) or (mid & 1 and arr[mid] == arr[mid - 1]):
            l = mid + 1
        else:
            r = mid - 1
        
    return -1
            
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))