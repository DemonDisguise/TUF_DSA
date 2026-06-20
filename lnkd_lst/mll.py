# Multi-level single linked list

class Node:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

    def __str__(self):
        return str(self.val)

    __repr__ = __str__


class MSLL:
    def __init__(self, data=None):
        self.head = None

        if data:
            self.build(data)
            
    def _build_list(self, arr):
        """Builds a normal SLL from array and returns head"""
        if not arr:
            return None

        head = Node(arr[0])
        curr = head

        for val in arr[1:]:
            curr.next = Node(val)
            curr = curr.next

        return head

    def _tail(self, root):
        while root and root.next:
            root = root.next
        return root

    def find(self, val):
        """DFS search across whole multilevel list"""

        def dfs(node):
            while node:
                if node.val == val:
                    return node

                if node.child:
                    found = dfs(node.child)

                    if found:
                        return found

                node = node.next

            return None

        return dfs(self.head)

    def append_main(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            return

        tail = self._tail(self.head)
        tail.next = node

    def add_child(self, parent_val, child_arr):
        parent = self.find(parent_val)

        if not parent:
            raise ValueError(f"Node {parent_val} not found")

        parent.child = self._build_list(child_arr)

    def build(self, data):
        """
        Example:
        [
            [1,2,3],
            [2,[7,8]],
            [8,[11,12]]
        ]
        """

        if not data:
            return

        self.head = self._build_list(data[0])

        for parent, child_list in data[1:]:
            self.add_child(parent, child_list)
            
    def __str__(self):
        res = []

        def get_line(node):
            vals = []

            while node:
                vals.append(str(node.val))
                node = node.next

            return " -> ".join(vals)

        def dfs(node):
            if not node:
                return

            curr = node

            while curr:
                if curr.child:
                    res.append(
                        f"{curr.val}.child -> {get_line(curr.child)}"
                    )

                    dfs(curr.child)

                curr = curr.next

        res.append(get_line(self.head))
        dfs(self.head)

        return "\n".join(res)
    
    def make_list(self):
        res = []

        def get_arr(node):
            arr = []

            while node:
                arr.append(node.val)
                node = node.next

            return arr

        def dfs(node):
            curr = node

            while curr:
                if curr.child:
                    child_arr = get_arr(curr.child)

                    res.append([curr.val, child_arr])

                    dfs(curr.child)

                curr = curr.next

        res.append(get_arr(self.head))
        dfs(self.head)

        return res

if __name__ == "__main__":

    ll = MSLL([
        [1, 2, 3],
        [2, [7, 8]],
        [8, [11, 12]]
    ])

    print(ll)