# Top K frequent elements
""" Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. """

from typing import List
import heapq
from collections import Counter

def solve(arr: List[int], k: int) -> List[int]:
    freq = Counter(arr)
    
    min_heap = []
    
    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    min_heap.sort(reverse=True)
    res = [num for _, num in min_heap]
    return res

""" 
def solve(arr: List[int], k: int) -> List[int]:
    freq = Counter(arr)
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x:x[1])]
"""
    
# Optimal - O(n)
""" 
def solve(arr: List[int], k: int) -> List[int]:
    freq = Counter(arr)
    n = len(arr)
    
    buckets = [[] for _ in range(n + 1)]
    
    for num, count in freq.items():
        buckets[count].append(num)
    
    res = []
    for i in range(n, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res
    
    return res 
"""

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(*solve(arr, k))

# 1 1 1 2 2 3
# 2    