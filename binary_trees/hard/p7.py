# Count total nodes in a complete Binary Tree

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode | None) -> int:
    if root is None:
        return 0
    
    def left_height(node: TreeNode | None) -> int:
        h = 0
        while node is not None:
            h += 1
            node = node.left
        return h
    
    def right_height(node: TreeNode | None) -> int:
        h = 0
        while node is not None:
            h += 1
            node = node.right
        return h
    
    lh = left_height(root)
    rh = right_height(root)

    if lh == rh: return (1 << lh) - 1
    
    return 1 + solve(root.left) + solve(root.right)

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    print(solve(tree.root))
