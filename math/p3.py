# Power exponentiation

def solve(x, n):
    negative = n < 0
    n = abs(n)

    ans = 1.0

    while n:
        if n & 1:
            ans *= x

        x *= x
        n >>= 1

    return 1 / ans if negative else ans


if __name__ == "__main__":
    x, n = input().split()
    x = float(x)
    n = int(n)

    print(solve(x, n))