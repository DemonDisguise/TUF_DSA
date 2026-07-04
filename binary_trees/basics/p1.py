# Iterative Post order using two stacks

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode) -> list[int]:
    stk1 = [root]
    stk2 = []
    postorder_traversal = []
    
    if root is None:
        return []
    
    while stk1:
        node = stk1.pop()
        stk2.append(node)
        if node.left: stk1.append(node.left)
        if node.right: stk1.append(node.right)

    while stk2:
        postorder_traversal.append(stk2.pop().val)
    
    return postorder_traversal

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    print(*solve(tree.root))
    