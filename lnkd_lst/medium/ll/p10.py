# Delete the middle node of the linked list

from lnkd_lst.ll import SLL, Node

def solve(root: Node) -> Node:
    if not root or not root.next:
        return root
    
    dummy = Node()
    dummy.next = root
    slow = dummy
    fast = dummy.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    slow.next = slow.next.next

    return dummy.next

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(SLL(solve(ll.head)))
    