# Reverse a Doubly Linked list

from lnkd_lst.dll import DLL, Node

def solve(root):
    if not root or not root.next:
        return root
    
    temp = None
    current = root
    
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    
    if temp:
        root = temp.prev
    
    return root
        

if __name__ == "__main__":
    dll = DLL(list(map(int, input().split())))
    dll.head = solve(dll.head)
    dll.set_tail()
    print(dll)