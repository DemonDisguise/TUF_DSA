# Children sum property in Binary Tree
""" Given a Binary Tree, convert the value of its nodes to follow the Children Sum Property. 
The Children Sum Property in a binary tree states that for every node, the sum of its children's values (if they exist) should be equal to the node's value. If a child is missing, it is considered as having a value of 0.
Note:
The node values can be increased by any positive integer any number of times, but decrementing any node value is not allowed.
A value for a NULL node can be assumed as 0.
We cannot change the structure of the given binary tree. """

from binary_trees.binary_tree import BinaryTree, TreeNode


def solve(root: TreeNode | None) -> None:
    if root is None:
        return 
    
    child = 0
    if root.left is not None:
        child += root.left.val
    if root.right is not None:
        child += root.right.val
    
    if child >= root.val: root.val = child
    else:
        if root.left is not None:
            root.left.val = root.val
        elif root.right is not None:
            root.right.val = root.val
    
    solve(root.left)
    solve(root.right)

    tot = 0
    if root.left is not None: tot += root.left.val
    if root.right is not None: tot += root.right.val
    if root.left is not None or root.right is not None: root.val = tot

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    solve(tree.root)
    print(tree.serialize())