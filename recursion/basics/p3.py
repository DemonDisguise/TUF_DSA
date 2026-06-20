# Implement Pow(x, n)
# X raised to the power N

def pow(x, n):
    if n < 0:
        return 1 / pow(x, -n)
    
    if n == 0:
        return 1
    
    if n == 1:
        return x
    
    if n & 1:
        return x * pow(x, n - 1) 
    else:
        return pow(x * x, n // 2)   

if __name__ == "__main__":
    x = float(input())
    n = int(input())
    print(pow(x, n))
    