# Maximal Rectangles (Stack version)
# Given a m x n binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

def solve(matrix):
    def get_mx_area(arr):
        n = len(arr)
        stk = []
        mx = 0

        for i in range(n):
            while stk and arr[stk[-1]] > arr[i]:
                curr = stk.pop()
                left = stk[-1] if stk else -1
                mx = max(mx, arr[curr] * (i - left - 1))

            stk.append(i)

        while stk:
            curr = stk.pop()
            left = stk[-1] if stk else -1
            mx = max(mx, arr[curr] * (n - left - 1))

        return mx

    n, m = len(matrix), len(matrix[0])

    prefix_sum = [[0] * m for _ in range(n)]

    for j in range(m):
        height = 0

        for i in range(n):
            if matrix[i][j] == 1:
                height += 1
            else:
                height = 0

            prefix_sum[i][j] = height

    mx_area = 0

    for i in range(n):
        mx_area = max(mx_area, get_mx_area(prefix_sum[i]))

    return mx_area

if __name__ == "__main__":
    n, m = map(int, input().split())
    mtrx = []
    for i in range(n):
        mtrx.append(list(map(int, input().split())))
    print(solve(mtrx))
    