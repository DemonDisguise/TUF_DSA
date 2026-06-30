# Maximum Sum Combination
""" Given two integer arrays nums1 and nums2 and an integer k, return the maximum k valid sum combinations from all possible sum combinations using the elements of nums1 and nums2. A valid sum combination is made by adding one element from nums1 and one element from nums2. Return the answer in non-increasing order. """

from typing import List
import heapq

def solve(arr1: List[int], arr2: List[int], k: int) -> List[int]:
    n = len(arr1)
    m = len(arr2)
    
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    
    max_heap = [((arr1[0] + arr2[0]), 0, 0)]
    visited = {(0, 0)}
    
    ans = []
    
    while max_heap and len(ans) < k:
        total, i, j = heapq.heappop_max(max_heap)
        ans.append(total)
        
        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush_max(max_heap, ((arr1[i + 1] + arr2[j]), i + 1, j))
            visited.add((i + 1, j))
        
        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush_max(max_heap, ((arr1[i] + arr2[j + 1]), i, j + 1))
            visited.add((i, j + 1))
    
    return ans

if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    k = int(input())
    print(*solve(arr1, arr2, k))

# 7 3
# 1 6
# 2   