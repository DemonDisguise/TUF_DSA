# Longest repeating character replacement
""" Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. 
This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter. """
# len - maxf <= k

def solve(s, k):
    l = 0
    mp = {}
    mx_freq = 0
    mx = 0

    for r, ch in enumerate(s):

        mp[ch] = mp.get(ch, 0) + 1

        mx_freq = max(mx_freq, mp[ch])

        while (r - l + 1) - mx_freq > k:
            mp[s[l]] -= 1
            l += 1

        mx = max(mx, r - l + 1)

    return mx

if __name__ == "__main__":
    s, k = input().split()
    print(solve(s, int(k)))
    
    # AABABBA 1