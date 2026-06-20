# Minimum Stack

class MinStack:
    def __init__(self):
        self.stk = []
        self.min_ele = None

    def push(self, x):
        if not self.stk:
            self.stk.append(x)
            self.min_ele = x

        elif x >= self.min_ele:
            self.stk.append(x)

        else:
            encoded = 2 * x - self.min_ele
            self.stk.append(encoded)
            self.min_ele = x

    def pop(self):
        if self.empty():
            raise IndexError("Stack underflow")

        top = self.stk.pop()

        if top >= self.min_ele:
            return top

        # encoded value
        actual = self.min_ele
        self.min_ele = 2 * self.min_ele - top

        if not self.stk:
            self.min_ele = None

        return actual

    def top(self):
        if self.empty():
            raise IndexError("Stack underflow")

        top = self.stk[-1]

        if top >= self.min_ele:
            return top

        return self.min_ele

    def get_min(self):
        if self.empty():
            raise IndexError("Stack underflow")

        return self.min_ele

    def empty(self):
        return len(self.stk) == 0

    def __len__(self):
        return len(self.stk)

    def __repr__(self):
        return f"Stack={self.stk}, Min={self.min_ele}"


if __name__ == "__main__":
    s = MinStack()

    s.push(12)
    s.push(15)
    s.push(10)
    print(s.get_min())
    s.pop()
    print(s.get_min())
    print(s.top())
    s.push(10)
    print(s.top())