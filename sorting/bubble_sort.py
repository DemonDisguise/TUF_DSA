# Bubble sort

def bub_sort(arr: list[int]) -> None:
    n: int = len(arr)
    for i in range(n - 1, -1, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break

arr: list[int] = list(map(int, input().split()))
bub_sort(arr)
print(arr)