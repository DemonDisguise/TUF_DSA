# Printing subsequences whose sum is k

def helper(ind, sm, nums):
    if sm == 0:
        return 1
    
    if sm < 0 or ind == len(nums):
        return 0
    
    return helper(ind + 1, sm - nums[ind], nums) + helper(ind + 1, sm, nums)        

def solve(nums, k):
    return helper(0, k, nums)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))
    