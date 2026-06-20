# Find number that appears once, and the other numbers twice

def solve(arr):
    res = 0
    for i in arr:
        res ^= i
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

# 4 1 2 1 2 => 4  