# Search element in a rotated sorted array - I

def solve(arr, k):
    n = len(arr)
    l, r = 0, n - 1
    
    while l <= r:
        mid = (l + r) >> 1
        
        if arr[mid] == k:
            return mid
        
        if arr[l] <= arr[mid]:
            if arr[l] <= k <= arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] <= k <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
    