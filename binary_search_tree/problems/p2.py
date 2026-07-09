# Floor in BST
# Find the maximum value val which is val <= key

from binary_search_tree.bst import BST
from binary_trees.binary_tree import TreeNode

def solve(root: TreeNode | None, key: int) -> int:
    floor = -1
    curr = root
    while curr is not None:
        if root.val == key:
            floor = root.val
            return floor
        
        if key > root.val:
            floor = root.val
            root = root.right
        else:
            root = root.left
    return floor

if __name__ == "__main__":
    tree = BST.deserialize(input())
    key = int(input())
    tree.pprint()

# 10 5 13 3 6 11 14 2 4 N 9
# 8