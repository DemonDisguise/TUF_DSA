# Sort an array of 0s, 1s and 2s
# Dutch national flag

def solve(arr):
    n = len(arr)
    
    low, mid, high = 0, 0, n - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        else:
            mid += 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    solve(arr)
    print(*arr)
            