from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestorBST:
    """
Problem: Lowest Common Ancestor of a BST
Difficulty: Medium
LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Pattern: BST / Tree Traversal
"""
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root