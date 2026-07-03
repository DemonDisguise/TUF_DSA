# Find intersection of two linked lists

from lnkd_lst.ll import SLL

def solve(root1, root2):
    if not root1 or not root2: return None
    
    curr1, curr2 = root1, root2
    
    while curr1 is not curr2:
        curr1 = curr1.next if curr1 else root2
        curr2 = curr2.next if curr2 else root1
    
    return curr1

if __name__ == "__main__":
    ll1 = SLL(list(map(int, input().split())))
    ll2 = SLL(list(map(int, input().split())))

    r = input()
    if r == "ll1":
        ll2.attach_at_index(ll1, int(input()))
    else:
        ll1.attach_at_index(ll2, int(input()))
    
    print(solve(ll1.head, ll2.head))
    