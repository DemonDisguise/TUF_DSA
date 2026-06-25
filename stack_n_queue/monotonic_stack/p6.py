# Sum of subarray minimums
#  Given an array of integers arr of size n, calculate the sum of the minimum value in each (contiguous) subarray of arr. Since the result may be large, return the answer modulo 10⁹ +7

def solve(arr):
    MOD = 10**9 + 7
    n = len(arr)
    stk = []
    nse = [n] * n
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()
        if stk: nse[i] = stk[-1]
        stk.append(i)
    
    stk.clear()
    psee = [-1] * n
    for i in range(n):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk: psee[i] = stk[-1]
        stk.append(i)
    
    print(psee, nse)
    
    res = 0
    
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        
        res += arr[i] * left * right
    
    return res % MOD

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

    # 3 1 2 5