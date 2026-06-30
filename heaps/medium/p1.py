# K-th largest element in an array

""" import heapq

def solve(arr, k):
    if k > len(arr) or k <= 0:
        return -1
    x = arr
    heapq.heapify_max(x)
    for _ in range(k - 1):
        heapq.heappop_max(x)
    return heapq.heappop_max(x) """

# QuickSelect version
import random

def partition(nums, left, right, pivot):
    nums[left], nums[pivot] = nums[pivot], nums[left]
    pivot_value = nums[left]

    store = left + 1

    for i in range(left + 1, right + 1):
        if nums[i] > pivot_value:
            nums[store], nums[i] = nums[i], nums[store]
            store += 1

    nums[left], nums[store - 1] = nums[store - 1], nums[left]
    return store - 1


def solve(nums, k):
    if k > len(nums) or k <= 0:
        return -1

    left, right = 0, len(nums) - 1
    target = k - 1

    while left <= right:
        pivot = random.randint(left, right)
        pivot = partition(nums, left, right, pivot)

        if pivot == target:
            return nums[pivot]

        if pivot < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
    
    # -5 4 1 2 -3
    # -5