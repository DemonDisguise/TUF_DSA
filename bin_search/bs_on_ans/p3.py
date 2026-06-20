# Koko eating bananas
# A monkey Koko is given 'n' piles of bananas, whereas 'ith' pile has a[i] bananas
# integer 'h' denotes time(in hours) for all bananas to be eaten

# each hour, monkey choses non-empty pile of bananas and eats k bananas. if pile less than k, he consumes all and won't eat any more bananas in that hour
# find min number of bananas 'k' to eat per hour so that the monkey can eat all the bananas within 'h' hours

def solve(arr, h):
    def can(b):
        ans = 0
        for i in arr:
            ans += (i + b - 1) // b
            if ans > h:
                return False
        return True
    
    m = max(arr)
    l, r = 1, m
    ans = m
    
    while l <= r:
        mid = l + ((r - l) // 2)
        
        if can(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    h = int(input())
    print(solve(arr, h))