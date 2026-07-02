# Non-overlapping intervals
# Given an array of N intervals in the form of (start[i], end[i]), where start[i] is the starting point of the interval and end[i] is the ending point of the interval, return the minimum number of intervals that need to be removed to make the remaining intervals non-overlapping.

from typing import List
import sys

def solve(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    removed = 0

    for start, finish in intervals[1:]:
        if start < end:
            removed += 1
        else:
            end = finish
    
    return removed

if __name__ == "__main__":
    intervals = []
    for line in sys.stdin:
        intervals.append(list(map(int, line.strip().split())))
    print(solve(intervals))
# 1 2
# 2 3
# 3 4
# 1 3