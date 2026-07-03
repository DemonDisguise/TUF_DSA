# Flattening a Linked List

import ast
from lnkd_lst.mll import MSLL, Node

def merge(a, b):

    dummy = tail = Node(0)

    while a and b:

        if a.val <= b.val:
            tail.child = a
            a = a.child
        else:
            tail.child = b
            b = b.child

        tail = tail.child

        # remove horizontal links
        tail.next = None

    tail.child = a if a else b

    return dummy.child


def solve(root):
    if not root or not root.next:
        return root

    # flatten right side
    right = solve(root.next)

    # disconnect horizontal link
    root.next = None

    # merge current vertical list
    # with flattened right side
    return merge(root, right)

if __name__ == "__main__":
    data = ast.literal_eval(input())
    ll = MSLL(data)
    ll.head = solve(ll.head)
    print(ll)
    