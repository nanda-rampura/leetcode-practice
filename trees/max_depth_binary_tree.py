from typing import Optional
from .tree_node import TreeNode

class MaxDepthBinaryTree:
    """
    Problem: Maximum Depth of Binary Tree
    Difficulty: Easy
    Pattern: DFS Iterative (Stack)
    """

    git_commit_message = "feat: compute max depth of binary tree using iterative DFS"

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        depth = 0

        while stack:
            node, current_depth = stack.pop()

            depth = max(depth, current_depth)

            if node.left:
                stack.append((node.left, current_depth + 1))

            if node.right:
                stack.append((node.right, current_depth + 1))

        return depth