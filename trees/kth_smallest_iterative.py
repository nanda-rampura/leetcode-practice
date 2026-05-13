from typing import Optional

from trees.invert_binary_tree import TreeNode


class KthSmallestBST:
    """
Problem: Kth Smallest Element in a BST
Difficulty: Medium
LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Pattern: Iterative Inorder Traversal / Stack
Key Idea: Simulate inorder traversal using stack and decrement k on each visit
"""
    def kthSmallest(self, root: Optional["TreeNode"], k: int) -> int:
        stack = []
        curr = root

        while True:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right