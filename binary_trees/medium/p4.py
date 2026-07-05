# Boundary traversal of binary tree
"""
Anticlockwise
Left Boundary excluding leaf -> leaf nodes -> Right boundary in reverse excluding leaf
Clockwise
Right Boundary excluding leaf -> leaf nodes in reverse -> Left boundary in reverse excluding leaf
"""

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque

def is_leaf(node: TreeNode | None) -> bool:
    return node is not None and node.left is None and node.right is None

def left_edge(node: TreeNode | None) -> list[int]:
    """Non-leaf nodes walking down the left spine, root's left child first."""
    edge = []
    curr = node
    while curr is not None and not is_leaf(curr):
        edge.append(curr.val)
        curr = curr.left if curr.left is not None else curr.right
    return edge

def right_edge(node: TreeNode | None) -> list[int]:
    """Non-leaf nodes walking down the right spine, root's right child first."""
    edge = []
    curr = node
    while curr is not None and not is_leaf(curr):
        edge.append(curr.val)
        curr = curr.right if curr.right is not None else curr.left
    return edge

def leaves(node: TreeNode | None) -> list[int]:
    """All leaves, left to right."""
    if node is None:
        return []
    if is_leaf(node):
        return [node.val]
    return leaves(node.left) + leaves(node.right)

def solve(root: TreeNode | None, direction: str) -> list[int]:
    if root is None:
        return []
    if is_leaf(root):
        return [root.val]
    
    ring = (
        [root.val]
        + left_edge(root.left)
        + leaves(root)
        + right_edge(root.right)[::-1]
    )
    
    if direction == "c":
        return [ring[0]] + ring[1:][::-1]
    return ring

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    direction = input() # c or ac
    tree.pprint()
    print(solve(tree.root, direction))

# 1 2 7 3 N N 8 N 4 9 N 5 6 10 11
# ac