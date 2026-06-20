# Add two numbers represented as Linked Lists in reverse
# 243 is stored in linked list as 3 -> 4 -> 2 -> None

from lnkd_lst.ll import SLL, Node

def solve(root1: Node, root2: Node) -> Node:
    dummy = Node()
    temp = dummy
    curr1, curr2 = root1, root2
    carry = 0
    
    while curr1 or curr2 or carry:
        val1 = curr1.val if curr1 else 0
        val2 = curr2.val if curr2 else 0
        
        total = val1 + val2 + carry
        
        temp.next = Node(total % 10)
        temp = temp.next
        
        carry = total // 10
        
        if curr1: curr1.next
        if curr2: curr2.next
        
    return dummy.next

if __name__ == "__main__":
    ll1 = SLL(list(map(int, input().split())))
    ll2 = SLL(list(map(int, input().split())))
    print(SLL(solve(ll1.head, ll2.head)))