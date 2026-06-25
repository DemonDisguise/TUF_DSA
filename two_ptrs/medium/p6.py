# Count number of nice subarrays
""" Given an array nums and an integer k. An array is called nice if and only if it contains k odd numbers.
Find the number of nice subarrays in the given array nums. A subarray is continuous part of the array. """

def solve(arr, k):
    def at_most(arr, k):
        if k < 0: return 0
        
        l = odds = cnt = 0
        
        for r in range(len(arr)):
            odds += arr[r] & 1
            
            while odds > k:
                odds -= arr[l] & 1
                l += 1
            
            cnt += r - l + 1
        
        return cnt

    return at_most(arr, k) - at_most(arr, k - 1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
    
    # 1 1 2 1 1 
    # 3