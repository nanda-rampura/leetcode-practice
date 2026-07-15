import pytest
from trees.subtree_of_another_tree import SubtreeOfAnotherTree, TreeNode


class TestSubtreeOfAnotherTree:

    def test_subtree_exists(self):
        r"""
                3
              /   \
             4     5
            / \
           1   2

             4
            / \
           1   2
        """
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        sub_root = TreeNode(4)
        sub_root.left = TreeNode(1)
        sub_root.right = TreeNode(2)

        assert SubtreeOfAnotherTree().isSubtree(root, sub_root) is True

    def test_subtree_not_exists(self):
        r"""
                3
              /   \
             4     5
            / \
           1   2
              /
             0

             4
            / \
           1   2
        """
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)

        sub_root = TreeNode(4)
        sub_root.left = TreeNode(1)
        sub_root.right = TreeNode(2)

        assert SubtreeOfAnotherTree().isSubtree(root, sub_root) is False

    def test_same_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        sub_root = TreeNode(1)
        sub_root.left = TreeNode(2)
        sub_root.right = TreeNode(3)

        assert SubtreeOfAnotherTree().isSubtree(root, sub_root) is True

    def test_empty_subtree(self):
        root = TreeNode(1)

        assert SubtreeOfAnotherTree().isSubtree(root, None) is True

    def test_both_empty(self):
        assert SubtreeOfAnotherTree().isSubtree(None, None) is True