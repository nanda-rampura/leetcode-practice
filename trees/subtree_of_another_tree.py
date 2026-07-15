# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SubtreeOfAnotherTree:
    """
Metadata:
    Problem: Subtree of Another Tree
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/subtree-of-another-tree/
    Pattern: DFS / Tree Comparison
    Key Idea: Traverse every node in the main tree. Whenever a node matches the subtree root value, recursively compare both trees for structural and value equality.
"""
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        def comparethetress(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False

            return comparethetress(node1.left, node2.left) and comparethetress(node1.right, node2.right)

        def dfs(node):
            if node is None:
                return False

            if node.val == subRoot.val and comparethetress(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        if not root:
            return subRoot is None

        return dfs(root)

        


            