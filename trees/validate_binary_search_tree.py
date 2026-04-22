from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ValidateBinarySearchTree:
    """
Problem: Validate Binary Search Tree
Difficulty: Medium
LeetCode: https://leetcode.com/problems/validate-binary-search-tree/
Pattern: BST / DFS (Range Validation)
"""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recursive(node, min_val, max_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (
                recursive(node.left, min_val, node.val)
                and recursive(node.right, node.val, max_val)
            )

        return recursive(root, float("-inf"), float("inf"))