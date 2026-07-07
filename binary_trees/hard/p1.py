# Print root to leaf path in Binary Tree
""" Given a Binary Tree and a reference to a root belonging to it. Return the path from the root node to the given leaf node.
Note: No two nodes in the tree have the same data value and it is assured that the given node is present and a path always exists.
 """
from binary_trees.binary_tree import BinaryTree, TreeNode


def solve(root: TreeNode | None, node: int) -> list[int]:
    def _walk(root: TreeNode | None, end: int, path: list[int]) -> bool:
        if root is None:
            return False
        
        path.append(root.val)
        
        if root.val == end:
            return True
        
        if _walk(root.left, end, path) or _walk(root.right, end, path):
            return True
        
        path.pop()
        return False
        
    path = []
    if root is None: return path
    _walk(root, node, path)
    return path

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    node = int(input())
    # tree.pprint()
    print(*solve(tree.root, node))

# 1 2 3 4 5 N N N N 6 7  
# 7  