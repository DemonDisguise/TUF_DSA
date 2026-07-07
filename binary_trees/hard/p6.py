# # Minimum time taken to burn the Binary Tree from a Node
""" Given a target node data and a root of binary tree. If the target is set on fire, determine the shortest amount of time needed to burn the entire binary tree. 
It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent. """

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque

def _build_parent_map(root: TreeNode | None) -> dict[TreeNode, TreeNode | None]:
    parent = {root: None}
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        for child in (node.left, node.right):
            if child is not None:
                parent[child] = node
                queue.append(child)
    
    return parent

def solve(root: TreeNode | None, target: TreeNode | None) -> int:
    if root is None or target is None:
        return 0
    
    parent = _build_parent_map(root)

    visited = {target}
    queue = deque([target])
    time = 0
    
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in (node.left, node.right, parent[node]):
                if neighbour is not None and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        time += 1
    
    return time

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    target = tree.find(int(input()))
    print(solve(tree.root, target))

# 1 2 3 4 N 5 6 N 7
# 1