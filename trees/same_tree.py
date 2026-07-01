from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Problem: Same Tree
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/same-tree/

    Pattern: Binary Tree / DFS / Recursion

    Approach:
    - Compare corresponding nodes recursively.
    - If both nodes are None, they are equal.
    - If one node is None or values differ, trees are not equal.
    - Recursively compare left and right subtrees.

    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        elif p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )