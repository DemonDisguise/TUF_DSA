# Largest element

def solve(arr):
    n = len(arr)
    largest = arr[0]
    
    for i in range(1, n):
        if largest < arr[i]:
            largest = arr[i]
        
    return largest 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))