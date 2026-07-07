# Construct Binary Tree from Preorder and Inorder

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(preorder: list[int], inorder: list[int]) -> BinaryTree | None:
    inorder_index = {val: i for i, val in enumerate(inorder)}
    preorder_pos = 0
    
    def build(in_left: int, in_right: int) -> TreeNode | None:
        nonlocal preorder_pos
        if in_left > in_right:
            return None
        
        root_val = preorder[preorder_pos]
        preorder_pos += 1
        root = TreeNode(root_val)

        mid = inorder_index[root_val]

        root.left = build(in_left, mid - 1)
        root.right = build(mid + 1, in_right)

        return root

    return BinaryTree(build(0, len(inorder) - 1))

if __name__ == "__main__":
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    tree = solve(preorder, inorder)
    print(tree)

# 3 4 5 6 2 9
# 5 4 6 3 2 9