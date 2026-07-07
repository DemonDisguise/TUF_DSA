# Construct Binary Tree from Postorder and Inorder

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(postorder: list[int], inorder: list[int]) -> BinaryTree | None:
    inorder_index = {val: i for i, val in enumerate(inorder)}
    postorder_pos = len(postorder) - 1
    
    def build(in_left: int, in_right: int) -> TreeNode | None:
        nonlocal postorder_pos
        if in_left > in_right or postorder_pos < 0:
            return None
        
        root_val = postorder[postorder_pos]
        postorder_pos -= 1
        root = TreeNode(root_val)
        
        mid = inorder_index[root_val]
        
        root.right = build(mid + 1, in_right)
        root.left = build(in_left, mid - 1)
        
        return root

    return BinaryTree(build(0, len(inorder) - 1))

if __name__ == "__main__":
    postorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    tree = solve(postorder, inorder)
    print(tree)

# 5 6 4 9 2 3
# 5 4 6 3 2 9