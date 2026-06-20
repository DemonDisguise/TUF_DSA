# Doubly Linked List

from __future__ import annotations
from collections.abc import Iterable

class Node:
    def __init__(
        self, 
        val: int=0, 
        next: Node | None= None, 
        prev: Node | None = None
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)


class DLL:
    def __init__(
        self, 
        data: Iterable[int] | None = None
    ):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

        if isinstance(data, Node):
            self.head = data
            self.set_tail()
            self.length = self.get_size()

        elif data:
            self._build(data)

    def get_size(self) -> int:
        curr = self.head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        return length

    def set_tail(self) -> None:
        curr = self.head

        while curr and curr.next:
            curr = curr.next

        self.tail = curr

    def _build(self, data: Iterable[int]) -> None:
        self.head = self.tail = Node(data[0])
        self.length = 1

        for val in data[1:]:
            new = Node(val, prev=self.tail)

            self.tail.next = new
            self.tail = new
            self.length += 1
    
    def __len__(self) -> int:
        return self.length
    
    def to_list(self) -> list[int]:
        vals = []
        
        curr = self.head
        
        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals
    
    def __str__(self) -> str:
        if not self.head:
            return None

        return " ".join(list(map(str, self.to_list())))

    def append(self, val: int) -> None:
        new = Node(val, prev = self.tail)

        if not self.tail:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new
            
        self.length += 1
    
    def appendleft(self, val: int) -> None:
        new = Node(val, next=self.head)
        
        self.head.prev = new
        self.head = new
    
    def insert_at(self, i: int, val: int) -> None:
        if i < 0 or i > self.length:
            raise IndexError("Index out of range")

        if i == 0:
            new = Node(val, next=self.head)

            if self.head:
                self.head.prev = new
            else:
                self.tail = new

            self.head = new

        elif i == self.length:
            self.append(val)
            return
        
        else:
            curr = self.head

            for _ in range(i - 1):
                curr = curr.next

            new = Node(val, prev=curr, next=curr.next)

            curr.next.prev = new
            curr.next = new

        self.length += 1
    
    def pop(self) -> int:
        if not self.tail:
            raise IndexError("pop from empty DLL")
        
        val = self.tail.val
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.length -= 1

        return val

    def popleft(self) -> int:
        if not self.tail:
            raise IndexError("pop from empty DLL")
        
        val = self.head.val
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1
        return val

    def remove(self, val: int) -> bool:

        curr = self.head

        while curr and curr.val != val:
            curr = curr.next

        if not curr:
            return False

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.length -= 1

        return True

    def remove_all(self, val: int) -> int:
        curr = self.head
        removed = 0

        while curr:
            nxt = curr.next

            if curr.val == val:

                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                self.length -= 1
                removed += 1

            curr = nxt

        return removed 
    
    def remove_last(self, val: int) -> bool:

        curr = self.tail

        while curr and curr.val != val:
            curr = curr.prev

        if not curr:
            return False

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.length -= 1

        return True 

    def delete_at(self, i: int) -> int:

        if i < 0 or i >= self.length:
            raise IndexError("Index out of range")

        # Optimize traversal direction
        if i < self.length // 2:
            curr = self.head

            for _ in range(i):
                curr = curr.next
        else:
            curr = self.tail

            for _ in range(self.length - i - 1):
                curr = curr.prev

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.length -= 1

        return curr.val     

if __name__ == "__main__":
    ll = DLL(list(map(int, input().split())))

    print(ll)
    print("Head :", ll.head)
    print("Tail :", ll.tail)
    print("Size :", ll.length)

    ll2 = DLL(ll.head)

    print(ll2)
    print("Tail of ll2 :", ll2.tail)