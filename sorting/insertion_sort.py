# Insertion sort

def in_sort(arr: list[int]) -> None:
    n: int = len(arr)
    for i in range(1, n):
        key: int = arr[i]
        j: int = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

arr: list[int] = list(map(int, input().split())) 
in_sort(arr)
print(arr)