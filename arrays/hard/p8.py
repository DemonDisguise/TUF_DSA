# Merge two sorted arrays without extra space

def solve(arr1, m, arr2, n):

    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:

        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1

        k -= 1

    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

    return arr1


if __name__ == "__main__":

    m, n = map(int, input().split())

    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    print(*solve(nums1, m, nums2, n))