# Count reverse pairs
# i < j and arr[i] > 2 * arr[j]

def solve(arr):
    n = len(arr)
    def merge(arr, l, mid, r):
        tmp = []
        left = l
        right = mid + 1
        
        while left <= mid and right <= r:
            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                right += 1
        
        while left <= mid:
            tmp.append(arr[left])
            left += 1
        
        while right <= r:
            tmp.append(arr[right])
            right += 1
        
        for i in range(l, r + 1):
            arr[i] = tmp[i - l]
    
    def cntPairs(arr, l, mid, r):
        cnt = 0
        right = mid + 1
        for i in range(l, mid + 1):
            while right <= r and arr[i] > 2 * arr[right]: right += 1
            cnt += right - (mid + 1)
        return cnt
            
    def mrge_srt(arr, l, r):
        cnt = 0
        if l >= r:
            return cnt
        mid = l + ((r - l) // 2)
        cnt += mrge_srt(arr, l, mid)
        cnt += mrge_srt(arr, mid + 1, r)
        cnt += cntPairs(arr, l, mid, r)
        merge(arr, l, mid, r)
        return cnt
    
    return mrge_srt(arr, 0, n - 1)   

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))