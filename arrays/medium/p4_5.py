# Kadane's algorithm: Maximum subarray sum in an array

def solve(arr):
    n = len(arr)
    mx = -float('inf')
    sm = 0
    start, end = -1, -1
    
    for i in range(n):
        if sm == 0:
            start = i
        sm += arr[i]
        if sm > mx:
            mx = sm
            end = i
        if sm < 0:
            sm = 0
    
    return (0 if mx < 0 else mx, arr[start: end + 1])

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solve(arr)
    print(res[0])
    print(*res[1])
    