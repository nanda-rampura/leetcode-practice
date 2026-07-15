import pytest
from trees.path_sum import PathSum, TreeNode


class TestPathSum:

    def build_tree(self):
        r"""
              5
            /   \
           4     8
          /     / \
         11    13  4
        /  \         \
       7    2         1
        """
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)

        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        return root

    def test_path_exists(self):
        root = self.build_tree()

        assert PathSum().hasPathSum(root, 22) is True

    def test_path_not_exists(self):
        root = self.build_tree()

        assert PathSum().hasPathSum(root, 100) is False

    def test_empty_tree(self):
        assert PathSum().hasPathSum(None, 0) is False

    def test_single_node_match(self):
        root = TreeNode(1)

        assert PathSum().hasPathSum(root, 1) is True

    def test_single_node_no_match(self):
        root = TreeNode(1)

        assert PathSum().hasPathSum(root, 2) is False