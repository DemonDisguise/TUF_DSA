# Find median from data stream
"""
Problem Statement: Find Median from Data Stream

Implement a class that finds the median from a data stream. 

The median is the middle value in an ordered integer list. If the size of the 
list is even, there is no middle value, and the median is the mean of the two 
middle values.

Implement the MedianFinder class:
    * __init__() -> Initializes the MedianFinder object.
    * add_num(num: int) -> Void. Adds the integer 'num' from the data stream 
      to the data structure.
    * find_median() -> Float. Returns the median of all elements so far. 
    Answers within 10-5 of the actual answer will be accepted.
"""

import heapq

class MedianFinder:
    """
    A data structure to find the median of a continuous stream of integers.
    
    This implementation uses two heaps (a max-heap and a min-heap) to keep 
    track of the data stream efficiently. 
    - 'max_heap' stores the smaller half of the numbers.
    - 'min_heap' stores the larger half of the numbers.
    """

    def __init__(self):
        """
        Initializes the MedianFinder object.
        """
        self.max_heap = []
        self.min_heap = []

    def add_num(self, num: int) -> None:
        """
        Adds the integer 'num' from the data stream to the data structure.
        
        Args:
            num (int): The integer to be added.
        """
        heapq.heappush_max(self.max_heap, num)
        heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        """
        Returns the median of all elements added so far.
        
        Returns:
            float: The median value.
        """
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] + self.min_heap[0]) / 2.0
        return float(self.max_heap[0])

if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())
    mf.add_num(3)
    print(mf.find_median())
    