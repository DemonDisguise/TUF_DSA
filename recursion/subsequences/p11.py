# Letter Combinations of a Phone Number
# String consisting of digits 2 - 9 (inclusive)
# Return all possible letter combinations that the number can represent

def helper(ind, curr, nums, res, mp):
    if ind == len(nums):
        res.append(''.join(curr))
        return
    
    char = mp[nums[ind]]
    for ch in char:
        curr.append(ch)
        helper(ind + 1, curr, nums, res, mp)
        curr.pop()
            
def solve(nums):
    if not nums:
        return []
    
    mp = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    
    res = []
    helper(0, [], nums, res, mp)
    return res

if __name__ == "__main__":
    nums = input()
    print(*solve(nums))