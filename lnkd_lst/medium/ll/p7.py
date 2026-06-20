# Check if the given linked list is palindrome

from lnkd_lst.ll import SLL, Node

def reverse(root):
    prev = None
    curr = root
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

def solve(root: Node) -> bool:
    if not root or not root.next:
        return True
    
    slow = fast = root
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    h = reverse(slow.next if fast else slow)
    l, r = root, h
    res = True
    
    while r:
        if l.val != r.val:
            res = False
            break
        l = l.next
        r = r.next
    
    reverse(h)
    
    return res

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(solve(ll.head))