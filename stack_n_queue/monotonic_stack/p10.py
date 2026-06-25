# Area of largest rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1 return the area of the largest rectangle in histogram. 

def solve(arr):
    mx = 0
    n = len(arr)

    stk = []

    for i in range(n):
        while stk and arr[stk[-1]] > arr[i]:
            mid = stk.pop()
            lft = stk[-1] if stk else -1
            mx = max(mx, arr[mid] * (i - lft - 1))
        stk.append(i)
    
    while stk:
        mid = stk.pop()
        lft = stk[-1] if stk else -1
        mx = max(mx, arr[mid] * (n - lft - 1))
    return mx

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))