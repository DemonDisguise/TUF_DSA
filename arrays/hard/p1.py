# Pascal's triangle

def solve1(n):
    """
    Given n size return n sized pascal triangle
    """
    rows = [[1]]
    for i in range(1, n):
        row = []
        for j in range(1, len(rows[i - 1])):
            row.append(rows[i - 1][j - 1] + rows[i - 1][j])
        rows.append([1] + row + [1])
    
    return rows

def solve2(n):
    """
    Given n, return the nth row of the pascal triangle
    """ 
    row = []
    
    val = 1
    row.append(val)
    
    for k in range(1, n):
        val = val * (n - k) // k
        row.append(val)
    
    return row

def solve3(r, c):
    """
    Given r and c, returns the element on that coordinates
    """
    n = r - 1
    k = c - 1
    
    res = 1
    
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

if __name__ == "__main__":
    # Solve1
    # n = int(input())
    # rows = solve1(n)
    # for i in rows:
    #     print(*i)
    
    # Solve2
    n = int(input())
    print(*solve2(n))
    
    # Solve3
    r, c = map(int, input().split())
    print(solve3(r, c))
        