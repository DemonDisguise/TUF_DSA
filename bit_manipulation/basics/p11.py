# Extract the ith bit

from bit_manipulation.bit import bit

def extract_bit(n, i):
    return (n >> i) & 1

def extract_kbits(n, k):
    return n & ((1 << k) - 1)

def extract_range_bits(n, l, r):
    return (n >> l) & ((1 << (r - l + 1)) - 1)

if __name__ == "__main__":
    n, i = map(int, input().split())
    print(bit(n))
    res = extract_bit(n, i)
    print(res, bit(res))
    res = extract_kbits(n, i)
    print(res, bit(res))
    l, r = map(int, input().split())
    res = extract_range_bits(n, l, r)
    print(res, bit(res))
    
# mask for range(l, r)
# mask = ((1 << (r - l + 1)) - 1) << 1