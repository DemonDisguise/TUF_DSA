# Reverse a linked list

from lnkd_lst.ll import SLL

def solve(root):
    prev = None
    curr = root 
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(SLL(solve(ll.head)))
    