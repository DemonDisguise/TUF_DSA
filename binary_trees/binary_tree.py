# Binary Tree implementation

from __future__ import annotations
from collections.abc import Iterable
from collections import deque

class TreeNode:
    """Represents a node in a binary tree."""
    __slots__ = ("val", "left", "right")
    
    def __init__(self, val: int, left: TreeNode | None=None, right: TreeNode | None=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right
    
    def __repr__(self):
        return f"{self.val}"
    
    __str__ = __repr__

class BinaryTree:
    """A data structure where each node has at most two children.

    This class represents a hierarchical collection of nodes. Each node 
    stores a value and references to its left and right child nodes. 
    It enables fast searching, sorting, and data organization.
    """
    
    def __init__(
        self,
        values: TreeNode | Iterable | None = None
    ): 
        if values is None:
            self.root = None
        elif isinstance(values, TreeNode):
            self.root = values
        else:
            self.root = None
            self.build(values)
    
    def __bool__(self):
        return self.root is not None
    
    def __repr__(self):
        return self.serialize()
    
    __str__ = __repr__
    
    def build(self, values: Iterable):
        """Build the binary tree from the given Iterable"""
        if not values:
            self.root = None
            return 
        
        iterator = iter(values)

        root_val = next(iterator)
        
        if root_val is None:
            self.root = None
            return
        
        self.root = TreeNode(root_val)
        
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            
            try:
                left = next(iterator)
                if left is not None:
                    node.left = TreeNode(left)
                    queue.append(node.left)
                
                right = next(iterator)
                if right is not None:
                    node.right = TreeNode(right)
                    queue.append(node.right)
            except StopIteration:
                break
    
    @classmethod
    def deserialize(cls, s: str) -> "BinaryTree":
        """Build a tree from a level-order string like '1 2 3 N 4 N N'."""
        tokens = s.split()
        arr = [
            None if tok.lower() in ("n", "none", "null") else int(tok)
            for tok in tokens
        ]
        return cls(arr)

    def serialize(self) -> str:
        """Level-order string, opposite of deserialize. 'N' marks absent children."""
        if not self.root:
            return ""
        
        out = [str(self.root.val)]
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            for child in (node.left, node.right):
                if child is not None:
                    out.append(str(child.val))
                    queue.append(child)
                else:
                    out.append("N")
        
        return " ".join(out)

    def pprint(self) -> None:
        """Print the tree with ASCII branches."""
        if not self.root:
            print("(empty)")
            return
        lines, _, _, _ = self._pprint_helper(self.root)
        print("\n".join(lines))

    def _pprint_helper(self, node: TreeNode | None):
        """
        Recursively builds the tree layout from the bottom up.
        Returns:
            - lines: List of strings representing the visual rows of the subtree.
            - width: Total width of the subtree block.
            - height: Total height of the subtree block.
            - middle: The column index where this node's label centers.
        """
        # Base Case: Leaf Node
        if node.left is None and node.right is None:
            line = str(node.val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Case 1: Only Left Child
        if node.right is None:
            lines, w, h, x = self._pprint_helper(node.left)
            s = str(node.val)
            u = len(s)
            first_line = (x + 1) * ' ' + (w - x - 1) * ' ' + s
            second_line = x * ' ' + '/' + (w - x - 1) * ' ' + u * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, w + u, h + 2, w + u // 2

        # Case 2: Only Right Child
        if node.left is None:
            lines, w, h, x = self._pprint_helper(node.right)
            s = str(node.val)
            u = len(s)
            first_line = s + x * ' ' + (w - x) * ' '
            second_line = u * ' ' + x * ' ' + '\\' + (w - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, w + u, h + 2, u // 2

        # Case 3: Two Children
        left_lines, left_w, left_h, left_x = self._pprint_helper(node.left)
        right_lines, right_w, right_h, right_x = self._pprint_helper(node.right)
        s = str(node.val)
        u = len(s)
        
        # Establish root and branch row tracking
        first_line = (left_x + 1) * ' ' + (left_w - left_x - 1) * ' ' + s + right_x * ' ' + (right_w - right_x) * ' '
        second_line = left_x * ' ' + '/' + (left_w - left_x - 1 + u + right_x) * ' ' + '\\' + (right_w - right_x - 1) * ' '
        
        # Vertically pad the shorter subtree block so they zip together cleanly
        if left_h < right_h:
            left_lines += [left_w * ' '] * (right_h - left_h)
        elif right_h < left_h:
            right_lines += [right_w * ' '] * (left_h - right_h)
            
        zipped_lines = [a + u * ' ' + b for a, b in zip(left_lines, right_lines)]
        return [first_line, second_line] + zipped_lines, left_w + right_w + u, max(left_h, right_h) + 2, left_w + u // 2
    
    def preorder(self) -> list[int]:
        """Root, Left, Right"""
        preorder_traversal = []
        
        def _walk(node: TreeNode | None) -> None:
            if node is None:
                return
            preorder_traversal.append(node.val)
            _walk(node.left)
            _walk(node.right)
        
        _walk(self.root)
        return preorder_traversal

    def inorder(self) -> list[int]:
        """Left, Root, Right"""
        inorder_traversal = []
        
        def _walk(node: TreeNode | None) -> None:
            if not node:
                return
            _walk(node.left)
            inorder_traversal.append(node.val)
            _walk(node.right)
        
        _walk(self.root)
        return inorder_traversal

    def postorder(self) -> list[int]:
        """Left, Right, Root"""
        postorder_traversal = []
        
        def _walk(node: TreeNode | None) -> None:
            if not node:
                return
            _walk(node.left)
            _walk(node.right)
            postorder_traversal.append(node.val)
        
        _walk(self.root)
        return postorder_traversal
    
    def preorder_iter(self) -> list[int]:
        """Root, Left, Right"""
        if self.root is None:
            return []
        
        preorder_traversal = []
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            preorder_traversal.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            
        return preorder_traversal

    def inorder_iter(self) -> list[int]:
        """Left, Root, Right"""
        inorder_traversal = []
        stack = []
        node = self.root
        
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            inorder_traversal.append(node.val)
            node = node.right
        
        return inorder_traversal  
    
    def postorder_iter(self) -> list[int]:
        """Left, Right, Root"""
        if not self.root:
            return []
        postorder_traversal = []  
        stack = [self.root]
        last_visited = None
        
        while stack:
            node = stack[-1]
            
            if (node.left is None and node.right is None) or (last_visited is not None and last_visited in (node.left, node.right)):
                postorder_traversal.append(node.val)
                stack.pop()
                last_visited = node
            else:
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
        
        return postorder_traversal  
    
    def levelorder(self) -> list[int]:
        """Top to bottom, left to right, level by level"""      

        if self.root is None:
            return []
        
        levelorder_traversal = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            levelorder_traversal.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return levelorder_traversal
    
    def height(self) -> int:
        """Number of edges on the longest root-to-leaf path. Empty tree: -1"""

        def _walk(node: TreeNode | None) -> int:
            if node is None:
                return -1
            return 1 + max(_walk(node.left), _walk(node.right))
        
        return _walk(self.root)
    
    def count_nodes(self) -> int:
        """Total number of nodes in the tree"""
        def _count(node: TreeNode | None) -> int:
            if node is None:
                return 0
            
            return 1 + _count(node.left) + _count(node.right)
        return _count(self.root)
    
    def count_leaves(self) -> int:
        """Number of nodes with no children"""
        def _count(node: TreeNode | None) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return _count(node.left) + _count(node.right)

        return _count(self.root)
    
    def find(self, value: int) -> TreeNode | None:
        """Finds the node with the value in the tree"""
        def _search(node: TreeNode | None):
            if node is None: 
                return None
            if node.val == value:
                return node
            left = _search(node.left)
            if left:
                return left
            return _search(node.right)
        return _search(self.root)
    
    def is_balanced(self) -> bool:
        """Checks if the tree is balanced tree"""

        def _check(node: TreeNode | None) -> tuple[bool, int]:
            if node is None:
                return True, -1
            
            left_balanced, left_h = _check(node.left)
            if not left_balanced:
                return False, 0
            
            right_balanced, right_h = _check(node.right)
            if not right_balanced:
                return False, 0
            
            balanced = abs(left_h - right_h) <= 1
            height = 1 + max(left_h, right_h)
            return balanced, height
        
        is_bal, _ = _check(self.root)
        return is_bal
    
    def diameter(self) -> int:
        """Longest path between any two nodes, measured in edges."""
        best = 0
        
        def _height(node: TreeNode | None) -> int:
            nonlocal best
            if node is None:
                return -1
            
            left_h = _height(node.left)
            right_h = _height(node.right)
            
            best = max(best, left_h + right_h + 2)
            return 1 + max(left_h, right_h)
        
        _height(self.root)
        return best
        
if __name__ == "__main__":
    # --- BinaryTree sanity checks ---
    bt = BinaryTree.deserialize("3 9 20 N N 15 7")

    assert bt.preorder() == [3, 9, 20, 15, 7], f"preorder failed: {bt.preorder()}"
    assert bt.inorder() == [9, 3, 15, 20, 7], f"inorder failed: {bt.inorder()}"
    assert bt.postorder() == [9, 15, 7, 20, 3], f"postorder failed: {bt.postorder()}"
    assert bt.levelorder() == [3, 9, 20, 15, 7], f"levelorder failed: {bt.levelorder()}"

    assert bt.preorder() == bt.preorder_iter(), "preorder vs preorder_iter mismatch"
    assert bt.inorder() == bt.inorder_iter(), "inorder vs inorder_iter mismatch"
    assert bt.postorder() == bt.postorder_iter(), "postorder vs postorder_iter mismatch"

    assert bt.height() == 2, f"height failed: {bt.height()}"         
    assert bt.count_nodes() == 5, f"count_nodes failed: {bt.count_nodes()}"
    assert bt.count_leaves() == 3, f"count_leaves failed: {bt.count_leaves()}"
    assert bt.is_balanced() is True, f"is_balanced failed: {bt.is_balanced()}"  
    assert bt.diameter() == 3, f"diameter failed: {bt.diameter()}"

    assert bt.find(15) is not None and bt.find(15).val == 15, "find failed to locate existing value"
    assert bt.find(100) is None, "find should return None for missing value"


    round_trip = BinaryTree.deserialize(bt.serialize())
    assert round_trip.levelorder() == bt.levelorder(), "serialize/deserialize round trip failed"
    assert round_trip.preorder() == bt.preorder(), "serialize/deserialize round trip failed (preorder check)"

    empty = BinaryTree()
    assert bool(empty) is False, "__bool__ failed on empty tree"
    assert bool(bt) is True, "__bool__ failed on non-empty tree"
    assert empty.preorder() == [], "preorder on empty tree should be []"
    assert empty.height() == -1, f"height on empty tree should be -1, got {empty.height()}"

    print("BinaryTree: all checks passed.")
    