# Longest Happy Prefix
# happy prefix is a string that is both proper prefix and proper suffix

def solve(s):
    n = len(s)
    lps = [0] * len(s)
    
    prev = 0
    i = 1
    
    while i < n:
        if s[i] == s[prev]:
            prev += 1
            lps[i] = prev
            i += 1
        else:
            if prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev - 1]
    return s[:lps[-1]]

if __name__ == "__main__":
    s = input()
    print(solve(s))
    