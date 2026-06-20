# Check if the i-th bit is set or not

def solve1(num, ind):
    if (num & (1 << ind)):
        return True
    return False

def solve2(num, ind):
    if ((num >> ind) & 1):
        return True
    return False

if __name__ == "__main__":
    n, i = map(int, input().split())
    print(solve1(n, i))
    print(solve2(n, i))
    