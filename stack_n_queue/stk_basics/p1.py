# Stack using arrays

class Stack:
    def __init__(self):
        self.stk = []

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        if self.empty():
            raise IndexError("Stack underflow")
        return self.stk.pop()

    def top(self):
        if self.empty():
            raise IndexError("Stack underflow")
        return self.stk[-1]

    def empty(self):
        return len(self.stk) == 0

    def __len__(self):
        return len(self.stk)

    def __repr__(self):
        return f"Stack({self.stk})"

if __name__ == "__main__":
    stk = Stack()
    stk.push(9)
    stk.push(10)
    stk.push(15)
    stk.pop()
    print(stk)
    print(stk.top())
    print(len(stk))