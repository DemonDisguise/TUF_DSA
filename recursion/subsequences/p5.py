# Check if there exists a subsequence with sum K

def helper(ind, sm, nums):
    if sm == 0:
        return True
    
    if sm < 0 or len(nums) == ind:
        return False
    
    return helper(ind + 1, sm, nums) or helper(ind + 1, sm - nums[ind], nums)

def solve(nums, k):
    return helper(0, k, nums)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))
    