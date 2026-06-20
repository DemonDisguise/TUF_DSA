# 4 Sum | Find Quads that add up to a target value

def solve(arr, target):
    n = len(arr)
    quads = []

    arr.sort()

    for i in range(n - 3):

        if i > 0 and arr[i] == arr[i - 1]:
            continue

        if arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] > target:
            break

        if arr[i] + arr[n - 1] + arr[n - 2] + arr[n - 3] < target:
            continue

        for j in range(i + 1, n - 2):

            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            if arr[i] + arr[j] + arr[j + 1] + arr[j + 2] > target:
                break

            if arr[i] + arr[j] + arr[n - 1] + arr[n - 2] < target:
                continue

            k = j + 1
            l = n - 1

            while k < l:

                total = arr[i] + arr[j] + arr[k] + arr[l]

                if total == target:

                    quads.append([arr[i], arr[j], arr[k], arr[l]])

                    k += 1
                    l -= 1

                    while k < l and arr[k] == arr[k - 1]:
                        k += 1

                    while k < l and arr[l] == arr[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1

                else:
                    l -= 1

    return quads


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    res = solve(arr, target)

    for quad in res:
        print(*quad)