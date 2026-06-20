# Power set: all possible subsequences

def solve1(s):
    "bit approach"
    n = len(s)
    
    res = []
    
    for i in range(0, 1 << n):
        sub = []
        for j in range(n):
            if (i & (1 << j)):
                sub.append(s[j])
        res.append(''.join(sub))
    
    return sorted(res)

def helper(s, ind, curr, res):
    if ind == len(s):
        res.append("".join(curr))
        return

    helper(s, ind + 1, curr, res)
    
    curr.append(s[ind])
    helper(s, ind + 1, curr, res)
    
    curr.pop()
        
def solve2(s):
    res = []
    
    helper(s, 0, [], res)
    
    return res

if __name__ == "__main__":
    s = input()
    print(solve1(s))
    print(solve2(s))
    