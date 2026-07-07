# Binary Search Tree Implementation

from collections.abc import Iterable
from binary_trees.binary_tree import BinaryTree, TreeNode

class BST(BinaryTree):
    """A Binary Search Tree — same structure as BinaryTree, plus the
    invariant: for every node, left subtree < node.val < right subtree."""
    
    def build(self, values: Iterable) -> None:
        """Overridden: BST needs ordered insertion, not level-order placement,
        or the BST property wouldn't hold at all."""
        self.root = None
        for val in values:
            if val is not None:
                self.insert(val)
    
    def insert(self, val: int) -> None:
        def _insert(node: TreeNode | None, val: int) -> TreeNode:
            if node is None:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)
    
    def find(self, value: int) -> TreeNode | None:
        """Overridden: O(h), not O(n) — exploit the BST property directly
        instead of searching both subtrees like the plain-tree version."""
        curr = self.root
        while curr is not None:
            if value == curr.val:
                return curr
            curr = curr.left if value < curr.val else curr.right
        return None


if __name__ == "__main__":
    # --- BST sanity checks ---
    bst = BST([5, 1, 9, 3, 7, 2, 8])

    assert isinstance(bst.root, TreeNode), "BST did not build a root"
    assert bst.root.val == 5, f"BST root should be 5, got {bst.root.val}"

    assert bst.inorder() == [1, 2, 3, 5, 7, 8, 9], f"BST inorder should be sorted: {bst.inorder()}"


    level_order_bt = BinaryTree([5, 1, 9, 3, 7, 2, 8])
    assert level_order_bt.inorder() != bst.inorder(), (
        "BST.build() does not appear to differ from BinaryTree.build() — "
        "override may not be taking effect"
    )

    found = bst.find(7)
    assert found is not None and found.val == 7, "BST.find failed to locate existing value"
    assert bst.find(999) is None, "BST.find should return None for missing value"

    assert bst.height() == 3, f"BST height failed: {bst.height()}"
    assert bst.count_nodes() == 7, f"BST count_nodes failed: {bst.count_nodes()}"
    assert bst.is_balanced() is False, (
        f"BST is_balanced should be False for this insertion order, "
        f"got {bst.is_balanced()} — this tree is a real example of how "
        f"plain BST insertion gives no balance guarantee at all"
    )

    bst.insert(6)
    assert bst.inorder() == [1, 2, 3, 5, 6, 7, 8, 9], f"BST insert broke ordering: {bst.inorder()}"
    assert bst.find(6) is not None, "BST.find failed to locate freshly inserted value"

    print("BST: all checks passed.")