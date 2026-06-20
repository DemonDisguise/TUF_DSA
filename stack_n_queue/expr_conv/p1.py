# Infix to Postfix

def prio(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def solve(s):
    stk = []
    ans = []
    for ch in s:
        if ch.isalnum():
            ans.append(ch)
        elif ch == '(':
            stk.append('(')
        elif ch == ')':
            while stk and stk[-1] != '(':
                ans.append(stk.pop())
            stk.pop()
        else:
            while stk and prio(ch) <= prio(stk[-1]):
                ans.append(stk.pop())
            stk.append(ch)
    
    while stk:
        ans.append(stk.pop())
    
    return ''.join(ans)

if __name__ == "__main__":
    s = input()
    print(solve(s))
    