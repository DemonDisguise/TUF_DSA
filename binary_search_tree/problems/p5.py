# Validate a BST

from binary_trees.binary_tree import BinaryTree, TreeNode


def solve(root: TreeNode | None) -> bool:
    def _helper(root: TreeNode | None, left_range: float, right_range: float) -> bool:
        if root is None:
            return True
        
        if not (left_range < root.val < right_range):
            return False
        
        return _helper(root.left, left_range, root.val) and _helper(root.right, root.val, right_range)
    
    return _helper(root, float('-inf'), float('inf'))          

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    print(solve(tree.root))

# 5 1 6 N N 4 8
# 13 10 15 7 12 14 17 N 9 N N N N 16 N 8 N