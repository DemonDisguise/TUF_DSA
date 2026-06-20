# Maximum nesting depth of parenthesis

def solve(s):
    dpth = 0
    mx_dpth = 0
    
    for i in s:
        if i == "(":
            dpth += 1
            mx_dpth = max(dpth, mx_dpth)
        elif i == ")":
            dpth -= 1
    
    return mx_dpth

if __name__ == "__main__":
    s = input()
    print(solve(s))
    