# Remove duplicates from sorted DLL

from lnkd_lst.dll import Node, DLL

def solve(root):
    if not root or not root.next:
        return root
    
    temp = root
    
    while temp and temp.next:
        if temp.val == temp.next.val:
            nxtNode = temp.next
            
            while nxtNode and temp.val == nxtNode.val:
                nxtNode = nxtNode.next
            
            temp.next = nxtNode
            if nxtNode:
                nxtNode.prev = temp
                   
        temp = temp.next
    
    return root

if __name__ == "__main__":
    dll = DLL(list(map(int, input().split())))
    dll.head = solve(dll.head)
    dll.set_tail()
    print(dll)