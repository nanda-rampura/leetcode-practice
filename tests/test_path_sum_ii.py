import pytest
from trees.path_sum_ii import Solution, TreeNode


class TestPathSumII:

    def build_tree(self):
        r"""
              5
            /   \
           4     8
          /     / \
         11    13  4
        /  \      / \
       7    2    5   1
        """
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)

        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)

        return root

    def test_path_sum_exists(self):
        root = self.build_tree()

        result = Solution().pathSum(root, 22)

        expected = [
            [5, 4, 11, 2],
            [5, 8, 4, 5]
        ]

        assert sorted(result) == sorted(expected)

    def test_empty_tree(self):
        assert Solution().pathSum(None, 22) == []

    def test_single_node_match(self):
        root = TreeNode(1)

        assert Solution().pathSum(root, 1) == [[1]]

    def test_single_node_no_match(self):
        root = TreeNode(1)

        assert Solution().pathSum(root, 2) == []

    def test_no_valid_path(self):
        root = self.build_tree()

        assert Solution().pathSum(root, 100) == []