# Detect a cycle in a linked list
from lnkd_lst.ll import SLL

def solve(root):
    slow = fast = root
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    ll.make_cycle(int(input()))
    print(solve(ll.head))