# Prefix to Postfix

def solve(s):
    stk = []
    
    for ch in reversed(s):
        if ch.isalnum():
            stk.append(ch)
        else:
            left = stk.pop()
            right = stk.pop()
            
            stk.append(f"{left}{right}{ch}")
    
    return stk[-1]

if __name__ == "__main__":
    s = input()
    print(solve(s))