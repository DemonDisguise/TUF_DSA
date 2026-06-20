# Length of loop in Linked List

from lnkd_lst.ll import SLL

def solve(root):
    slow = fast = root 
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return 0
    
    fast = fast.next
    lngth = 1
    
    while slow != fast:
        fast = fast.next
        lngth += 1
    
    return lngth

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    # ll.make_cycle(2)
    print(solve(ll.head))