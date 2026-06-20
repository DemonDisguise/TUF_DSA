# Combination Sum - 1
# given array of distinct integers and target 
# return the list of all unique combinations where the chosen numbers sum to target

def helper(ind, target, arr, ans, ds):
    if ind == len(arr):
        if target == 0:
            ans.append(ds[:])
        return
    
    if arr[ind] <= target:
        ds.append(arr[ind])
        helper(ind, target - arr[ind], arr, ans, ds)
        ds.pop()
    
    helper(ind + 1, target, arr, ans, ds)

def solve(arr, k):
    ans = []
    
    helper(0, k, arr, ans, [])
    
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    res = solve(arr, k)
    for i in res:
        print(*i)
        