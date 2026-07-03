# N meetings in one room
"""  There is one meeting room in a firm. You are given two arrays, start and end each of size N. For an index ‘i’, start[i] denotes the starting time of the ith meeting while end[i] will denote the ending time of the ith meeting. 
 Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a particular time. 
 Print the order in which these meetings will be performed. """

import sys

def solve(meetings: list[tuple[int]]) -> list[int]:
    ind_meetings = [(start, end, ind) for ind, (start, end) in enumerate(meetings, start=1)]
    meetings = [(start, end, ind) for ind, (start, end) in enumerate(meetings, start=1)]
    ind_meetings.sort(key=lambda x: x[1])
    res = []
    curr_end = -1
    
    for (start, end, ind) in ind_meetings:
        if start > curr_end:
            res.append(ind)
            curr_end = end
    
    return res

if __name__ == "__main__":
    meetings = []
    for line in sys.stdin:
        line = line.strip()
        if not line: break
        meetings.append(tuple(map(int, line.split())))
    print(*solve(meetings))
    print(meetings)
        