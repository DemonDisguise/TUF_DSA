# Middle of the linked list

from lnkd_lst.ll import SLL

def solve(root):
    slow = fast = root

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
        
if __name__ == "__main__":
    root = SLL(list(map(int, input().split())))
    s = solve(root.head)
    print(s.val)