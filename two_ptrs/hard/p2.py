# Subarrays with k different integers
""" You are given an integer array nums and an integer k. Return the number of good subarrays of nums.

A good subarray is defined as a contiguous subarray of nums that contains exactly k distinct integers. A subarray is a contiguous part of the array. """

def solve(nums, k):
    def at_most(nums, k):
        if k < 0: return 0
        
        mp = {}
        l = cnt = 0
        
        for r, num in enumerate(nums):
            mp[num] = mp.get(num, 0) + 1
    
            while len(mp) > k:
                left = nums[l]
                mp[left] -= 1
                if mp[left] == 0: del mp[left]
                l += 1
            
            cnt += r - l + 1
        
        return cnt
    
    return at_most(nums, k) - at_most(nums, k - 1)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(solve(nums, k))

    # 1 2 1 2 3
    # 2