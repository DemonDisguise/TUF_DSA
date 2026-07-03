# Jump game 2
""" You are given a 0-indexed array nums of length n representing your maximum jump capability from each index.

You start at index 0. Each element nums[i] represents the maximum number of steps you can jump forward from index i.
Your goal is to reach the last index of the array (nums[n - 1]) using the minimum number of jumps
Return the minimum number of jumps required to reach the last index.
You can assume that it is always possible to reach the last index. """


def solve(arr: list[int]) -> int:
    l = r = 0
    n = len(arr)
    jumps = 0
    
    while r < n - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(i + arr[i], farthest)     
        l = r + 1
        r = farthest
        jumps += 1
    
    return jumps

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    
    # 2 3 1 4 1 1 1 2