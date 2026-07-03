# Candy
"""  A line of N kids is standing there. The rating values listed in the integer array ratings are assigned to each kid. These kids are receiving candy according to the following criteria:

There must be at least one candy for every child.
Kids whose scores are higher than their neighbours receive more candies than their neighbours.
Return the minimum number of candies needed to distribute among children. """


def solve(ratings: list[int]) -> int:
    n = len(ratings)
    total_sum = 1
    i = 1
    
    while i < n:
        if ratings[i] == ratings[i - 1]:
            total_sum += 1
            i += 1
            continue
        peak = 1
        while (i < n and ratings[i] > ratings[i - 1]):
            peak += 1
            total_sum += peak
            i += 1
        down = 1
        while (i < n and ratings[i] < ratings[i - 1]):
            total_sum += down
            i += 1
            down += 1
        if down > peak:
            total_sum += down - peak
        
    return total_sum
        
if __name__ == "__main__":
    ratings = list(map(int, input().split()))
    print(solve(ratings))
    