# Sum of Beauty of all substring
# Difference between the frequency of most frequent character and least frequent character (excluding characters that do not appear) in that string

def solve(s):
    a = [ord(ch) - 97 for ch in s]
    
    n = len(a)
    res = 0
    
    for i in range(n):
        cnt = [0] * 26
        freq = [0] * (n + 1)
        
        mn = 0
        mx = 0
        
        for j in range(i, n):
            idx = a[j]
            
            old = cnt[idx]
            
            if old:
                freq[old] -= 1
            
            new = old + 1
            
            cnt[idx] = new
            freq[new] += 1
            
            if new > mx:
                mx = new
            
            if mn == 0 or new < mn:
                mn = new
            elif old == mn and freq[old] == 0:
                while mn <= mx and freq[mn] == 0:
                    mn += 1
            
            res += mx - mn

    return res

if __name__ == "__main__":
    s = input()
    print(solve(s))
    