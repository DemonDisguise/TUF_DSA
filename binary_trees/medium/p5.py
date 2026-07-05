# Vertical order traversal

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import defaultdict, deque

def solve(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    
    columns: dict[int, dict[int, list[int]]] = defaultdict(lambda: defaultdict(list))

    queue = deque([(root, 0, 0)])
    
    while queue: 
        node, col, row = queue.popleft()
        columns[col][row].append(node.val)
        if node.left is not None:
            queue.append((node.left, col - 1, row + 1))
        if node.right is not None:
            queue.append((node.right, col + 1, row + 1))
    
    result = []
    for col in sorted(columns.keys()):
        rows = columns[col]
        col_values = []
        for row in sorted(rows.keys()):
            col_values.extend(sorted(rows[row]))
        result.append(col_values)
    
    return result
    
if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    for i in solve(tree.root):
        print(*i)

# 1 2 3 4 10 9 10 N 5 N N N N N N N 6
