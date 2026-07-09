# Recover BST, if two nodes swapped
"""
Swap can have 2 cases - check after getting inorder (BST's inorder is always sorted)

1. Swapped nodes are not adjacent
2. Swapped nodes are not adjacent
"""

from binary_trees.binary_tree import TreeNode, BinaryTree


def solve(root: TreeNode | None) -> None:
    first = middle = last = prev = None
    curr = root
    
    while curr:
        if curr.left is None:
            if prev and prev.val > curr.val:
                if first is None:
                    first = prev
                    middle = curr
                else:
                    last = curr
            
            prev = curr
            curr = curr.right
        else:
            pred = curr.left
            
            while pred.right and pred.right != curr:
                pred = pred.right
            
            if pred.right is None:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                
                if prev and prev.val > curr.val:
                    if first is None:
                        first = prev
                        middle = curr
                    else:
                        last = curr
                
                prev = curr
                curr = curr.right
    
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and middle:
        first.val, middle.val = middle.val, first.val

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    print(tree)
    tree.pprint()
    solve(tree.root)
    print(tree)
    tree.pprint()

# 2 1 4 N N 3 N