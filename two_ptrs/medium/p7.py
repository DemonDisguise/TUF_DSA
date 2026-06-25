# Number of substrings containing all three characters
# Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.

def solve(s):
    last = [-1, -1, -1]  
    cnt = 0

    for r, ch in enumerate(s):
        last[ord(ch) - 97] = r  

        m = min(last)
        if m != -1:
            cnt += m + 1

    return cnt

if __name__ == "__main__":
    s = input()
    print(solve(s))
    
    # abcba