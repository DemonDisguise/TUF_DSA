# Ceil in BST
# Find the minimum value val which is val >= key

from binary_search_tree.bst import BST
from binary_trees.binary_tree import TreeNode

def solve(root: TreeNode | None, key: int) -> int:
    ceil = -1
    curr = root
    while curr is not None:
        if curr.val == key:
            ceil = curr.val
            return ceil

        if key > curr.val:
            curr = curr.right
        else:
            ceil = curr.val
            curr = curr.left
    
    return ceil 

if __name__ == "__main__":
    tree = BST.deserialize(input())
    key = int(input())
    tree.pprint()

# 10 5 13 3 6 11 14 2 4 N 9
# 8