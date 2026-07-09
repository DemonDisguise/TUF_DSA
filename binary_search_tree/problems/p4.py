# Kth largest and smallest element in Binary Search Tree

""" Given the root node of a binary search tree (BST) and an integer k.
Return the kth smallest and largest value (1-indexed) of all values of the nodes in the tree.

Return the 1st integer as kth smallest and 2nd integer as kth largest in the returned array. """

from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST

def solve(root: TreeNode | None, k: int) -> list[int]:
    def kth_smallest(k: int) -> int | None:
        stack = []
        curr = root
        count = 0
        while stack or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
        return None
    
    def kth_largest(k: int) -> int | None:
        stack = []
        curr = root
        count = 0
        while stack or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.left
        return None
    
    return [kth_smallest(k), kth_largest(k)]

if __name__ == "__main__":
    tree = BST.deserialize(input())
    k = int(input())
    print(*solve(tree.root, k))

# 3 1 4 N 2
# 1