# Assign cookies
""" Consider a scenario where a teacher wants to distribute cookies to students, with each student receiving at most one cookie. Given two arrays, student and cookie, the ith value in the student array describes the minimum size of cookie that the ith student can be assigned. 
The jth value in the cookie array represents the size of the jth cookie. If cookie[j] >= student[i], the jth cookie can be assigned to the ith student. Maximize the number of students assigned with cookies and output the maximum number. """

from typing import List

def solve(g: List[int], s: List[int]) -> int:
    n, m = len(g), len(s)
    g.sort()
    s.sort()
    
    i = j = 0
    
    while i < n and j < m:
        if s[j] >= g[i]:
            i += 1
        j += 1
    
    return i

if __name__ == "__main__":
    student = list(map(int, input().split()))
    cookie = list(map(int, input().split()))
    print(solve(student, cookie))

# 1 5 3 3 4
# 4 2 1 2 1 3 