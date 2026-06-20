# Postfix to Prefix

def solve(s):
    stk = []
    
    for ch in s:
        if ch.isalnum():
            stk.append(ch)
        else:
            right = stk.pop()
            left = stk.pop()
            stk.append(f"{ch}{left}{right}")
    
    return stk[-1]

if __name__ == "__main__":
    s = input()
    print(solve(s))
    
    # abcd^e-fgh*+^*+i-