# Remove ith bit 

from bit_manipulation.bit import bit

def del_bit(n, i):
   lower = n & ((1 << i) - 1)
   higher = n >> (i + 1)
   return  (higher << i) | lower

if __name__ == "__main__":
    n, i = map(int, input().split())
    print(bit(n))
    res = del_bit(n, i)
    print(res, bit(res))
