# Largest BST in Binary Tree

from binary_trees.binary_tree import TreeNode, BinaryTree
from dataclasses import dataclass

@dataclass
class Stats:
    is_bst: bool
    size: int
    min_val: float
    max_val: float

def solve(root: TreeNode | None) -> tuple[TreeNode | None, int]:
    best_size = 0
    best_root: TreeNode | None = None
    
    def _walk(node: TreeNode | None) -> Stats:
        nonlocal best_root, best_size
        
        if node is None:
            return Stats(is_bst=True, size=0, min_val=float('inf'), max_val=float('-inf'))

        left = _walk(node.left)
        right = _walk(node.right)
        
        if (left.is_bst and right.is_bst and left.max_val < node.val < right.min_val):
            size = left.size + right.size + 1
            if size > best_size:
                best_size = size
                best_root = node
            return Stats(is_bst=True, size=size, min_val=min(left.min_val, node.val), max_val=max(right.max_val, node.val))

        return Stats(is_bst=False, size=0, min_val=float('-inf'), max_val=float('inf'))
    
    _walk(root)
    return best_root, best_size

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    res_root, size = solve(tree.root)
    res_tree = BinaryTree(res_root)
    print(res_tree)
    res_tree.pprint()
    print(size)
    