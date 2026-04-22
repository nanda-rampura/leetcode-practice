import pytest
from trees.validate_binary_search_tree import ValidateBinarySearchTree, TreeNode


class TestValidateBinarySearchTree:

    def test_valid_bst(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        assert ValidateBinarySearchTree().isValidBST(root) is True


    def test_invalid_bst(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        assert ValidateBinarySearchTree().isValidBST(root) is False


    def test_single_node(self):
        root = TreeNode(1)

        assert ValidateBinarySearchTree().isValidBST(root) is True


    def test_duplicate_values(self):
        root = TreeNode(2)
        root.left = TreeNode(2)

        assert ValidateBinarySearchTree().isValidBST(root) is False


    def test_large_valid_tree(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(20)

        assert ValidateBinarySearchTree().isValidBST(root) is True