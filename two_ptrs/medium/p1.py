# Longest Substring Without Repeating Characters

def solve(s):
    hshmp = {}
    l = 0
    mx_len = 0
    
    for r, ch in enumerate(s):
        if ch in hshmp:
            l = max(l, hshmp[ch] + 1)
        
        hshmp[ch] = r
        
        mx_len = max(mx_len, r - l + 1)
    
    return mx_len

if __name__ == "__main__":
    s = input()
    print(solve(s))
    
    # abcddabac