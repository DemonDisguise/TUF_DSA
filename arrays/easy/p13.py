# Length of the longest subarray with zero sum

def solve(arr):
    n = len(arr)
    hshmp = {}
    maxi = 0
    s = 0
    
    for i in range(n):
        s += arr[i]
        
        if s == 0:
            maxi = i + 1
        else:
            if s in hshmp:
                maxi = max(maxi, i - hshmp[s])
            else:
                hshmp[s] = i
    
    return maxi

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    