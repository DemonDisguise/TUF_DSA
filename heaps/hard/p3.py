# Kth largest element in a stream of running integers
"""
Problem: Kth Largest Element in a Stream

Design a class `KthLargest` that maintains the kth largest element in a stream of integers.

Implement the following methods:

1. `__init__(self, k: int, nums: list[int])`
   - Initializes the object with the integer `k` and the initial list of numbers `nums`.

2. `add(self, val: int) -> int`
   - Adds the integer `val` to the stream.
   - Returns the kth largest element in the current stream after the insertion.

Note:
- The kth largest element is determined based on the sorted order of all elements in the stream.
- It is **not** the kth distinct largest element; duplicate values are counted separately.
"""

import heapq

class KthLargest:
    """
    Maintains the kth largest element in a stream of integers.

    Methods:
        __init__(k, nums):
            Initializes the object with the integer k and the initial
            list of numbers.

        add(val):
            Adds val to the stream and returns the kth largest
            element in the current stream.
    """

    def __init__(self, k: int, nums: list[int]):
        """
        Initialize the KthLargest object.

        Args:
            k (int):
                The position of the largest element to maintain.
            nums (list[int]):
                The initial stream of integers.
        """
        self.k = k
        self.heap = nums[:]
        
        heapq.heapify(self.heap)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Add a new value to the stream.

        Args:
            val (int):
                The value to be added to the stream.

        Returns:
            int:
                The kth largest element after the insertion.
        """
        if len(self.heap) > self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]

if __name__ == "__main__":
   kth = KthLargest(3, [4, 5, 6, 8, 2])
   
   print(kth.add(3))
   print(kth.add(5))
   print(kth.add(10))
   print(kth.add(9))
   print(kth.add(4))