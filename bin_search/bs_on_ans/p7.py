# Kth missing positive number

def solve(arr, k):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        miss = arr[mid] - (mid + 1)
        
        if miss < k:
            l = mid + 1
        else:
            r = mid - 1
    
    return k + r + 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
    