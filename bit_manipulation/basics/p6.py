# Swap two numbers

def solve(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(*solve(a, b))
    