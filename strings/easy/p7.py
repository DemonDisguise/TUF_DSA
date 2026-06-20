# Check if two strings are anagrams of each other

def solve(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = [0] * 26
    
    for i in s1:
        freq[ord(i) - 65] += 1
    
    for i in s2:
        freq[ord(i) - 65] -= 1
    
    return all(freq[i] == 0 for i in range(26))

if __name__ == "__main__":
    s1, s2 = input().split()
    print(solve(s1, s2))
    