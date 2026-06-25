# Maximum point you can obtain from cards
""" Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. 
In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards. """

# O(k)
def solve(arr, k):
    n = len(arr)
    
    left_sum = sum(arr[:k])
    mx_sum = left_sum
    
    right_sum = 0
    r_ind = n - 1
    
    for i in range(k - 1, -1, -1):
        left_sum -= arr[i]
        right_sum += arr[r_ind]
        r_ind -= 1
        
        mx_sum = max(mx_sum, left_sum + right_sum)
    
    return mx_sum

# Use this when n is large as this is O(n)
""" def solve(arr, k):
    n = len(arr)

    total = sum(arr)

    if k == n:
        return total

    window = n - k

    curr = sum(arr[:window])
    min_sum = curr

    for r in range(window, n):
        curr += arr[r] - arr[r - window]
        min_sum = min(min_sum, curr)

    return total - min_sum """

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
    
    # 5 4 1 8 7 1 3
    # 3