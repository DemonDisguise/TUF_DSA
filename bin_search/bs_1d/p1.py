# Search x in sorted array

def solve(arr, target):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(solve(arr, target))