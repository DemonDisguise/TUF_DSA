# Maximum sum path in binary tree

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode | None) -> int:
    best = float('-inf')
    def _path(node: TreeNode | None) -> int:
        nonlocal best
        if node is None:
            return 0
        
        left_sum = max(_path(node.left), 0)
        right_sum = max(_path(node.right), 0)
        
        best = max(best, node.val + left_sum + right_sum)
        
        return max(left_sum, right_sum) + node.val

    _path(root)
    return best

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    print(solve(tree.root))

# 2 -1
