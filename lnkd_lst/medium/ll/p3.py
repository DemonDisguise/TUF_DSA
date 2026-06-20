# Reverse a linked list - recursive

from lnkd_lst.ll import SLL

def solve(root):
    if not root.next or not root:
        return root
    
    new_head = solve(root.next)
    
    front = root.next
    front.next = root
    root.next = None
    
    return new_head

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(SLL(solve(ll.head)))