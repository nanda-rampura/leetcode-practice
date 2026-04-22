# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, Tuple

from trees.invert_binary_tree import TreeNode


class BalancedBinaryTreeChecker:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursive(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0
            
            left_balanced, leftheight = recursive(node.left)
            right_balanced, rightheight = recursive(node.right)

            isbalanced = left_balanced and right_balanced and abs(leftheight - rightheight) <= 1
            height = max(leftheight, rightheight)+1
            
            return isbalanced, height

        result,_ = recursive(root)
        return result