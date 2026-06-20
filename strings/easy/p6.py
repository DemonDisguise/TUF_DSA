# Check if one string is rotation of another

def solve(s, goal):
    n = len(goal)
    if n != len(s):
        return False
    
    return goal in (s + s)

if __name__ == "__main__":
    s, goal = input().split()
    print(solve(s, goal))
