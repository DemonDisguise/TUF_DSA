# gcd or hcf

def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a == 0:
        return b
    return a

a: int = int(input())
b: int = int(input())
print(gcd(a, b))
