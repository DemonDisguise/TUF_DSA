# Remove duplicates from sorted array

def solve(arr):
    if not arr:
        return 0
    n = len(arr)
    i = 0
    
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))            
    k = solve(arr)
    print(k)
    print(*arr[:k])
    