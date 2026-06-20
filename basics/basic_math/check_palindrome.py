# Palindrome check
def is_palindrome(n: int) -> bool:
    sign = -1 if n < 0 else 1
    tmp = abs(n)
    rev_num = 0
    while tmp > 0:
        rev_num = rev_num * 10 + tmp % 10
        tmp //= 10
    return True if n == sign * rev_num else False

n: int = int(input())
print(is_palindrome(n))