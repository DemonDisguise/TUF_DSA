# Remove Outermost parentheses
# Valid Parenthesis if 
# - it is empty string
# - if A is a valid parentheses string, then so is "(" + A + ")"
# - If A and B are valid parentheses strings, then A + B is also valid

def solve(s):
    result = ""
    
    level = 0
    
    for ch in s:
        if ch == '(':
            if level > 0:
                result += ch
            level += 1
        elif ch == ')':
            level -= 1
            if level > 0:
                result += ch
    
    return result

if __name__ == "__main__":
    s = input()
    print(solve(s))
