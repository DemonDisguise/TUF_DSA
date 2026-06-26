# Minimum window subsequence
""" Given two strings S and T, find the minimum contiguous substring W of S such that T is a subsequence of W.

If there are multiple minimum windows, return the one with the left-most starting index.

If no such window exists, return an empty string "".

A subsequence is a sequence that can be derived from another sequence by deleting some or no characters without changing the order of the remaining characters. """

def solve(S: str, T: str) -> str:
    n, m = len(S), len(T)
    res = ""
    min_len = float('inf')
    i = 0

    while i < n:
        j = 0
        k = i
        while k < n:
            if S[k] == T[j]:
                j += 1
                if j == m:
                    break
            k += 1

        if j < m:
            break  

        end = k

        j = m - 1
        start = end
        while j >= 0:
            if S[start] == T[j]:
                j -= 1
            start -= 1
        start += 1

        if end - start + 1 < min_len:
            min_len = end - start + 1
            res = S[start:end + 1]

        i = start + 1  

    return res

if __name__ == "__main__":
    s, t = input().split()
    print(solve(s, t))
