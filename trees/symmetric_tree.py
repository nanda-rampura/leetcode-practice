# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tests.test_kth_smallest_iterative import TreeNode


class Solution:
    """
Problem: Symmetric Tree
Difficulty: Easy
LeetCode: https://leetcode.com/problems/symmetric-tree/

Pattern: Binary Tree / DFS / Recursion

Approach:
- Compare the left and right subtrees recursively.
- Two trees are mirrors if:
  - Both nodes are null.
  - Their values are equal.
  - Left subtree of one matches right subtree of the other.
  - Right subtree of one matches left subtree of the other.

Time Complexity: O(n)
Space Complexity: O(h)
"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursive(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False

            return (
                recursive(left.left, right.right)
                and recursive(left.right, right.left)
            )

        if root is None:
            return True

        return recursive(root.left, root.right)