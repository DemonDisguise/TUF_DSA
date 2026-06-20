# Second largest 

def solve(arr):
    n = len(arr)
    largest = arr[0]
    sec_largest = -1

    
    for i in range(1, n):
        if arr[i] > largest:
            sec_largest = largest
            largest = arr[i]
        elif arr[i] > sec_largest and arr[i] != largest:
            sec_largest = arr[i]
    
    return sec_largest

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))