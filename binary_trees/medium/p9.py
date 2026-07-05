# Right view of Binary Tree 
# The right view of the binary tree, arranged from top to bottom

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque


def solve(root: TreeNode | None) -> list[int]:
    rows = {}

    queue = deque([(root, 0)])

    while queue:
        node, row = queue.popleft()
        rows[row] = node.val
        if node.left is not None:
            queue.append((node.left, row + 1))
        if node.right is not None:
            queue.append((node.right, row + 1))
        
    return list(rows.values())
        
if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    # tree.pprint()
    print(*solve(tree.root))
    