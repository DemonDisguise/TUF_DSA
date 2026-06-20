# Count Good Numbers
# A digit string is considered good if:
# the digits at even indices are even
# the digits at odd indices are prime
# return ans modulo 10 ** 9 + 7

mod = 10 ** 9 + 7

def solve(ind, n):
    if ind == n:
        return 1

    res = 0
    if ind % 2 == 0:
        # even nums - 5
        for i in range(5):
            res = (res + solve(ind + 1, n)) % mod
    else:
        # prime nums - 4
        for i in range(4):
            res = (res + solve(ind + 1, n)) % mod 
    
    return res


if __name__ == "__main__":
    n = int(input())
    print(solve(0, n))
    