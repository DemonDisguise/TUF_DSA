# Recursive Insertion Sort

def insertion_sort(arr, n):

    if n <= 1:
        return

    insertion_sort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    insertion_sort(arr, len(arr))

    print(arr)