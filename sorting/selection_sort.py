# Selection sort

def sel_sort(arr: list[int]) -> None:
    n: int = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i, n):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

arr: list[int] = list(map(int, input().split()))
sel_sort(arr)
print(arr)