# Check if an array represents a min heap

def solve(arr):
    n = len(arr)
    
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] > arr[left]:
            return False
        
        if right < n and arr[i] > arr[right]:
            return False
    
    return True
        
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    
    # 10 20 30 21 23