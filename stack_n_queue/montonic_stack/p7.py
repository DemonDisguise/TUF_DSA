# Asteroid collision
""" Given an array of integers asteroids, where each integer represents an asteroid in a row, determine the state of the asteroids after all collisions. In this array, the absolute value represents the size of the asteroid, and the sign represents its direction (positive meaning right and negative meaning left). All asteroids move at the same speed.

When two asteroids meet, the smaller one will explode. If they are the same size, both will explode. Asteroids moving in the same direction will never meet. """

def solve(arr):
    stk = []

    for a in arr:
        while stk and a < 0 and stk[-1] > 0:
            if stk[-1] < -a:         
                stk.pop()
                continue
            elif stk[-1] == -a:      
                stk.pop()
            break
        else:
            stk.append(a)

    return stk

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(*solve(arr))
