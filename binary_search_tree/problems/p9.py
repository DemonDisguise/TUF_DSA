# Merge 2 BSTs

from binary_trees.binary_tree import TreeNode
from binary_search_tree.bst import BST, BSTIterator

def solve(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
    it1 = BSTIterator(root1)
    it2 = BSTIterator(root2)
    
    merged: list[int] = []
    while it1.has_next() and it2.has_next():
        if it1.peek() <= it2.peek():
            merged.append(it1.next())
        else:
            merged.append(it2.next())
    while it1.has_next():
        merged.append(it1.next())
    while it2.has_next():
        merged.append(it2.next())
    
    
    def build_balanced(arr: list[int]) -> TreeNode | None:
        if not arr: return None
        
        mid = len(arr) // 2
        node = TreeNode(arr[mid])
        node.left = build_balanced(arr[:mid])
        node.right = build_balanced(arr[mid + 1:])
        return node
    
    return build_balanced(merged)

if __name__ == "__main__":
    tree1 = BST.deserialize(input())
    tree2 = BST.deserialize(input())
    merged = BST(solve(tree1.root, tree2.root))
    merged.pprint()
    print(merged)

# 7 3 15 N N 9 20
# 8 5 10 3 6 N 29    