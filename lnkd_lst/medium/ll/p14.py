# Add 1 to a number represented by LL

from lnkd_lst.ll import SLL, Node

def solve1(root: Node) -> Node:
    """ Iterative approach: tO(3n) sO(1)"""
    def reverse(root: Node) -> Node:
        prev = None
        curr = root
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    root = reverse(root)
    carry = 1
    
    curr = root
    
    while curr and carry:
        total = curr.val + carry
        
        curr.val = total % 10
        carry = total // 10
        
        if not curr.next and carry:
            curr.next = Node(carry)
            carry = 0
        
        curr = curr.next
    
    root = reverse(root)
    
    return root

def solve2(root: Node) -> Node:
    """ Recursive approach: tO(n) sO(n)"""
    def add(root: Node) -> int:
        if not root:
            return 1

        carry = add(root.next)
        
        total = root.val + carry
        
        root.val = total % 10
        
        return total // 10
    
    carry = add(root)
    
    if carry:
        new = Node(carry)
        new.next = root
        root = new
    
    return root
    
if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    ll.head = solve2(ll.head)
    print(ll)