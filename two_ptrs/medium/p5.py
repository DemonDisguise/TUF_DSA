# Binary subarray with sum
"""  You are given a binary array nums (containing only 0s and 1s) and an integer goal. Return the number of non-empty subarrays of nums that sum to goal. 
 A subarray is a contiguous part of the array. """

def at_most(arr, goal):
    if goal < 0:
        return 0
    
    cnt = 0
    sm = 0
    l = 0
    
    for r in range(len(arr)):
        sm += arr[r]
        
        while sm > goal:
            sm -= arr[l]
            l += 1
        
        cnt += r - l + 1
    
    return cnt

def solve(arr, goal):
    return at_most(arr, goal) - at_most(arr, goal - 1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    goal = int(input())
    print(solve(arr, goal))
    
    # 1 0 0 1 1 0
    # 2