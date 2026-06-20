# Stock buy and sell

def solve(arr):
    mx_prft = 0
    mn_prce = float('inf')

    for i in arr:
        if mn_prce < i:
            mn_prce = i
        else:
            mx_prft = max(mx_prft, i - mn_prce)
    
    return mx_prft

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
