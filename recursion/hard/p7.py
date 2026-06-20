# Word break
# string s and dict of strings wordDict
# return true if s can be segmented into
# space separated sequence of one or more dictionary words
# otherwise return false

def solve(s, word_set):
    def dfs(start_ind):
        if start_ind == len(s):
            return True
        
        for end_ind in range(start_ind + 1, len(s) + 1):
            curr_wrd = s[start_ind:end_ind]
            
            if curr_wrd in word_set and dfs(end_ind):
                return True
        
        return False

    return dfs(0)

if __name__ == "__main__":
    s = input()
    word_set = set(input().split())
    print(solve(s, word_set))