# Sum of Subarray Ranges
# Given an integer array nums, determine the range of a subarray, defined as the difference between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.
# A subarray is defined as a contiguous, non-empty sequence of elements within the array.

""" def subarr_min(arr):
    n = len(arr)
    stk = []
    nse = [n] * n
    psee = [-1] * n
    
    for i in range(n):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk: psee[i] = stk[-1]
        stk.append(i)
    
    stk.clear()
    
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()
        if stk: nse[i] = stk[-1]
        stk.append(i)
    
    ans = 0
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        
        ans += arr[i] * left * right
    
    return ans

def subarr_max(arr):
    n = len(arr)
    stk = []
    plee = [-1] * n
    nle = [n] * n
    
    for i in range(n):
        while stk and arr[stk[-1]] < arr[i]:
            stk.pop()
        if stk: plee[i] = stk[-1]
        stk.append(i)
    
    stk.clear()
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()
        if stk: nle[i] = stk[-1]
        stk.append(i)
    
    ans = 0
    for i in range(n):
        left = i - plee[i]
        right = nle[i] - i
        ans += arr[i] * left * right

    return ans

def solve(arr):
    return subarr_max(arr) - subarr_min(arr) """

def solve(arr):
    n = len(arr)
    
    stk = []
    ans = 0
    
    for i in range(n + 1):
        curr = arr[i] if i < n else float('-inf')

        while stk and arr[stk[-1]] > curr:
            mid = stk.pop()
        
            left = mid - (stk[-1] if stk else -1)
            right = i - mid
            
            ans -= arr[mid] * left * right
        stk.append(i)
    
    stk.clear()

    for i in range(n + 1):
        curr = arr[i] if i < n else float('inf')
        
        while stk and arr[stk[-1]] < curr:
            mid = stk.pop()

            left = mid - (stk[-1] if stk else -1)
            right = i - mid

            ans += arr[mid] * left * right
            
        stk.append(i)
    
    return ans
 
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
