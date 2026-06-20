# Merge sort

def merge(arr: list[int], low: int, mid: int, high: int) -> None:
    temp = []
    i = low
    j = mid + 1
    
    while i <= mid or j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
        
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= high:
        temp.append(arr[j])
        j += 1
    
    for i in range(high - low + 1):
        arr[low + i] = temp[i] 

def _merge_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        mid: int = (low + high) // 2
        
        _merge_sort(arr, low, mid)
        _merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge_sort(arr: list[int]) -> None:
    if len(arr) <= 1:
        return
    _merge_sort(arr, 0, len(arr) - 1)

arr: list[int] = list(map(int, input().split()))
merge_sort(arr)
print(arr)