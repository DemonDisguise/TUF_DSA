# Toggle the ith bit 

from bit_manipulation.bit import bit

def toggle_bit(num, ind):
    return num ^ (1 << ind)

if __name__ == "__main__":
    n, i = map(int, input().split())
    print(bit(n))
    a = toggle_bit(n, i)
    print(a, bit(a))
    