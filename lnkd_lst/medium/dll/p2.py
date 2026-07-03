# Find pairs with given sum in doubly linked list

from lnkd_lst.dll import DLL

def solve(root, sm):
    if not root and not root.next:
        return []
    
    curr = root
    
    while curr.next:
        curr = curr.next
    
    tail = curr
    
    l, r = root, tail
    res = []
    
    while l != r and r.next != l:
        total = l.val + r.val
        
        if total > sm:
            r = r.prev
        elif total < sm:
            l = l.next
        else:
            res.append((l.val, r.val))
            l = l.next
            r = r.prev
    
    return res

if __name__ == "__main__":
    dll = DLL(list(map(int, input().split())))
    sum = int(input())
    res = solve(dll.head, sum)
    for pair in res:
        print(*pair)
        