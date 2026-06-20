# Next smaller element

def solve(arr):
    n = len(arr)
    nse = [-1]*n
    stk = []
    
    for i in range(n-1, -1, -1):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        
        if stk: nse[i] = stk[-1]
        stk.append(arr[i])
    
    return nse 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
