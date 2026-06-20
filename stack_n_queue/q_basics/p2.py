# Implement Queue using stack
    
# O(n) for push, O(1) for pop and peek
class Queue1:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []
    
    def push(self, item):
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(item)
        while self.stk2:
            self.stk1.append(self.stk2.pop())
    
    def pop(self):
        if self.empty():
            raise IndexError("Queue Underflow")
        return self.stk1.pop()
    
    def peek(self):
        if self.empty():
            raise IndexError("Queue Underflow")
        return self.stk1[-1]
    
    def empty(self):
        return not self.stk1
    
    def __len__(self):
        return len(self.stk1)
    
    def __repr__(self):
        return f"Queue({self.stk1})"

# O(1) for push, O(n) for pop and peek
class Queue2:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
    
    def push(self, item):
        self.in_stk.append(item)
    
    def pop(self):
        if self.empty():
            raise IndexError("Queue Underflow")
        
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk.pop()
    
    def peek(self):
        if self.empty():
            raise IndexError("Queue Underflow")
        
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
    
    def empty(self):
        return not self.in_stk and not self.out_stk
    
    def __len__(self):
        return len(self.in_stk) + len(self.out_stk)

    def __repr__(self):
        return f"Queue({list(reversed(self.out_stk)) + self.in_stk})"

if __name__ == "__main__":
    q = Queue2()
    q.push(5)
    print(q)
    q.push(10)
    print(q)
    print(q.peek())
    print(q.pop())
    print(q.empty())
    