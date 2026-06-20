# Median of 2 sorted arrays

def solve(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    
    if (n < m): return solve(arr2, arr1)

    l, r = 0, m
    
    while l <= r:
        cut1 = (l + r) >> 1
        cut2 = (m + n + 1) // 2 - cut1
        
        l1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
        l2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]

        r1 = float("inf") if cut1 == m else arr1[cut1]
        r2 = float("inf") if cut2 == n else arr2[cut2]
        
        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return float(max(l1, l2))
        elif l1 > r2:
            r = cut1 - 1
        else:
            l = cut1 + 1
    
    return 0.0
    
if __name__ == "__main__": 
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(solve(arr1, arr2))
    