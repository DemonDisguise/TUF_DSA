# Largest subarray with sum 0

def solve(arr):
    n = len(arr)
    sm = 0
    mx = float('-inf')
    
    hshmp = {} 
    
    for i in range(n):
        sm += arr[i]
        if sm == 0: mx += 1
        else:
            if sm in hshmp:
                mx = max(mx, i - hshmp[sm])
            else:
                hshmp[sm] = i
    
    return mx    

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))