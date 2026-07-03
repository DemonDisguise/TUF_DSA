# Job Sequencing Problem
""" You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. 
Find the number of jobs done and the maximum profit that can be obtained. 
Each job takes a single unit of time and only one job can be performed at a time """

import sys

def solve(jobs: list[tuple[int]]) -> tuple[int]:
    max_deadline = max(job[1] for job in jobs)
    
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    slots = [0] * (max_deadline + 1)
    
    total_profit = 0
    scheduled_jobs = 0
    
    for job_id, deadline, profit in jobs:
        for slot in range(deadline, 0, -1):
            if slots[slot] == 0:
                slots[slot] = job_id
                total_profit += profit
                scheduled_jobs += 1
                break
    
    return (scheduled_jobs, total_profit)

if __name__ == "__main__":
    jobs = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        jobs.append(tuple(map(int, line.split())))
    print(*solve(jobs))
 
# 1 4 20
# 2 1 10
# 3 1 40
# 4 1 30   