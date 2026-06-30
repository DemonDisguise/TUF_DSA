# Hands of Straights
""" You are given an array of integers hand, where hand[i] is the value on the i-th card that Alice owns. Alice wants to split her entire hand into groups such that: every group contains exactly groupSize cards, and the card values in each group form a sequence of groupSize consecutive integers (e.g. [3, 4, 5], [10, 11, 12, 13]). """

from typing import List
import heapq
from collections import Counter

def solve(hand: List[int], n: int) -> bool:
    if len(hand) % n != 0:
        return False
    
    freq = Counter(hand)
    min_heap = list(freq.keys())
    heapq.heapify(min_heap)

    while min_heap:
        first = min_heap[0]

        if freq[first] == 0:
            heapq.heappop(min_heap)
            continue
        
        for i in range(n):
            card = first + i
            if freq[card] == 0:
                return False
            freq[card] -= 1
        
        if freq[first] == 0:
            heapq.heappop(min_heap)
    
    return True

if __name__ == "__main__":
    hand = list(map(int, input().split()))
    n = int(input())
    print(solve(hand, n))
    