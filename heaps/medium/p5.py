# Replace elements by its rank in the array

from typing import List
import heapq

# This is the optimal solution but can be solved using heaps as well
""" def solve(arr: List[int]) -> List[int]:
    sorted_unique = sorted(set(arr))
    rank = {num: i + 1 for i, num in enumerate(sorted_unique)}
    return [rank[x] for x in arr]
 """

# Heap solution
def solve(arr: List[int]) -> List[int]:
    if not arr:
        return []
    
    heap = []
    
    for num in arr:
        heapq.heappush(heap, num)
        
    rank = {}
    curr_rank = 1
    
    while heap:
        num = heapq.heappop(heap)
        
        if num not in rank:
            rank[num] = curr_rank
            curr_rank += 1
    
    return [rank[num] for num in arr]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    
    # 20 15 26 2 98 6