# Merge K sorted lists

from lnkd_lst.ll import Node, SLL
import sys
import heapq

def solve(arr: list[Node]) -> SLL:
    min_heap = []
    
    for i, node in enumerate(arr):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    dummy = Node()
    curr = dummy
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    
    return SLL(dummy.next)

if __name__ == "__main__":
    arr = [SLL(list(map(int, line.strip().split()))) for line in sys.stdin if line.strip()]

    heads = [sll.head for sll in arr]
    
    print(solve(heads))

    