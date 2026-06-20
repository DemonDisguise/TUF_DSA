# Search element in rotated sorted array II - duplicates

def solve(arr, k):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) >> 1

        if arr[mid] == k:
            return True

        if arr[l] == arr[mid] == arr[r]:
            l += 1
            r -= 1
            continue

        if arr[l] <= arr[mid]:

            if arr[l] <= k <= arr[mid]:
                r = mid - 1
            else:
                l = mid + 1

        else:

            if arr[mid] <= k <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1

    return False


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(solve(arr, k))