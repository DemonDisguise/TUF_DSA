# Insert Interval
""" You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it. """

from typing import List
import sys

def solve(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    n = len(intervals)
    res = []
    i = 0
    
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    
    res.append(new_interval)
    
    while i < n:
        res.append(intervals[i])
        i += 1
    
    return res

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    intervals = []
    
    for line in lines[:-1]:
        intervals.append(list(map(int, line.strip().split())))
    
    new_interval = list(map(int, lines[-1].strip().split()))

    res = solve(intervals, new_interval)
        
    for i in res:
        print(*i)

# 1 2
# 3 5
# 6 7
# 8 10
# 12 16
# 4 8