# Prefix to Infix 

def solve(s):
    stk = []
    
    for ch in reversed(s):
        if ch.isalnum():
            stk.append(ch)
        else:
            left = stk.pop()
            right = stk.pop()

            stk.append(f"({left}{ch}{right})")
    
    return stk[-1]

if __name__ == "__main__":
    s = input()
    print(solve(s))

    # -+a*b^-^cde+f*ghi