# Two sum: Check if a pair with given sum exists in array

def solve(arr, target):
    n = len(arr)
    hshmp = {}

    for i in range(n):
        if target - arr[i] in hshmp:
            return [hshmp[target - arr[i]], i]
            break
        else:
            hshmp[arr[i]] = i
    
    return [-1, -1] 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(*solve(arr, target))
    