from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeRightSideView:
    """
Problem: Binary Tree Right Side View
Difficulty: Medium
LeetCode: https://leetcode.com/problems/binary-tree-right-side-view/
Pattern: Tree / BFS (Level Order)
"""
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == size - 1:
                    result.append(node.val)

        return result