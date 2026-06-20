# Integer to binary

def solve1(num):
    """Manual"""
    if num == 0: return '0'
    bin = []
    while num:
        if not num % 2:
            bin.append("0")
        else:
            bin.append("1")
        num //= 2
    
    bin.reverse()
    return ''.join(bin)

def solve2(num):
    """built in"""
    return bin(num)[2:]

def solve3(num):
    """bitwise"""
    if num == 0: return '0'

    bin = []
    
    while num:
        bin.append(str(num & 1))
        num >>= 1
    
    return ''.join(reversed(bin))

def solve4(num):
    """Recursive"""
    if num < 2:
        return str(num)

    return solve4(num // 2) + str(num % 2)

def solve5(num):
    """Using format"""
    return format(num, '08b')

def solve6(num):
    """using f string"""
    return f"{num:08b}"

if __name__ == "__main__":
    n = int(input())
    print(solve1(n))
    print(solve2(n))
    print(solve3(n))
    print(solve4(n))
    print(solve5(n))
    print(solve6(n))
    