# Remove K digits
#  Given a string nums representing a non-negative integer, and an integer k, find the smallest possible integer after removing k digits from num.

def solve(num, k):
    stk = []

    for ch in num:

        while stk and stk[-1] > ch and k > 0:
            stk.pop()
            k -= 1

        stk.append(ch)

    while stk and k > 0:
        stk.pop()
        k -= 1

    ans = ''.join(stk).lstrip('0')

    return ans if ans else '0'


if __name__ == "__main__":
    num, k = input().split()
    print(solve(num, int(k)))