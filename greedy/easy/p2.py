# Fractional Knapsack
""" The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.

Note: We can either take the item as a whole or break it into smaller units. """

from typing import List
import sys

def solve(items: List[tuple[int, int]], capacity: int) -> float:
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    curr_cap = 0
    profit = 0
    
    for val, wt in items:
        if curr_cap + wt <= capacity:
            curr_cap += wt
            profit += val
        else:
            remaining = capacity - curr_cap
            profit += val * (remaining / wt)
            break
    
    return profit

if __name__ == "__main__":
    input = sys.stdin
    
    items = []
    
    for line in input:
        s = line.strip().split()
        if len(s) > 1:
            items.append((int(s[0]), int(s[1])))
        else:
            capacity = int(s[0])
            break
    
    print(solve(items, capacity))
    