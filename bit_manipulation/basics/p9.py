# Clear the ith bit
# Set that bit to 0, while keeping all other bits in their positions.

from bit_manipulation.bit import bit

def clear_bit(n, i):
    return n & ~(1 << i)

if __name__ == "__main__":
    n, i = map(int, input().split())
    print(bit(n))
    a = clear_bit(n , i)
    print(a, bit(a))