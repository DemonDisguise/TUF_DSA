# Stack using queue

from collections import deque

class Stack:
    def __init__(self):
        self.stk = deque()
    
    def push(self, el):
        self.stk.append(el)
        
        for _ in range(len(self.stk) - 1):
            self.stk.append(self.stk.popleft())
    
    def pop(self):
        return self.stk.popleft()
    
    def top(self):
        return self.stk[0]
    
    def empty(self):
        return len(self.stk) == 0

    def __len__(self):
        return len(self.stk)
    
    def __repr__(self):
        return f"Stack({list(self.stk)})"

if __name__ == "__main__":
    stk = Stack()
    stk.push(9)
    stk.push(10)
    stk.push(15)
    stk.pop()
    print(stk)
    print(stk.top())
    print(len(stk))