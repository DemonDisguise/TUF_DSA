# Roman numerals to integer
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# Roman numerals are usually written large -> small (l -> r)
# But in siz special cases, subtraction is used instead of addition:
# I before V or X 
# X before L or C
# C before D or M

def solve(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    res = 0
    
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    
    return res + roman[s[-1]]
 
if __name__ == "__main__":
    s = input()
    print(solve(s))