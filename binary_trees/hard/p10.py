# Morris Inorder Traversal of Binary Tree
# Morris Inorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure. The algorithm should efficiently visit each node in the binary tree in preorder sequence, printing or processing the node values as it traverses, without using a stack or recursion.

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode | None) -> list[int]:
    inorder_traversal = []
    curr: TreeNode | None = root
    
    while curr is not None:
        if curr.left is None:
            inorder_traversal.append(curr.val)
            curr = curr.right
        else:
            prev: TreeNode | None = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                inorder_traversal.append(curr.val)
                curr = curr.right
    return inorder_traversal

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    # tree.pprint()
    print(*solve(tree.root))
    