# Task scheduler with variable cooldown

from collections import Counter, deque
from typing import Dict, List
import heapq


def solve(tasks: List[str], cooldown: Dict[str, int]) -> int:
    freq = Counter(tasks)

    max_heap = [(count, task) for task, count in freq.items()]
    heapq.heapify_max(max_heap)

    wait = deque()

    time = 0

    while max_heap or wait:
        time += 1

        if max_heap:
            count, task = heapq.heappop_max(max_heap)
            count -= 1

            if count:
                available_time = time + cooldown[task]
                wait.append((available_time, count, task))

        while wait and wait[0][0] == time:
            _, count, task = wait.popleft()
            heapq.heappush_max(max_heap, (count, task))

    return time


if __name__ == "__main__":
    tasks = [
        "A", "A",
        "B", "B",
        "C", "C"
    ]

    cooldown = {
        "A": 2,
        "B": 1,
        "C": 3
    }

    print(solve(tasks, cooldown))