# Power set | Bit manipulation

def solve(arr):
    n = len(arr)
    res = []
    
    for i in range(1 << n):
        curr = []
        for j in range(n):
            if i & (1 << j):
                curr.append(arr[j])
        res.append(curr)

    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solve(arr)
    for i in res:
        print(*i)
        