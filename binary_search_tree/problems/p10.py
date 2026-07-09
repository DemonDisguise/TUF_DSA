# Two Sum in BST (Two Sum IV)
# Check if there exists a pair with sum K

from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST, BSTIterator


def solve(root: TreeNode | None, k: int) -> bool:
    lo_it = BSTIterator(root)
    hi_it = BSTIterator(root, reverse=True)

    lo_val = lo_it.next() if lo_it.has_next() else None
    hi_val = hi_it.next() if hi_it.has_next() else None
    
    while lo_val is not None and hi_val is not None and lo_val < hi_val:
        total = lo_val + hi_val
        if total == k:
            return True
        elif total < k:
            lo_val = lo_it.next() if lo_it.has_next() else None
        else:
            hi_val = hi_it.next() if hi_it.has_next() else None
    
    return False

if __name__ == "__main__":
    tree = BST.deserialize(input())
    k = int(input())
    print(solve(tree.root, k))

# 7 3 10 2 6 9 11 1 N 5 N 8 N N N N N 4 N
# 16   
