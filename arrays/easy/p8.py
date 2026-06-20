# Union of two sorted arrays

def solve(arr1, arr2):
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    res = []
    last = None   

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if arr1[i] != last:
                res.append(arr1[i])
                last = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != last:
                res.append(arr2[j])
                last = arr2[j]
            j += 1
        else:
            if arr1[i] != last:
                res.append(arr1[i])
                last = arr1[i]
            i += 1
            j += 1

    while i < n:
        if arr1[i] != last:
            res.append(arr1[i])
            last = arr1[i]
        i += 1

    while j < m:
        if arr2[j] != last:
            res.append(arr2[j])
            last = arr2[j]
        j += 1

    return res

if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = solve(arr1, arr2)
    print(*res)
