# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from tests.test_lowest_common_ancestor import TreeNode


class BinaryTreeBuilder:
    """
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
LeetCode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Pattern: Binary Tree / Recursion / Divide and Conquer
Topics: Hash Map, Tree Construction, Recursion
Time Complexity: O(n)
Space Complexity: O(n)
"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderdict = {}
        for i, ele in enumerate(inorder):
            inorderdict[ele] = i

        preorderindex = 0

        def build(start,end):
            nonlocal preorderindex
            if start > end:
                return None
            val = preorder[preorderindex]
            preorderindex += 1

            node = TreeNode(val)

            mid = inorderdict[val]
            node.left = build(start, mid-1)
            node.right = build(mid+1, end)

            return node

        return build(0, len(preorder) - 1)