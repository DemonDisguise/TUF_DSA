# Minimum number of platforms required for a railway
""" We are given one array that represent the arrival and departure times of trains that stop at the platform.
We need to find the minimum number of platforms needed at the railway station so that no train has to wait.
for 9:00 write it as 900, 12:30 as 1230
"""


def solve(arrivals: list[int], departures: list[int]) -> int:
    arrivals.sort()
    departures.sort()     

    i = j = 0
    platforms = max_platforms = 0
    n = len(arrivals)
    
    while i < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    return max_platforms

if __name__ == "__main__":
    arrivals = list(map(int, input().split()))
    departures = list(map(int, input().split()))
    print(solve(arrivals, departures))

# 900 920
# 945 1200
# 955 1130
# 1100 1150
# 1500 1900
# 1800 2000    