# Minimum number of bracket reversals needed to make ana expression balanced

def solve(s: str) -> int:
    n = len(s)
    if n & 1:
        return -1
    
    opnd = 0
    clsd = 0
    
    for i in s:
        if i == "(":
            opnd += 1
        else:
            if opnd > 0:
                opnd -= 1
            else:
                clsd += 1
    
    return (opnd + 1) // 2 + (clsd + 1) // 2

if __name__ == "__main__":
    s = input()
    print(solve(s))
    