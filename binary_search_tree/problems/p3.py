# Delete a node in Binary Tree

from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST


def find_last_right(node: TreeNode) -> TreeNode:
    while node.right is not None:
        node = node.right
    return node

def helper(root: TreeNode) -> TreeNode:
    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    right = root.right
    last_right = find_last_right(root.left)
    last_right.right = right
    return root.left

def solve(root: TreeNode | None, key: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == key:
        return helper(root)

    original_root = root
    while root is not None:
        if root.val > key:
            if root.left is not None and root.left.val == key:
                root.left = helper(root.left)
                break
            else:
                root = root.left
        else:
            if root.right is not None and root.right.val == key:
                root.right = helper(root.right)
                break
            else:
                root = root.right
    
    return original_root

if __name__ == "__main__":
    tree = BST.deserialize(input())
    key = int(input())
    tree.pprint()
    BST(solve(tree.root, key)).pprint()

# 9 8 12 5 N 10 13 3 7 N 11 N N 2 4 6 8 1
# 5  