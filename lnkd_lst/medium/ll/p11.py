# Sort a linked list

from lnkd_lst.ll import SLL, Node

def middle(root):
    slow = root
    fast = root.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(root1, root2):
    dummy = Node()
    temp = dummy
    
    while root1 and root2:
        if root1.val < root2.val:
            temp.next = root1
            root1 = root1.next
        else:
            temp.next = root2
            root2 = root2.next
        temp = temp.next
        
    if root1: temp.next = root1
    else: temp.next = root2
    
    return dummy.next

def solve(root: Node) -> Node:
    if not root or not root.next:
        return root
    
    mid = middle(root)
    l, r = root, mid.next
    mid.next = None
    
    l = solve(l)
    r = solve(r)   

    return merge(l, r)

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    print(SLL(ll.head))
