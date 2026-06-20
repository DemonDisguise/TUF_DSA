# Infix to prefix

def solve(s):
    vals = []
    ops = []
    
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for ch in s:
        if ch.isalnum():
            vals.append(ch)
        
        elif ch == '(':
            ops.append(ch)
        
        elif ch == ')':
            while ops[-1] != '(':
                op = ops.pop()
                right = vals.pop()
                left = vals.pop()
                vals.append(op + left + right)            
            ops.pop()        
        else:
            while (ops and ops[-1] != '(' and (prec[ops[-1]] > prec[ch] or (prec[ops[-1]] == prec[ch] and ch != '^'))):
                op = ops.pop()
                right = vals.pop()
                left = vals.pop()
                vals.append(op + left + right)            
            ops.append(ch)
    
    while ops:
        op = ops.pop()
        right = vals.pop()
        left = vals.pop()
        vals.append(op + left + right)
    
    return vals[-1]

if __name__ == "__main__":
    s = input()
    print(solve(s))

# a+b*(c^d-e)^(f+g*h)-i

