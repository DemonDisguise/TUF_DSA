# Merge Intervals
""" Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. """

from typing import List
import sys

def solve(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []
    
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
        
    return res       

if __name__ == "__main__":
    intervals = []
    for line in sys.stdin:
        intervals.append(list(map(int, line.strip().split())))
    res = solve(intervals)
    for i in res:
        print(*i)
    