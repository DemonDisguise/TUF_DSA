# Minimum window substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

from collections import Counter

def solve(s, t):
    if len(t) > len(s):
        return ""

    need = Counter(t)
    window = {}

    formed = 0
    required = len(need)

    l = 0
    start = 0
    min_len = float('inf')

    for r, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
            formed += 1

        while formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                start = l

            left = s[l]
            window[left] -= 1

            if left in need and window[left] < need[left]:
                formed -= 1

            l += 1

    return "" if min_len == float('inf') else s[start:start + min_len]
    
if __name__ == "__main__":
    s, t = input().split()
    print(solve(s, t))
    
    # ADOBECODEBANC ABC