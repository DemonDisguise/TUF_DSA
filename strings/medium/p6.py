# Longest Palindromic Substring

def solve(s):
    t = '#' + '#'.join(s) + '#'
    
    n = len(t)
    
    center, right = 0, 0
    mx_len = 0
    start = 0
    
    p = [0] * n
    
    for i in range(n):
        mirror = 2 * center - i
        
        if i < right:
            p[i] = min(right - i, p[mirror])
            
        l = i - (p[i] + 1)
        r = i + (p[i] + 1)
        
        while i >= 0 and r < n and t[l] == t[r]:
            p[i] += 1
            l -= 1
            r += 1
        
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        if p[i] > mx_len:
            mx_len = p[i]
            
            start = (i - mx_len) // 2
    
    return s[start:start+mx_len]       

if __name__ == "__main__":
    s = input()
    print(solve(s))
