# Reverse words in a string

def solve(s: str) -> str:
    i = len(s) - 1
    res = []
    while i >= 0:
        while i >= 0 and s[i] == " ":
            i -= 1
        
        if i < 0:
            break
        
        end = i 
        
        while i >= 0 and s[i] != " ":
            i -= 1
        
        res.append(s[i + 1: end + 1])
        
    return " ".join(res)            

if __name__ == "__main__":
    s = input()
    print(solve(s))