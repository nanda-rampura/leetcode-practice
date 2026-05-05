from trees.max_depth_binary_tree import MaxDepthBinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestMaxDepthBinaryTree:

    def build_tree(self):
        """
            1
           / \
          2   3
         /
        4
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        return root

    def test_example(self):
        sol = MaxDepthBinaryTree()
        root = self.build_tree()
        assert sol.maxDepth(root) == 3

    def test_single_node(self):
        sol = MaxDepthBinaryTree()
        root = TreeNode(1)
        assert sol.maxDepth(root) == 1

    def test_empty_tree(self):
        sol = MaxDepthBinaryTree()
        assert sol.maxDepth(None) == 0

    def test_skewed_tree(self):
        sol = MaxDepthBinaryTree()

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        assert sol.maxDepth(root) == 3