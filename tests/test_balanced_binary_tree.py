import pytest
from trees.balanced_binary_tree import BalancedBinaryTreeChecker, TreeNode


def balanced_tree():
    """
         3
        / \
       9  20
         /  \
        15   7
    """
    return TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )


def unbalanced_tree():
    """
         1
        /
       2
      /
     3
    """
    return TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(3)
        )
    )


class TestBalancedBinaryTreeChecker:

    def test_balanced_tree(self):
        root = balanced_tree()
        assert BalancedBinaryTreeChecker().isBalanced(root) is True

    def test_unbalanced_tree(self):
        root = unbalanced_tree()
        assert BalancedBinaryTreeChecker().isBalanced(root) is False

    def test_empty_tree(self):
        assert BalancedBinaryTreeChecker().isBalanced(None) is True

    def test_single_node(self):
        root = TreeNode(1)
        assert BalancedBinaryTreeChecker().isBalanced(root) is True