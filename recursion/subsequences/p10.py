# Combination Sum III
# All possible set of k no.s that can be added together to equal n while:
# there is only use of numerals 1 through 9
# a single use is made of each number
# Return list of every feasible combination that is allowed.

def helper(start, k, target, curr, res):
    if target == 0 and len(curr) == k:
        res.append(curr[:])
        return
    
    if target < 0 or len(curr) > k:
        return 
    
    for i in range(start, 10):
        curr.append(i)
        helper(i + 1, k, target - i, curr, res)
        curr.pop()

def solve(k, n):
    res = []
    
    helper(1, k , n , [], res)
    
    return res

if __name__ == "__main__":
    k = int(input())
    n = int(input())
    res = solve(k, n)
    for i in res:
        print(*i)
        