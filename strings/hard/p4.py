# Rabin karp
# Uses Hashing
# Instead of comparing strings directly: compare hashes

# If hash(window) == hash(pattern) then strings MAY match, then verify actual strings
# O(n + m) time

def rabin_karp(txt, pattern):
    n, m = len(txt), len(pattern)
    
    p = 31
    mod = 10**9 + 7
    
    power = 1
    
    for _ in range(m - 1):
        power = (power * p) % mod
    
    pattern_hash = 0
    window_hash = 0
    
    for i in range(m):
        pattern_hash = (pattern_hash * p + (ord(pattern[i]) - 96)) % mod
        window_hash = (window_hash * p + (ord(txt[i]) - 96)) % mod
    
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if txt[i:i+m] == pattern:
                return i
        
        if i < n - m:
            window_hash = ((window_hash - (ord(txt[i]) - 96) * power) * p) + (ord(txt[i + m]) - 96) % mod
            window_hash %= mod
    
    return -1

if __name__ == "__main__":
    txt, pattern = input().split()
    print(rabin_karp(txt, pattern))