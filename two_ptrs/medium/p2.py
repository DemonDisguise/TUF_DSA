# Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Trick: Find the longest subarray with atmost k zeros

def solve(nums, k):
    ans = 0
    l = 0
    zeros = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        
        ans = max(ans, r - l + 1)
    
    return ans

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))
    
    # 1 1 1 0 0 0 1 1 1 1 0
    # 2