# Top view of a binary tree
# The Top View of a Binary Tree is the set of nodes visible when we see the tree from the top.

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque

def solve(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    
    columns = {}
    queue = deque([(root, 0)])
    
    while queue:
        node, col = queue.popleft()
        if col not in columns:
            columns[col] = node.val
        if node.left is not None:
            queue.append((node.left, col - 1))
        if node.right is not None:
            queue.append((node.right, col + 1))
    
    result = []
    for col in sorted(columns.keys()):
        result.append(columns[col])
    return result
        
if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    # tree.pprint()
    print(*solve(tree.root))

# 1 2 3 4 10 9 11 N 5 N N N N N N N 6