# K-th element of two sorted arrays

def solve(arr1, arr2, k):
    m = len(arr1)
    n = len(arr2)
    
    if n < m: return solve(arr2, arr1, k)
    
    left = k
    
    l, r = max(0, k - n), min(k, m)
    
    while l <= r:
        mid1 = (l + r) >> 1
        mid2 = left - mid1
        
        l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
        l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
        r1 = arr1[mid1] if mid1 < m else float('inf')
        r2 = arr2[mid2] if mid2 < n else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            r = mid1 - 1
        else:
            l = mid1 + 1
    
    return -1

if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    k = int(input())
    print(solve(arr1, arr2, k))
    