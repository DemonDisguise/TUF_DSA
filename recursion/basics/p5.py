# Sort a stack
# Using recusion in descending order
# You are not allowed to use loop based sorting methods
# Use recursive operation and stndrd push, pop and isEmpty

def insert(stk, temp):
    if not stk or stk[-1] >= temp:
        stk.append(temp)
        return

    val = stk.pop()
    insert(stk, temp)
    
    stk.append(val)

def solve(stk):
    if stk:
        temp = stk.pop()
        solve(stk)
        insert(stk, temp)

if __name__ == "__main__":
    stk = list(map(int, input().split()))
    solve(stk)
    print(*stk)