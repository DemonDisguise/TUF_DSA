# Leaders in an array

def solve(arr):
    n = len(arr)
    
    mx_rgt = arr[-1]
    ldrs = [mx_rgt]
    
    for i in range(n - 2, -1, -1):
        if arr[i] > mx_rgt:
            mx_rgt = arr[i]
            ldrs.append(arr[i])
    
    ldrs.reverse()
    return ldrs

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    