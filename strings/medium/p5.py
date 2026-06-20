# Count number of substrings that contain exactly k distinct characters

def atmost_k(s, k):
    left, res = 0, 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        res += (right - left + 1)
    
    return res

def solve(s, k):
    return atmost_k(s, k) - atmost_k(s, k - 1)

if __name__ == "__main__":
    s = input()
    k = int(input())
    print(solve(s, k))
    