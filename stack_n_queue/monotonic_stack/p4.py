# Previous Smaller Element

def solve(arr):
    pse = []
    stk = []
    
    for i in arr:
        while stk and stk[-1] >= i:
            stk.pop()
        pse.append(stk[-1] if stk else -1)
        stk.append(i)
    
    return pse 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    