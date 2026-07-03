# Binary Tree implementation

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
    
    def build(self, values: Iterable):
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
        """Returns (lines, width, height, root_x) for the subtree at `node`.
        root_x is the column of the node's own label within `lines`, so the
        caller can align connector branches to it.
        """
        if node is None:
            return [], 0, 0, 0
        
        label = str(node.val)
        
        if node.left is None and node.right is None:
            return [label], len(label), 1, len(label) // 2
        
        if node.right is None:
            left_lines, left_w, left_h, left_x = self._pprint_helper(node.left)
            first = (" " * (left_x + 1)) + label
            second = (" " * left_x) + "/" + (" " * (left_w - left_x - 1))
            lines = [first, second] + [l + " " * len(label) for l in left_lines]
            return lines, left_w + len(label), left_h + 2, left_w + len(label) // 2
        
        if node.left is None:
            right_lines, right_w, right_h, right_x = self._pprint_helper(node.right)
            first = label + (" " * right_x)
            second = (" " * (len(label) + right_x - 1)) + "\\" + (" " * (right_w - right_x))
            lines = [first, second] + [" " * len(label) + l for l in right_lines]
            return lines, right_w + len(label), right_h + 2, len(label) // 2
        
        left_lines, left_w, left_h, left_x = self._pprint_helper(node.left)
        right_lines, right_w, right_h, right_x = self._pprint_helper(node.right)
        
        first = (" " * (left_x + 1)) + label + (" " * right_x)
        second = (" " * left_x) + "/" + (" " * (left_w - left_x - 1 + len(label) + right_x)) + "\\" + (" " * (right_w - right_x - 1))
        
        if left_h < right_h:
            left_lines += [" " * left_w] * (right_h - left_h)
        elif right_h < left_h:
            right_lines += [" " * right_w] * (left_h - right_h)
        
        lines = [first, second] + [
            a + " " * len(label) + b for a, b in zip(left_lines, right_lines)
        ]
        return lines, left_w + len(label) + right_w, max(left_h, right_h) + 2, left_w + len(label) // 2

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    tree.pprint()
    print(tree)