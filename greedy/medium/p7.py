# Shortest Job First CPU Scheduling
""" Given a list of job durations representing the time it takes to complete each job. Implement the Shortest Job First algorithm to find the average waiting time for these jobs.
 selects the waiting process with the smallest execution (burst) time to execute next. It is primarily used to minimize the average waiting time and turnaround time for a batch of processes """

from typing import List

def solve(jobs: List[int]) -> int:
    jobs.sort()
    
    total_time = 0
    waiting_time = 0
    n = len(jobs)
    
    for job in jobs:
        waiting_time += total_time
        total_time += job
    
    return waiting_time // n

if __name__ == "__main__":
    jobs = list(map(int, input().split()))
    print(solve(jobs))

# 3 1 4 2 5