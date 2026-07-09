# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from tests.test_max_depth_binary_tree import TreeNode


class Solution:
    """
Metadata:
    Problem: Path Sum II
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/path-sum-ii/
    Pattern: DFS / Backtracking / Tree Traversal
    Key Idea: Perform DFS while maintaining the current path and running sum. When a leaf node is reached, check if the path sum equals the target. If it does, store a copy of the current path, then backtrack to explore other paths.
"""
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        def dfs(node, sum, path):
            if not node:
               return 
            if node.left is None and node.right is None:
                path.append(node.val)
                if sum+node.val == targetSum:
                    results.append(path[:])
                path.pop()
                return

            path.append(node.val)
            dfs(node.left, sum+node.val, path) 
            dfs(node.right, sum+node.val, path)
            path.pop()
        
        dfs(root, 0, list())
        return results
