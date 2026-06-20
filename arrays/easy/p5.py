# Left or Right rotate the array by k times

def solve(arr, k, dir):
    n = len(arr)
    k = k % n
    
    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    if dir == "l":
        reverse(0, k - 1)
        reverse(k, n - 1)
        reverse(0, n - 1)
    else:
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    solve(arr, k, 'l')
    print(*arr)