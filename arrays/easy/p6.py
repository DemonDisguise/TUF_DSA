# Move zeros to end

def solve(arr):
    n = len(arr)
    j = -1
    
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    
    if j == -1:
        return
    
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    solve(arr)
    print(*arr)