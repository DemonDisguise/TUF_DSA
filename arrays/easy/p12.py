# Longest subarray with given sum K(positives)

def solve(arr, k):
    n = len(arr)
    mx = 0
    curr_sum = arr[0]
    
    left = 0
    right = 0
    
    while right < n:
        while left <= right and curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        
        if curr_sum == k:
            mx = max(mx, right - left + 1)
        
        right += 1
        
        if right < n:
            curr_sum += arr[right]
    
    return mx

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))        