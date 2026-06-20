# stack using linked list

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, el):
        self.head = Node(el, self.head)
        self.size += 1
    
    def pop(self):
        if self.empty():
            raise IndexError("Stack underflow")
        
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val
    
    def top(self):
        if self.empty():
            raise IndexError("Stack underflow")
        return self.head.val
    
    def empty(self):
        return self.head is None
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return f"Stack({res})"

if __name__ == "__main__":
    stk = Stack()
    stk.push(9)
    stk.push(10)
    stk.push(15)
    stk.pop()
    print(stk)
    print(stk.top())
    print(len(stk))