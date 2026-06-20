# Remove the nth node from the back of the ll

from lnkd_lst.ll import SLL, Node

def solve(root, n):
    if not root:
        return None
    
    dummy = Node()
    dummy.next = root
    
    slow = fast = dummy
    
    for _ in range(n + 1):
        fast = fast.next
    
    while fast :
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    
    return dummy.next

if __name__ == "__main__":
    ll = SLL(list(map(int, input().split())))
    n = int(input())
    print(SLL(solve(ll.head, n)))
    