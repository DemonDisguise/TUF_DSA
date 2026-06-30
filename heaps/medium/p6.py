# Task scheduler
"""  You are given a list of tasks represented by uppercase English letters ('A' to 'Z'), and an integer n representing a cooldown interval between two same tasks. Each task takes exactly 1 CPU interval to complete. Tasks can be executed in any order, but identical tasks must be separated by at least n intervals, during which the CPU may remain idle or execute other tasks.
Return the minimum number of CPU intervals required to complete all the tasks . """

from typing import List
import heapq
from collections import Counter

def solve(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)
    
    max_heap = [count for count in freq.values()]  
    heapq.heapify_max(max_heap) 
    
    time = 0
    
    while max_heap:
        temp = []
        cycle = n + 1
        used = 0
        
        while used < cycle and max_heap:
            count = heapq.heappop_max(max_heap) - 1
            
            if count > 0:
                temp.append(count)
            
            time += 1
            used += 1
            
        for count in temp:
            heapq.heappush_max(max_heap, count)
        
        if max_heap:
            time += cycle - used
    
    return time

if __name__ == "__main__":
    tasks = input().split()
    n = int(input())
    print(solve(tasks, n))
    # A A A B B B
    # 2