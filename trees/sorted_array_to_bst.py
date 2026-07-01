from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SortedArrayToBST:
    """
Problem: Convert Sorted Array to Binary Search Tree
Difficulty: Easy
LeetCode: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Pattern: Divide & Conquer / Recursion / Tree Construction

Approach:
- Choose middle element as root
- Recursively build left and right subtrees
- Ensures height-balanced BST

Time Complexity: O(n)
Space Complexity: O(log n) recursion stack (balanced tree)
"""
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(st, end):
            if st > end:
                return None

            mid = (st + end) // 2

            left = build(st, mid - 1)
            right = build(mid + 1, end)

            return TreeNode(nums[mid], left, right)

        return build(0, len(nums) - 1)