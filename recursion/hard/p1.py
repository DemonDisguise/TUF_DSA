# Print all permutations of a array

def helper(ind, arr, res):
    if ind == len(arr):
        res.append(arr[:])
        return
    
    for i in range(ind, len(arr)):
        arr[ind], arr[i] = arr[i], arr[ind]
        
        helper(ind + 1, arr, res)
        
        arr[ind], arr[i] = arr[i], arr[ind]

def solve(arr):
    res = []
    helper(0, arr, res)
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solve(arr)
    for i in res:
        print(*i)
    