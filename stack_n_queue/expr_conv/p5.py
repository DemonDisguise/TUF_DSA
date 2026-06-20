# Postfix to Infix

def solve(s):
    stk = []
    
    for ch in s:
        if ch.isalnum():
            stk.append(ch)
        else:
            right = stk.pop()
            left = stk.pop()
            stk.append(f"({left}{ch}{right})")
    
    return stk[-1]

if __name__ == "__main__":
    s = input()
    print(solve(s))