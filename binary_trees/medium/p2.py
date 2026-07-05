# Check if two trees are identical or not

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def _walk(node1: TreeNode | None, node2: TreeNode | None) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None or node1.val != node2.val:
            return False
            
        return _walk(node1.left, node2.left) and _walk(node1.right, node2.right)

    return _walk(root1, root2)

if __name__ == "__main__":
    tree1 = BinaryTree.deserialize(input())
    tree2 = BinaryTree.deserialize(input())
    print(solve(tree1.root, tree2.root))

# 1 2 3 N N 4 5
# 1 2 3 N N 4 N    