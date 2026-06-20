# Find XOR of numbers from L to R

def xor_upto(n):
    return [n, 1, n + 1, 0][n % 4]

def solve(l, r):
    return xor_upto(r) ^ xor_upto(l - 1)

if __name__ == "__main__":
    l, r = map(int, input().split())
    print(solve(l, r))
    