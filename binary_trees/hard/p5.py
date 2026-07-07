# Print all the nodes at a distance of k in binary tree

from binary_trees.binary_tree import BinaryTree, TreeNode
from collections import deque

def _build_parent_map(root: TreeNode) -> dict[TreeNode, TreeNode | None]:
    parent = {root: None}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in (node.left, node.right):
            if child is not None:
                parent[child] = node
                queue.append(child)
    return parent

def solve(root: TreeNode | None, target: int, k: int) -> list[int]:
    if root is None or target is None:
        return []
    
    parent = _build_parent_map(root)

    visited = {target}
    queue = deque([target])
    distance = 0
    
    while queue and distance < k:
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in (node.left, node.right, parent[node]):
                if neighbour is not None and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        distance += 1
    
    return [node.val for node in queue]

if __name__ == "__main__":
    tree = BinaryTree.deserialize(input())
    target, k = map(int, input().split())
    print(*solve(tree.root, tree.find(target), k))

# 3 5 1 6 2 0 8 N N 7 4
