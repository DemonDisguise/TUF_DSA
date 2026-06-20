# Implement Queue using Linked list

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def push(self, el):
        nw_node = Node(el)
        if self.empty():
            self.head = self.tail = nw_node
        else:
            self.tail.next = nw_node
            self.tail = nw_node
        self.size += 1
    
    def pop(self):
        if self.empty():
            raise IndexError("Queue Underflow")
        el = self.head.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return el
    
    def peek(self):
        if self.empty():
            raise IndexError("Queue Underflow")
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
        return f"Queue({res})"
    
if __name__ == "__main__":
    q = Queue()
    q.push(5)
    print(q)
    q.push(10)
    print(q)
    print(q.peek())
    print(q.pop())
    print(q.empty())