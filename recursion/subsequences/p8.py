# Subset Sum: Sum of all subsets

def solve1(arr):
    """ Bitmask approach """
    n = len(arr)
    res = []
    
    for i in range(1 << n):
        sm = 0
        for j in range(n):
            if (i & (1 << j)):
                sm += arr[j]
        res.append(sm)
    
    return sorted(res)

def helper(index, curr, res, arr):
    if index == len(arr):
        res.append(curr)
        return
    
    helper(index + 1, curr, res, arr)
    
    curr += arr[index]
    helper(index + 1, curr, res, arr)
    curr -= arr[index]

def solve2(arr):
    """ Recursive Approach """  
    res = []
    
    helper(0, 0, res, arr)
    
    return res
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve2(arr))