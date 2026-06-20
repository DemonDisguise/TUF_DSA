# Segregate even and odd nodes in linked list

from lnkd_lst.ll import SLL, Node

def solve(root: Node) -> Node:
    if not root or not root.next:
        return root
    
    even = Node()
    odd = Node()
    
    p1, p2 = even, odd
    curr = root
    
    while curr:
        nxt = curr.next
        curr.next = None
        
        if curr.val & 1:
            p2.next = curr
            p2 = curr
        else:
            p1.next = curr
            p1 = curr
            
        curr = nxt

    p1.next = odd.next
    
    return even.next

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(SLL(solve(ll.head)))
    