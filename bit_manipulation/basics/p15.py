# Divide two numbers without multiplication and division

def solve(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError
    
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    
    for bit in range(31, -1, -1):
        if (divisor << bit) <= dividend:
            dividend -= divisor << bit
            quotient |= (1 << bit)
    
    return sign * quotient

if __name__ == "__main__":
    dividend, divisor = map(int, input().split())
    print(solve(dividend, divisor))