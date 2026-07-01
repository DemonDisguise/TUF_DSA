# Valid Paranthesis checker
""" Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "". """

def solve(s: str) -> bool:
    min = max = 0
    for ch in s:
        if ch == "(":
            min += 1
            max += 1
        elif ch == ")":
            min -= 1
            max -= 1
        else:
            min -= 1
            max += 1
        
        if max < 0: return False

        if min < 0: min = 0
        
    
    return min == 0 

if __name__ == "__main__":
    s = input()
    print(solve(s))
    
    # ()*)*()
    # (**(