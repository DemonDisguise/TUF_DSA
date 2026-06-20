# Patterns

def p1(n: int) -> None:
    """ 
    *****
    *****
    *****
    *****
    ***** 
    """
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()

def p2(n: int) -> None:
    """ 
    *
    **
    ***
    ****
    *****
    """
    for i in range(n):
        for _ in range(i + 1):
            print("*", end="")
        print()

def p3(n: int) -> None:
    """
    1
    12
    123
    1234
    12345
    """
    for i in range(n):
        for j in range(1, i + 2):
            print(j, end="")
        print()

def p4(n: int) -> None:
    """
    1
    22
    333
    4444
    55555
    """
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end="")
        print()

def p5(n: int) -> None:
    """
    *****
    ****
    ***
    **
    *
    """
    for i in range(n, 0, -1):
        for _ in range(i):
            print("*", end="")
        print()

def p6(n: int) -> None:
    """
    12345
    1234
    123
    12
    1
    """ 
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def p7(n: int) -> None:
    """
        *    
       ***   
      *****
     *******
    *********
    """
    for i in range(n - 1, -1, -1):
        for j in range(1, n * 2):
            if j <= i or j >= (n * 2 - i):
                print(" ", end="")
            else:
                print("*", end="")
        print()

def p8(n: int) -> None:
    """
    *********
     ******* 
      *****
       ***
        *
    """
    for i in range(0, n):
        for j in range(1, n * 2):
            if j <= i or j >= (n * 2 - i):
                print(" ", end="")
            else: 
                print("*", end="")
        print()

def p9(n: int) -> None:
    """
        *    
       ***   
      *****
     *******
    *********
     ******* 
      *****
       ***
        *
    """
    rows = n * 2 - 1
    mid = rows // 2
    for i in range(rows):
        for j in range(rows):
            if i <= mid:
                if j >= mid - i and j <= mid + i:
                    print("*", end="")
                else: 
                    print(" ", end="")
            else:
                if j >= mid - (rows - i - 1) and j <= mid + (rows - i - 1):
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

def p10(n: int) -> None:
    """
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    """
    rows = n * 2 - 1
    mid = rows // 2
    
    for i in range(rows):
        for j in range(n):
            if i <= mid:
                if j <= i:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                if j < rows - i:
                    print("*", end="")
                else:
                    print(" ", end="")        
        print()

def p11(n: int) -> None:
    """
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
    """
    for i in range(n):
        for j in range(i + 1):
            if (i + j) % 2 != 0:
                print(0, end=" ")
            else:
                print(1, end=" ")
        print()

def p12(n: int) -> None:
    """
    1      1
    12    21
    123  321
    12344321
    """
    for i in range(1, n + 1):
        for j in range(1, n * 2 + 1):
            if j <= i:
                print(j, end="")
            elif j > n * 2 - i:
                print((n * 2 - j) + 1, end="")
            else:
                val = j if j <= n else (n * 2 - j) + 1
                print(len(str(val)) * " ", end="")
        print()

def p13(n: int) -> None:
    """
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """
    x = 1
    for i in range(n):
        for _ in range(i + 1):
            print(x, end=" ")
            x += 1
        print()

def p14(n: int) -> None:
    """
    A
    AB
    ABC
    ABCD
    ABCDE
    """
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord('A') + j), end="")
        print()

def p15(n: int) -> None:
    """
    ABCDE
    ABCD
    ABC
    AB
    A
    """
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            print(chr(ord('A') + j), end="")
        print()

def p16(n: int) -> None:
    """
    A
    BB
    CCC
    DDDD
    EEEEE
    """
    for i in range(n):
        for _ in range(i + 1):
            print(chr(ord('A') + i), end="")
        print()

def p17(n: int) -> None:
    """
        A
       ABA
      ABCBA
     ABCDCBA
    ABCDEDCBA
    """
    cols = n * 2 - 1
    mid = cols // 2
    for i in range(n):
        for j in range(n * 2 - 1):
            if j >= mid - i and j <= mid + i:
                print(chr(ord('A') + i - abs(mid - j)), end="")
            else:
                print(" ", end="")
        print()

def p18(n: int) -> None:
    """
    E
    D E
    C D E
    B C D E
    A B C D E
    """
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if j <= (n - i - 1):
                print(chr(ord('A') + i + j), end=" ")
        print()  

def p19(n: int) -> None:
    """
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    """
    rows = 2 * n - 1
    cols = 2 * n
    mid = rows // 2

    for i in range(rows):
        dist = i if i <= mid else rows - 1 - i

        for j in range(cols):
            if j < n - dist or j >= n + dist:
                print("*", end="")
            else:
                print(" ", end="")
        print()
                  
def p20(n: int) -> None:
    """
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    """
    mid = (n * 2 - 1) // 2
    for i in range(n * 2 - 1):
        dist = abs(mid - i)
        for j in range(n * 2):
            if j < n - dist or j >= n + dist:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def p21(n: int) -> None:
    """
    *****
    *   *
    *   *
    *   *
    *****
    """
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print("*", end="")
            else:
                if j == 0 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")        
        print()

def p22(n: int) -> None:
    """
    5 5 5 5 5 5 5 5 5
    5 4 4 4 4 4 4 4 5
    5 4 3 3 3 3 3 4 5
    5 4 3 2 2 2 3 4 5
    5 4 3 2 1 2 3 4 5
    5 4 3 2 2 2 3 4 5
    5 4 3 3 3 3 3 4 5
    5 4 4 4 4 4 4 4 5
    5 5 5 5 5 5 5 5 5
    """
    for i in range(n * 2 - 1):
        for j in range(n * 2 - 1):
            dist = min(i, j, n * 2 - 2 - i, n * 2 - 2 - j)
            print(n - dist, end=" ")
        print()

def p23(n: int) -> None:
    """
    Palindromic number triangle
            1
          2 3 2
        3 4 5 4 3
      4 5 6 7 6 5 4
    5 6 7 8 9 8 7 6 5
    """

    for i in range(1, n + 1):

        for j in range(1, 2 * n):
            if j < n - i + 1:
                print(" ", end=" ")
            
            elif j <= n:
                print(i + j - (n - i + 1), end=" ")
            
            elif j <= n + i - 1:
                print(i + (n + i - 1) - j, end=" ")
        print()

                
if __name__ == "__main__":
    
    n: int = int(input())
    p1(n)
    print()
    p2(n)
    print()
    p3(n)
    print()
    p4(n)
    print()
    p5(n)
    print()
    p6(n)
    print()
    p7(n)
    print()
    p8(n)
    print()
    p9(n)
    print()
    p10(n)
    print()
    p11(n)
    print()
    p12(n)
    print()
    p13(n)
    print()
    p14(n)
    print()
    p15(n)
    print()
    p16(n)
    print()
    p17(n)
    print()
    p18(n)
    print()
    p19(n)
    print()
    p20(n)
    print()
    p21(n)
    print()
    p22(n)
    print()
    p23(n)
    print()