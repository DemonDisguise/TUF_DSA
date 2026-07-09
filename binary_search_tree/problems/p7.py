# Construct BST from preorder traversal

from binary_trees.binary_tree import TreeNode, BinaryTree

def solve(preorder: list[int]) -> TreeNode | None:
    ind = 0
    
    def _build(upper_bound: float) -> TreeNode | None:
        nonlocal ind
        if ind == len(preorder) or preorder[ind] > upper_bound:
            return None
        root = TreeNode(preorder[ind])
        ind += 1
        root.left = _build(root.val)
        root.right = _build(upper_bound)
        return root
    
    return _build(float('inf'))

if __name__ == "__main__":
    preorder = list(map(int, input().split()))
    bst = BinaryTree(solve(preorder))
    bst.pprint()
    print(bst)

# 8 5 1 7 10 12
    