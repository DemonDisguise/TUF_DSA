# Count subarrays with given xor k

def solve(arr, k):
    xor = 0
    cnt = 0
    
    freq = {0: 1}
    
    for i in arr:
        xor ^= i
        
        target = xor ^ k
        
        if target in freq:
            cnt += freq[target]
        
        freq[xor] = freq.get(xor, 0) + 1
    
    return cnt               

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))