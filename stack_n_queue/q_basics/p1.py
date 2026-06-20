# Implement Queue using array

class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if self.empty():
            raise IndexError("Queue underflow")
        return self.queue.pop(0)
    
    def peek(self):
        if self.empty():
            raise IndexError("Queue underflow")
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)
    
    def __repr__(self):
        return f"Queue:({self.queue})"

if __name__ == "__main__":
    q = Queue()
    q.push(5)
    q.push(10)
    print(q.peek())
    print(q.pop())
    print(q.empty())
    
    