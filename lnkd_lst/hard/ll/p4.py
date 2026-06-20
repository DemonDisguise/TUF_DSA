import ast


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return str(self.val)


class RandomLL:

    def __init__(self, arr):
        self.head = self.build(arr)

    def build(self, arr):

        if not arr:
            return None

        nodes = [Node(val) for val, _ in arr]

        n = len(nodes)

        # next pointers
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]

        # random pointers
        for i, (_, rnd) in enumerate(arr):

            if rnd is not None:
                nodes[i].random = nodes[rnd]

        return nodes[0]

    def __str__(self):

        res = []

        curr = self.head

        while curr:

            rnd = (
                curr.random.val
                if curr.random
                else None
            )

            res.append(
                f"[{curr.val}, random={rnd}]"
            )

            curr = curr.next

        return " ".join(res)

def solve(head):

    if not head:
        return None

    curr = head

    while curr:

        copy = Node(curr.val)

        copy.next = curr.next
        curr.next = copy

        curr = copy.next

    curr = head

    while curr:

        copy = curr.next

        if curr.random:
            copy.random = curr.random.next

        curr = copy.next

    curr = head

    dummy = copy_curr = Node(0)

    while curr:

        copy = curr.next

        copy_curr.next = copy
        copy_curr = copy

        curr.next = copy.next

        curr = curr.next

    return dummy.next

if __name__ == "__main__":
    data = ast.literal_eval(input())

    ll = RandomLL(data)

    ll.head = solve(ll.head)
    
    print(ll)