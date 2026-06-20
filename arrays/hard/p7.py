# Merge overlapping sub-intervals

def solve(intrvls):
    n = len(intrvls)
    intrvls.sort()
    res = []
    
    for start, end in intrvls:
        if not res or res[-1][1] < start:
            res.append([start, end])
        else:
            res[-1][1] = max(res[-1][1], end) 
    
    return res    

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    intrvls = [[nums[i], nums[i + 1]] for i in range(0, len(nums), 2)]
    res = solve(intrvls)
    for i in res:
        print(*i)
        