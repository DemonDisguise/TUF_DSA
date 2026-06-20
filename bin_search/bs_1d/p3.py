# Upper bound of x 
# upper bound is the smallest index, ind, where arr[ind] > x

def solve(arr, x):
    l, r = 0, len(arr) - 1
    ans = -1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] > x:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())
    print(solve(arr, x))
    