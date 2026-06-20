# Check if the number is odd or not

def solve(n):
    if n & 1:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())
    print(solve(n))