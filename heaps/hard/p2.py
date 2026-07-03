# Minimum cost to connect sticks
""" You are given an array sticks, where sticks[i] represents the length of the i-th stick. You can connect any two sticks into one stick.
The cost of connecting two sticks is equal to the sum of their lengths. After connecting, the new stick has length equal to that sum. Return the minimum total cost to connect all sticks into one. """

import heapq

def solve(arr: list[int]) -> int:
    if len(arr) <= 1:
        return 0
    
    min_heap = arr.copy()
    heapq.heapify(min_heap)
    cost = 0
    
    while len(min_heap) > 1:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(min_heap)
        total = a + b
        cost += total
        heapq.heappush(min_heap, total)
    return cost

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    