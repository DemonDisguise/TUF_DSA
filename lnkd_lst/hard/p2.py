# Rotate a linked list k times

from lnkd_lst.ll import SLL, Node

def solve(root: Node, k: int) -> Node:
    if not root or not root.next:
        return root
    
    len, tail = 1, root
    
    while tail.next:
        len += 1
        tail = tail.next
    
    k %= len
    
    if k == 0:
        return root
    
    tail.next = root
    
    curr = root
    for _ in range(len - k - 1):
        curr = curr.next
    
    root = curr.next
    curr.next = None
    
    return root

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    ll.head = solve(ll.head, 2)
    print(ll)
    