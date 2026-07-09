# LCA (Lowest Common ancestor) in BST

from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST

def solve(root: TreeNode | None, val1: int, val2: int) -> TreeNode | None:
    curr = root
    while curr is not None:
        if val1 < curr.val and val2 < curr.val:
            curr = curr.left
        elif val1 > curr.val and val2 > curr.val:
            curr = curr.right
        else:
            return curr
    return None

if __name__ == "__main__":
    tree = BST.deserialize(input())
    val1, val2 = map(int, input().split())
    print(solve(tree.root, val1, val2))

# 10 4 13 3 8 11 15 1 N 6 9 N N N N 1 N 5 7 N N N 2
# 5 9   