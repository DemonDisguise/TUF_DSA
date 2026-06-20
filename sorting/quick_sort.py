# Quick sort

def partition(arr, low, high):
    pivot = arr[low]          
    i = low + 1
    j = high

    while True:

        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low + 1 and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    quicksort(arr, 0, len(arr) - 1)

    print(arr)