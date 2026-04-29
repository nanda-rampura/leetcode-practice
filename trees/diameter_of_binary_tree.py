# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from .tree_node import TreeNode


class DiameterOfBinaryTree:
    """
    Problem: Diameter of Binary Tree
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/
    Pattern: Tree DFS / Postorder Traversal
    Approach: Compute left/right height at each node and track max path through node
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def recursive(node) -> int:
            nonlocal diameter
            if not node:
               return 0
            left = recursive(node.left)
            right = recursive(node.right)

            diameter = max(diameter, left, right, left+right)
            return max(left,right) + 1

        recursive(root)
        return diameter