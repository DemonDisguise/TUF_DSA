# Peak element in array

def solve(arr):
    n = len(arr)
    l, r = 1, n - 2
    
    while l < r:
        mid = l + ((r - l) // 2)
        
        if arr[mid] > arr[mid + 1]:
            r = mid
        else:
            l = mid + 1
        
        return l       

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))