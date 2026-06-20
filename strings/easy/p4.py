# Longest Common Prefix

def solve(s):
    if not s:
        return ""
    
    s.sort()
    
    res = []
    for i in range(min(len(s[0]), len(s[-1]))):
        if s[0][i] != s[-1][i]:
            return ''.join(res)
        res.append(s[0][i])
    
    return ''.join(res)       

if __name__ == "__main__":
    s = list(input().split())
    print(solve(s))
