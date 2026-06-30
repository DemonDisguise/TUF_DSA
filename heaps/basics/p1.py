# MinHeap implementation

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return bool(self.heap)

    def __repr__(self):
        return f"MinHeap({self.heap})"

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def push(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")

        minimum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify(0)

        return minimum

    def build_heap(self, iterable):
        self.heap = list(iterable)

        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._heapify(i)

    def decrease_key(self, index, value):
        if value > self.heap[index]:
            raise ValueError("New value must be smaller.")

        self.heap[index] = value
        self._bubble_up(index)

    def increase_key(self, index, value):
        if value < self.heap[index]:
            raise ValueError("New value must be larger.")

        self.heap[index] = value
        self._heapify(index)

    def delete(self, index):
        self.decrease_key(index, float("-inf"))
        self.pop()

    def replace(self, value):
        if not self.heap:
            self.heap.append(value)
            return None

        minimum = self.heap[0]
        self.heap[0] = value
        self._heapify(0)
        return minimum

    def pushpop(self, value):
        if self.heap and value > self.heap[0]:
            value, self.heap[0] = self.heap[0], value
            self._heapify(0)
        return value

    def _bubble_up(self, i):
        while i:
            parent = self._parent(i)

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _heapify(self, i):
        n = len(self.heap)

        while True:
            smallest = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

if __name__ == "__main__":
    heap = MinHeap()

    for x in [5, 3, 8, 1, 6, 2]:
        heap.push(x)

    print(heap)

    print(heap.peek())

    while heap:
        print(heap.pop(), end=" ")