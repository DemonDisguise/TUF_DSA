# Stock span problem
""" Given an array arr of size n, where each element arr[i] represents the stock price on day i. Calculate the span of stock prices for each day.

The span Sᵢ for a specific day i is defined as the maximum number of consecutive previous days (including the current day) for which the stock price was less than or equal to the price on day i. """


class StockSpanner:
    def __init__(self):
        self.stk = []
    
    def next(self, price: int) -> int:
        span = 1
        
        while self.stk and self.stk[-1][0] < price:
            span += self.stk[-1][1]
            self.stk.pop()
        
        self.stk.append((price, span))
        return span

def solve(arr: list[int]) -> list[int]:
    s = StockSpanner()
    res = []
    for i in arr:
        res.append(s.next(i))
    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
    
    # 120 100 60 80 90 110 115