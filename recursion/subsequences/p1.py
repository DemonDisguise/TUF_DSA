# Generate all binary strings of length n that do not contain consecutive 1s

def helper(n, curr, res):
    if len(curr) == n:
        res.append(''.join(curr))
        return
    
    curr.append("0")
    helper(n, curr, res)
    curr.pop()
    
    if not curr or curr[-1] != '1':
        curr.append("1")
        helper(n, curr, res)
        curr.pop()
        

def solve(n):
    res = []
    
    helper(n, [], res)
    
    return res

if __name__ == "__main__":
    n = int(input())
    print(*solve(n))