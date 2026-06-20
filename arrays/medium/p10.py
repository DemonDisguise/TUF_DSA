# Longest consecutive sequence in an array

def solve(arr):
    n = len(arr)
    
    lngst = 1
    st = set(arr)
    
    for i in st:
        if i - 1 not in st:
            cnt = 1
            x = i
            
            while x + 1 in st:
                x += 1
                cnt += 1
            
            lngst = max(lngst, cnt)
            
    return lngst

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    