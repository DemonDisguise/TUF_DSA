# Zig Zag traversal of binary tree

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque

def solve(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    
    zigzag_traversal = []
    q = deque([root])
    flag = False
    
    while q:
        row = []
        for _ in range(len(q)):
            node = q.popleft()
            row.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        if flag:
            zigzag_traversal.append(row[::-1])
        else:
            zigzag_traversal.append(row)
        flag = not flag
    
    return zigzag_traversal     

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    for i in solve(tree.root):
        print(*i)
    