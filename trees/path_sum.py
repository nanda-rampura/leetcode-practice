# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tests.test_kth_smallest_iterative import TreeNode


class PathSum:
    """
Metadata:
    Problem: Path Sum
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/path-sum/
    Pattern: DFS / Tree Traversal
    Key Idea: Traverse every root-to-leaf path while maintaining a running sum. At each leaf node, compare the accumulated sum with the target sum.
"""
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum):
            if not node: 
                return False          
            if node.left is None and node.right is None:
                return (sum+node.val) == targetSum

            return dfs(node.left, sum+node.val) or dfs(node.right, sum+node.val)
        
        if not root:
            return False

        return dfs(root, 0)
