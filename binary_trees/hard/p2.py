# Lowest Common Ancestor for two given nodes
""" Given a root of binary tree, find the lowest common ancestor (LCA) of two given nodes (p, q) in the tree.

The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself). """

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode | None, p: TreeNode | None, q: TreeNode | None) -> TreeNode:
    if root is None or root == p or root == q:
        return root
    
    left = solve(root.left, p, q)
    right = solve(root.right, p, q)

    if left is None: return right
    elif right is None: return left
    else: return root
    
if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    p, q = (tree.find(i) for i in map(int, input().split()))
    print(solve(tree.root, p, q))

# 3 5 1 6 2 0 8 N N 7 4