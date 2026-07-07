# Flatten Binary Tree to Linked List
""" Given a Binary Tree, convert it to a Linked List where the linked list nodes follow the same order as the pre-order traversal of the binary tree.

Use the right pointer of the Binary Tree as the ‘next’ pointer for the linked list and set the left pointer to null. Do this in place and do not create extra nodes. """

from binary_trees.binary_tree import BinaryTree, TreeNode


def solve(root: TreeNode | None) -> None:
    curr = root
    
    while curr is not None:
        if curr.left is not None:
            prev = curr.left
            while prev.right is not None:
                prev = prev.right
            prev.right = curr.right
            curr.right = curr.left
        curr.left = None
        curr = curr.right

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    tree.pprint()
    print(tree)
    solve(tree.root)
    print(tree)
    tree.pprint()

# 1 2 5 3 4 N 6 N N N N 7 N