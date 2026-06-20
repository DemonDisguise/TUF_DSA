# Linear search

def solve(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(solve(arr, 3))