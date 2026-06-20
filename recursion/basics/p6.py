# Reverse a stack

def insert(stk, temp):
    if not stk:
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