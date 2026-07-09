# Find max or min in BST

from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST

def solve1(root: TreeNode | None) -> int:
    if root is None:
        return -1
    
    curr = root  
    while curr.right:
        curr = curr.right
    
    return curr.val

def solve2(root: TreeNode | None) -> int:
    if root is None:
        return -1
    
    curr = root
    while curr.left:
        curr = curr.left
    
    return curr.val

if __name__ == "__main__":
    tree = BST.deserialize(input())
    o = input() # "max" or "min"
    if o == "max":
        print(solve1(tree.root))
    else:
        print(solve2(tree.root))

# 10 5 13 3 6 11 14 2 4 N 9
# max        