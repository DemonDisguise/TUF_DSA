# Find missing number

def solve(arr):
    n = len(arr)
    
    for i in range(1, n + 1):
        found = False
        if i in arr:
            found = True
        
        if not found:
            return i
    
    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
