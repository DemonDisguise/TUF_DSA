# Check if a number is power of 2 or not

def solve(n):
    return n > 0 and n & (n - 1) == 0

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
    