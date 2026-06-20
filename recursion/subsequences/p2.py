# Generate Paranthesis 
# Given n pairs of parentheses, generate all combinations of well formed parentheses

def helper(n, open, close, curr, res):
    if len(curr) == 2 * n:
        res.append(''.join(curr))
        return
    
    if open < n:
        curr.append('(')
        helper(n, open + 1, close, curr, res)
        curr.pop()
    
    if close < open:
        curr.append(')')
        helper(n, open, close + 1, curr, res)
        curr.pop()

def solve(n):
    res = []
    
    helper(n, 0, 0, [], res)
    
    return res

if __name__ == "__main__":
    n = int(input())
    print(*solve(n))
    