# Z - algorithm

# Build pattern + '$' + text
# Now compute: Z[i] = longest substring starting at i that matches prefix

# if any Z[i] == len(pattern) return
# the [L, R] window remembers already matched ranges. So characters are not compared repeatedly. 
# O(n) - time

def z_algorithm(s):
    n = len(s)
    
    z = [0] * n
    
    l = 0
    r = 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - 1])
            
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    
    return z

def find_pattern(txt, pattern):
    combined = pattern + '$' + txt
    
    z = z_algorithm(combined)
    
    m = len(pattern)
    
    for i in range(len(z)):
        if z[i] == m:
            return i - m - 1
    
    return -1

if __name__ == "__main__":
    txt, pattern = input().split()
    print(find_pattern(txt, pattern))
