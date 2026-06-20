# Sort a linked list of 0's 1's and 2's

from lnkd_lst.ll import SLL, Node

def solve(root):
    zero_head = Node()
    one_head = Node()
    two_head = Node()
    
    zero, one, two = zero_head, one_head, two_head
    
    curr = root
    
    while curr:
        nxt = curr.next
        curr.next = None
        
        if curr.val == 0:
            zero.next = curr
            zero = zero.next
        elif curr.val == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next
            
        curr = nxt
    
    zero.next = one_head.next if one_head.next else two_head.next
    one.next = two_head.next
    
    return zero_head.next      

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(SLL(solve(ll.head)))