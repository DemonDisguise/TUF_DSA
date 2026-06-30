# Convert Min heap to Max heap

def max_heapify(arr, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest == i:
            break
        
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def min_heap_to_max_heap(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
        print(arr)
        
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(arr)
    print(min_heap_to_max_heap(arr))
    
    # 10 20 30 21 23