# Palindrome partitioning
# input: "aab"
# output: [["a", "a", "b"], ["aa", "b"]]

def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

def helper(ind, curr, s, res):
    if ind == len(s):
        res.append(curr[:])
        return
    
    for i in range(ind, len(s)):
        if isPalindrome(s, ind, i):
            curr.append(s[ind:i+1])
            helper(i + 1, curr, s, res)
            curr.pop()

def solve(s):
    res = []
    
    helper(0, [], s, res)
    
    return res

if __name__ == "__main__":
    s = input()
    res = solve(s)
    for i in res:
        print(*i)
    