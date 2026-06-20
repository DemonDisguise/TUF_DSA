# Knutt Morris Pratt (KMP)
# Avoids rechecking characters
# Instead of moving fully ahead after mismatch, it uses previous information
# O(n + m) time

def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    
    prev = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[prev]:
            prev += 1
            lps[i] = prev
            i += 1
        else:
            if prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev - 1]
    
    return lps

def kmp(txt, pattern):
    n, m = len(txt), len(pattern)
    
    lps = build_lps(pattern)
    
    i = 0
    j = 0
    
    while i < n:
        if txt[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            return i - m
        
        elif i < n and txt[i] != pattern[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    
    return -1

if __name__ == "__main__":
    txt, pattern = input().split()
    print(kmp(txt, pattern))