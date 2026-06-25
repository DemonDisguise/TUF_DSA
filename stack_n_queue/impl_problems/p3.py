# Celebrity problem
"""  A celebrity is a person who is known by everyone else at the party but does not know anyone in return. Given a square matrix M of size N x N where M[i][j] is 1 if person i knows person j, and 0 otherwise, determine if there is a celebrity at the party. Return the index of the celebrity or -1 if no such person exists.

Note that M[i][i] is always 0. """
# Is a two pointer problem, but stack for better simulation and understanding.

import sys

def solve(mtrx):
    n = len(mtrx)
    
    top, down = 0, n - 1
    
    while top < down:
        if mtrx[top][down] == 1:
            top += 1
        elif mtrx[down][top] == 1:
            down -= 1
        else:
            top += 1
            down -= 1
    
    if top > down:
        return -1

    for i in range(n):
        if i == top:
            continue
        
        if mtrx[top][i] == 1 or mtrx[i][top] == 0:
            return -1
    
    return top

if __name__ == "__main__":
    matrix = []
    
    for line in sys.stdin:
        line = line.strip()
        if line:
            matrix.append(list(map(int, line.split())))
    
    print(solve(matrix))
    