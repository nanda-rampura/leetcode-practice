import pytest
from collections import deque
from trees.binary_tree_level_order import BinaryTreeLevelOrder, TreeNode


class TestBinaryTreeLevelOrder:

    def build_tree(self):
        r"""
      1
    /   \
   2     3
  / \     \
 4   5     6
"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        return root

    def test_basic_tree(self):
        root = self.build_tree()
        result = BinaryTreeLevelOrder().levelOrder(root)

        assert result == [[1], [2, 3], [4, 5, 6]]
    