# Sliding Window Maximum 
# Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window..

from collections import deque

def solve(arr, k):
    if k == 1:
        return arr

    q = deque()
    res = []
    
    for i, x in enumerate(arr):
        left = i - k + 1
        
        if q and q[0] < left:
            q.popleft()
        
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        
        q.append(i)
        
        if left >= 0: res.append(arr[q[0]])
    
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(*solve(arr, k))
    
    # 4 0 -1 3 5 3 6 8
    # 3  