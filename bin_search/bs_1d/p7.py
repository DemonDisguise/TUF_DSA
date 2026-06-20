# Count occurences in sorted array

def solve(arr, x):
    n = len(arr)
    
    def frst_occur(arr, n, x):
        l, r = 0, n - 1
        frst = -1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            
            if arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
            else:
                frst = mid
                r = mid - 1
        
        return frst
    
    def last_occur(arr, n, x):
        l, r = 0, n - 1
        last = 0
        
        while l <= r:
            mid = l + ((r - l) // 2)
            
            if arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
            else:
                last = mid
                l = mid + 1
        
        return last

    frst = frst_occur(arr, n, x)
    if frst == -1:
        return 0
    last = last_occur(arr, n, x)
    
    return last - frst + 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())
    print(solve(arr, x))
    