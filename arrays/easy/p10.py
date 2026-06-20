# Maximum Consecutive Ones

def solve(arr):
    n = len(arr)
    count = 0
    mx_count = 0
    
    for i in range(n):
        if arr[i] == 1:
            count += 1
            mx_count = max(count, mx_count)
        else:
            count = 0
    return mx_count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))