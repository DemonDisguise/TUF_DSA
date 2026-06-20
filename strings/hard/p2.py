# Count and say sequence
# A sequence of digit strings defined by the recursive formula
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1)

# Run-length encoding(RLE) is a string compression method that works by replacing consecutive identical characters
# with the concatenation of the characte and the number marking the count of the characters.
# Eg. compress string "3322251" we replace "33" with "23", replace "222" with "32", repalce "5" with "15" and replace "1" with "11".
# Result: 23321511

# Given n, return nth element of the count and say sequence

def solve(n):
    res = "1"
    
    for _ in range(1, n):
        curr = []
        cnt = 1
        
        for j in range(1, len(res)):
            if res[j] == res[j - 1]:
                cnt += 1
            else:
                curr.append(str(cnt))
                curr.append(res[j - 1])
                cnt = 1
        
        curr.append(str(cnt))
        curr.append(res[-1])

        res = "".join(curr)
    
    return res               

if __name__ == "__main__":
    n = int(input())
    print(solve(n))