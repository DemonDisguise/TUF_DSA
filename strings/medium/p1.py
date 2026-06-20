# Sort characters by frequency

def solve(s):
    freq = [0] * 26
    
    res = []
    
    for i in s:
        freq[ord(i) - 97] += 1 
    
    for i in range(26):
        if freq[i] > 0:
            res.append((freq[i], chr(i + 97)))
    
    res.sort(key=lambda x: -x[0])
    
    return [ch for _, ch in res]

if __name__ == "__main__":
    s = input()
    print(*solve(s))
    