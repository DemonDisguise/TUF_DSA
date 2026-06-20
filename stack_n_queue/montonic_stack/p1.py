# Next Greater Element

def solve(arr):
    n = len(arr)
    stk = []
    res = [-1] * n
    
    for i in range(n - 1, -1, -1):
        while stk and stk[-1] <= arr[i]:
            stk.pop()
        
        if stk: res[i] = stk[-1]
        
        stk.append(arr[i])
    
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
