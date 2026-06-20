# Largest odd number in a string

def solve(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] in "13579":
            return s[:i+1].lstrip('0')
    
    return ""

if __name__ == "__main__":
    s = input()
    print(solve(s))