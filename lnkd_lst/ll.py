# Single Linked List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

class SLL:
    def __init__(self, data=None):
        self.head = None
        
        self.size = 0
        
        if data is None:
            return
        
        if isinstance(data, Node):
            self.head = data
            self.size = self._getsize()
        else:
            self.head = self._build(data)
    
    def __len__(self):
        return self.size
    
    def _getsize(self):
        size = 0
        
        curr = self.head
        
        while curr:
            size += 1
            curr = curr.next
        
        return size
    
    def _build(self, arr):
        dummy = Node()
        curr = dummy
        
        for x in arr:
            curr.next = Node(x)
            curr = curr.next
            self.size += 1
        
        return dummy.next

    def to_list(self):
        arr = []
        curr = self.head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        return arr

    def __str__(self):
        if not self.head:
            return "None"
        
        vals = []
        curr = self.head 

        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        
        return " ".join(vals)
    
    def append(self, val): 
        new = Node(val)
        if not self.head:
            self.head = new
            self.size += 1
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new
        self.size += 1
        
    def appendleft(self, val):
        self.head = Node(val, self.head)
        self.size += 1
    
    def insert_at(self, i, val):
        new = Node(val)
        dummy = Node(0)
        dummy.next = self.head
        
        curr = dummy
        pos = 0
        
        while pos < i and curr.next:
            curr = curr.next
            pos += 1
            
        new.next = curr.next
        curr.next = new

        self.head = dummy.next
        self.size += 1
    
    def pop(self):
        if not self.head:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        
        curr = dummy
        while curr.next and curr.next.next:
            curr = curr.next
            
        val = curr.next.val
        curr.next = None
        
        self.head = dummy.next
        self.size -= 1
        
        return val
    
    def popleft(self):
        if not self.head:
            return None
        
        val = self.head.val
        self.head = self.head.next
        
        self.size -= 1
        
        return val 
    
    def remove(self, val):
        dummy = Node(0)
        dummy.next = self.head
        
        curr = dummy
        
        while curr.next and curr.next.val != val:
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
            self.size -= 1
        
        self.head = dummy.next
    
    def remove_all(self, val):
        dummy = Node(0)
        dummy.next = self.head
        
        curr = dummy
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                self.size -= 1
            else:
                curr = curr.next
        
        self.head = dummy.next
    
    def remove_last(self, val):
        dummy = Node(0)
        dummy.next = self.head

        curr = dummy
        
        last = None
        
        while curr.next:
            if curr.next.val == val:
                last = curr
            
            curr = curr.next
        
        if last:
            last.next = last.next.next
            self.size -= 1

        self.head = dummy.next
    
    def delete_at(self, i):
        dummy = Node(0)
        dummy.next = self.head
        
        curr = dummy
        pos = 0
        
        while pos < i and curr.next:
            curr = curr.next
            pos += 1
        
        
        if not curr.next:
            return None
        
        val = curr.next.val
        curr.next = curr.next.next
        
        self.head = dummy.next
        self.size -= 1
        
        return val
    
    def search(self, val):
        curr = self.head
        
        pos = 0
        
        while curr:
            if curr.val == val:
                return pos
            curr = curr.next
            pos += 1
        
        return -1
    
    def make_cycle(self, pos=0):
        if pos < 0 or not self.head:
            return
        
        target = None
        curr = self.head
        
        i = 0
        
        while curr:
            if i == pos:
                target = curr
                
            if not curr.next:
                break
            
            curr = curr.next
            i += 1
         
        if target:
            curr.next = target
    
    def break_cycle(self):
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return
        
        slow = self.head
        
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        
        fast.next = None
    
    def has_cycle(self):
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return True
        return False          

    # Intersection logic
    def get_node_at(self, index):
        curr = self.head
        
        while index and curr:
            curr = curr.next
            index -= 1
        
        return curr
    
    def attach_at(self, node):
        if not self.head:
            self.head = node
            return
        
        curr = self.head
        
        while curr.next:
            curr = curr.next
        
        curr.next = node
    
    def attach_at_index(self, other, index):
        node = other.get_node_at(index)
        
        if not node:
            return
        
        self.attach_at(node)

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(ll.delete_at(1))
    
    