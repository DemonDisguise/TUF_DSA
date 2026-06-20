# Check if array is sorted 
def solve(arr):
    n = len(arr)
    return all(arr[i] < arr[i + 1] for i in range(0, n - 1))

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))