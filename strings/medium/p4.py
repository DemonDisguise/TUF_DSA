# String to Integer (atoi)

INT_MIN = -2**31
INT_MAX = 2**31 - 1

def helper(s, i, num, sign):
    if i >= len(s) or not s[i].isdigit():
        return sign * num

    num = num * 10 + int(s[i])

    if sign * num <= INT_MIN: return INT_MIN
    if sign * num >= INT_MAX: return INT_MAX
    
    return helper(s, i + 1, num, sign)

def solve(s: str) -> int:
    i = 0
    
    while i < len(s) and s[i] == " ":
        i += 1
    
    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    
    return helper(s, i, 0, sign)

if __name__ == "__main__":
    s = input()
    print(solve(s))
    