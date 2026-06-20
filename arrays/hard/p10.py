# Count inversions

def solve(arr):
    cnt = 0
    n = len(arr)
    
    def merge(arr, l, mid, r):
        nonlocal cnt
        tmp = []
        left = l
        right = mid + 1
        
        while left <= mid and right <= r:
            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                cnt += (mid - left + 1)
                right += 1
        
        while left <= mid:
            tmp.append(arr[left])
            left += 1
        
        while right <= r:
            tmp.append(arr[right])
            right += 1
        
        for i in range(l, r + 1):
            arr[i] = tmp[i - l]
    
    def mrge_srt(arr, l, r):
        if l >= r:
            return
        mid = l + ((r - l) // 2)
        mrge_srt(arr, l, mid)
        mrge_srt(arr, mid + 1, r)
        merge(arr, l, mid, r)
    
    mrge_srt(arr, 0, n - 1)
    return cnt
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
    