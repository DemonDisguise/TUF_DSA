# Set or unset the rightmost bit

from bit_manipulation.bit import bit

def set_rbit(n):
    return n | (n + 1)

def unset_rbit(n):
    return n & (n - 1)

if __name__ == "__main__":
    n = int(input())
    print(bit(n))
    a = set_rbit(n)
    print(a, bit(a))
    b = unset_rbit(n)
    print(b, bit(b))
    