# Longest substring with at most k distinct characters
# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters

def solve(s, k):
    if k == 0 or not s:
        return 0
    
    mp = {}
    mx = l = 0
    
    for r, ch in enumerate(s):
        mp[ch] = mp.get(ch, 0) + 1
        
        while len(mp) > k:
            left = s[l]
            mp[left] -= 1
            if mp[left] == 0: del mp[left]
            l += 1
        
        mx = max(mx, r - l + 1)
    
    return mx

if __name__ == "__main__":
    s, k = input().split()
    print(solve(s, int(k)))
    
    # aababbcaacc 2