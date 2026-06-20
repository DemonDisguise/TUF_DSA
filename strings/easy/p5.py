# Isomorphic string
# Given two strings s and t
# If characters in s can be replaced to get t. 
# All occurences of a character must be replaced with another character while preserving the order of characters
# No two characters may map to the same character, but a character may map to itself

def solve(s, t):
    if len(s) != len(t):
        return False

    m1, m2 = [0] * 256, [0] * 256
    
    for i in range(len(s)):
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False
        
        m1[ord(s[i])] = i + 1
        m2[ord(t[i])] = i + 1
    
    return True

if __name__ == "__main__":
    s,t = input().split()
    print(solve(s, t))