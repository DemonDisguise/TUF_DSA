# Next Greater Element 2
# Given circular integer array, find the NGE

def solve(arr):
    n = len(arr)
    nge = [-1] * n
    stk = []

    for i in range(2*n-1, -1, -1):
        curr = arr[i%n]
        while stk and stk[-1] <= curr:
            stk.pop()
        
        if i < n:
            if stk: nge[i] = stk[-1]

        stk.append(curr)
    
    return nge

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    