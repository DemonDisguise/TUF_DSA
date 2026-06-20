# 3 Sum: Find triplets that add up to a zero

def solve(arr):
    n = len(arr)
    trplts = []           

    arr.sort()
    
    for i in range(n):
        if (i > 0 and arr[i] == arr[i - 1]):
            continue
        j = i + 1
        k = n - 1
        
        while j < k:
            sm = arr[i] + arr[j] + arr[k]
            
            if sm < 0:
               j += 1 
            elif sm > 0:
                k -= 1
            else:
                trplts.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]: j += 1
                while j < k and arr[k] == arr[k + 1]: k -= 1
        
    return trplts       
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solve(arr)
    for i in res:
        print(*i)
    