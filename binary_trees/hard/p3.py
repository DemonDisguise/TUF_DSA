# Maximum width of Binary Tree
""" Given a Binary Tree, return its maximum width. The maximum width of a Binary Tree is the maximum diameter among all its levels. The width or diameter of a level is the number of nodes between the leftmost and rightmost nodes. """

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque

def solve(root: TreeNode | None) -> int:
    if root is None:
        return 0
    
    max_width = 0
    queue = deque([(root, 0)])

    while queue:
        level_size = len(queue)
        _, first_col = queue[0]
        _, last_col = queue[-1]
        max_width = max(max_width, last_col - first_col + 1)

        for _ in range(level_size):
            node, col = queue.popleft()
            if node.left is not None:
                queue.append((node.left, 2 * col))
            if node.right is not None:
                queue.append((node.right, 2 * col + 1))
        
    return max_width

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    # tree.pprint()
    print(solve(tree.root))

# 1 3 2 5 3 N 9  