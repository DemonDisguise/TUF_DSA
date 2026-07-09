# Inorder Successor/Predecessor in BST

""" Given a Binary Search Tree and a 'key' value which represents the data data of a node in this tree. Return the inorder predecessor and successor of the given node in the BST.

The predecessor of a node in BST is that node that will be visited just before the given node in the inorder traversal of the tree. Return nullptr if the given node is the one that is visited first in the inorder traversal.
The successor of a node in BST is that node that will be visited immediately after the given node in the inorder traversal of the tree. Return nullptr if the given node is visited last in the inorder traversal. """


from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST

def solve(root: TreeNode | None, key: TreeNode | None) -> tuple[TreeNode | None]:
    if root is None or key is None: 
        return (None, None)
    
    def _predecessor(root: TreeNode | None, key: TreeNode) -> TreeNode | None:
        predecessor = None
        curr = root
        
        while curr is not None:
            if key.val <= curr.val:
                curr = curr.left
            else:
                predecessor = curr
                curr = curr.right
        
        return predecessor
    
    def _successor(root: TreeNode | None, key: TreeNode) -> TreeNode | None:
        successor = None
        curr = root
        
        while curr is not None:
            if key.val >= curr.val:
                curr = curr.right
            else:
                successor = curr
                curr = curr.left
        
        return successor

    return (_predecessor(root, key), _successor(root, key))

if __name__ == "__main__":
    tree = BST.deserialize(input())
    key = tree.find(int(input()))
    print(*solve(tree.root, key))

# 5 2 7 1 4 6 9 N N 3 N N N 8 10
# 3