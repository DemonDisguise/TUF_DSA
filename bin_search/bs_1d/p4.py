# Search insert position

def solve(arr, x):
    n = len(arr)
    l, r = 0, n - 1
    ans = n
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] >= x:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())
    print(solve(arr, x))
    