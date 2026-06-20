# Binary to integer

def solve1(bin):
    """Manual"""
    num = 0
    
    for bit in bin:
        num = num * 2 + int(bit)
    
    return num

def solve2(bin):
    """Using int"""
    return int(bin, 2)

    # use int(bin, 0) if bin has prefix '0b' for python to auto detect

def solve3(bin):
    """Bitwise"""
    num = 0
    
    for bit in bin:
        num = (num << 1) | int(bit)
    
    return num

def solve4(bin):
    """Recursive"""
    if len(bin) == 1:
        return int(bin)

    return 2 * solve4(bin[:-1]) + int(bin[-1])

def solve5(bin):
    """Using sum()"""
    n = len(bin)
    
    return sum(int(bit) * (1 << (n - 1 - i)) for i, bit in enumerate(bin))

if __name__ == "__main__":
    bin = input()
    print(solve1(bin))
    print(solve2(bin))
    print(solve3(bin))
    print(solve4(bin))
    print(solve5(bin))