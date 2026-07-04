# Preorder, Postorder, Inorder traversal in one pass

from binary_trees.binary_tree import BinaryTree, TreeNode

def solve(root: TreeNode) -> list[list[int]]:
    stk = [(root, 1)]
    preorder_traversal = []
    inorder_traversal = []
    postorder_traversal = []

    while stk:
        node, num = stk.pop()

        if num == 1:
            preorder_traversal.append(node.val)
            num += 1
            stk.append((node, num))
            
            if node.left is not None:
                stk.append((node.left, 1))
        elif num == 2:
            inorder_traversal.append(node.val)
            num += 1
            stk.append((node, num))
            
            if node.right is not None:
                stk.append((node.right, 1))
        else:
            postorder_traversal.append(node.val)
    
    return [preorder_traversal, inorder_traversal, postorder_traversal]

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    tree.pprint()
    res = solve(tree.root)
    print(f"Preorder: {' '.join(map(str, res[0]))}")
    print(f"Inorder: {' '.join(map(str, res[1]))}")
    print(f"Postorder: {' '.join(map(str, res[2]))}")
