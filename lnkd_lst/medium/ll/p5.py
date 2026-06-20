# Starting point of loop in linked list

from lnkd_lst.ll import SLL

def solve(root):
    slow = fast = root
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None
    
    slow = root
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    ll.make_cycle(2)
    print(solve(ll.head))