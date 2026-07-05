# Symmetrical Binary Tree 
# Check if a Binary Tree is symmetric or not

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode | None) -> bool:
    def _walk(node1: TreeNode | None, node2: TreeNode | None) -> bool:
        if node1 is None or node2 is None:
            return node1==node2
        
        if node1.val != node2.val: return False
        return _walk(node1.left, node2.right) and _walk(node1.right, node2.left)
        
    return root is None or _walk(root.left, root.right)
        
if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    # tree.pprint()
    print(solve(tree.root))

# 1 2 2 3 4 4 3   