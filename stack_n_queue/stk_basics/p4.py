# Balanced Paranthesis

def solve(s):
    stk = []

    close = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for ch in s:
        if ch in close:
            stk.append(close[ch])

        elif not stk or stk.pop() != ch:
            return False

    return not stk

if __name__ == "__main__":
    s = input()
    print(solve(s))