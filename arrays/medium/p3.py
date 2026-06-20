# Find the majority element that occurs more than N/2 times

def solve(arr):
    n = len(arr)
    
    cnt = 0
    mjr = None
    
    for i in arr:
        if i == mjr:
            cnt += 1
        elif i != mjr and cnt == 0:
            mjr = i
            cnt += 1
        else:
            cnt -= 1
    
    cnt = 0
    for i in arr:
        if i == mjr:
            cnt += 1
    
    if cnt > n // 2:
        return mjr

    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    