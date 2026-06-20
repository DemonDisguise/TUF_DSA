# Expression Add Operators
# Given string num that contains only digits and an integer target
# return all possiblities to insert the binary operations +, -, / or * 
# between digits of num so that result is the target value
# operands in the returned expressions should not contain leading zeros
# Number can contain multiple digits

def solve(num, target):
    res = []
    
    n = len(num)
    
    def dfs(idx, expr, value, prev):
        if idx == n:
            if value == target:
                res.append(expr)
            return
        
        for j in range(idx, n):
            if j > idx and num[idx] == '0':
                break
            
            curr_str = num[idx:j + 1]
            curr_num = int(curr_str)
            
            if idx == 0:
                dfs(j + 1, curr_str, curr_num, curr_num)
            else:
                dfs(j + 1, expr + '*' + curr_str, value - prev + prev * curr_num, prev*curr_num)
                dfs(j + 1, expr + '+' + curr_str, value + curr_num, curr_num)
                dfs(j + 1, expr + '-' + curr_str, value - curr_num, -curr_num)

    dfs(0, "", 0, 0)
    return res

if __name__ == "__main__":
    num = input()
    target = int(input())
    print(*solve(num, target))
    