# Subset - II 
# Print all the unique subsets

def helper(ind, curr, res, arr):
    res.append(curr[:])
    
    for i in range(ind, len(arr)):
        if i > ind and arr[i] == arr[i - 1]:
            continue
        
        curr.append(arr[i])
        helper(i + 1, curr, res, arr)
        curr.pop()
          
def solve(arr):
    arr.sort()
    res = []
    
    helper(0, [], res, arr)
    
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solve(arr)
    for i in res:
        print(*i)