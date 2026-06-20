# Combination sum II 
# Find all unique combinations - each number may only be used once in combination

def helper(ind, target, curr, arr, ans):
    if target == 0:
        ans.append(curr[:])
        return

    for i in range(ind, len(arr)):
        if i > ind and arr[i] == arr[i - 1]:
            continue
        
        if arr[i] > target:
            break
        
        curr.append(arr[i])
        
        helper(i + 1, target - arr[i], curr, arr, ans)
        
        curr.pop()

def solve(arr, k):
    arr.sort()
    
    ans = []
    
    helper(0, k, [], arr, ans)
    
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    res = solve(arr, k)
    for i in res:
        print(*i)
    