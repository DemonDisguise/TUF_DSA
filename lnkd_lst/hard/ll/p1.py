# Reverse Linked List in groups of size k

from lnkd_lst.ll import SLL, Node

def solve(root, k):
    def reverse(root):
        prev = None
        curr = root
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    def get_kth_node(root, k):
        curr = root
        
        while curr.next and k > 1:
            curr = curr.next
            k -= 1
        
        return curr
    
    dummy = Node()
    dummy.next = root
    curr = root
    prev = dummy
    
    while curr:
        kth = get_kth_node(curr, k)
        nxt = kth.next
        kth.next = None
        
        kth = reverse(prev.next)
        
        prev.next = kth
        curr.next = nxt
        prev = curr
        curr = curr.next 
    
    return dummy.next       
        
if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    k = int(input())
    ll.head = solve(ll.head, k)
    print(ll)