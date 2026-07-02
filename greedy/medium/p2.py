# Jump Game 1
""" Given an array where each element represents the maximum number of steps you can jump forward from that element, return true if we can reach the last index starting from the first index. Otherwise, return false. """

from typing import List

def solve(arr: List[int]) -> bool:
    max_reach = 0
    
    for ind, num in enumerate(arr):
        if max_reach >= ind:
            max_reach = max(max_reach, num + ind)
        else:
            return False
    
    return True

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    
    # 1 2 4 1 1 0 2 5