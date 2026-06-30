# Sort K sorted array

# Given an array arr[] and a number k . The array is sorted in a way that every element is at max k distance away from it sorted position. It means if we completely sort the array, then the index of the element can go from i - k to i + k where i is index in the given array. Our task is to completely sort the array.

import heapq

def solve(arr, k):
    if not arr:
        return []

    k = min(k, len(arr) - 1)

    heap = arr[:k + 1]
    heapq.heapify(heap)

    res = []

    for num in arr[k + 1:]:
        res.append(heapq.heappushpop(heap, num))

    while heap:
        res.append(heapq.heappop(heap))

    return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(*solve(arr, k))

# 6 5 3 2 8 10 9
# 3