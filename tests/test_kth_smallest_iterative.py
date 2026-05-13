from trees.kth_smallest_iterative import KthSmallestBST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestKthSmallestBST:

    def build_tree(self):
        """
              3
             / \
            1   4
             \
              2
        """
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        return root

    def test_kth_smallest_1(self):
        root = self.build_tree()
        assert KthSmallestBST().kthSmallest(root, 1) == 1

    def test_kth_smallest_2(self):
        root = self.build_tree()
        assert KthSmallestBST().kthSmallest(root, 2) == 2

    def test_kth_smallest_3(self):
        root = self.build_tree()
        assert KthSmallestBST().kthSmallest(root, 3) == 3

    def test_kth_smallest_4(self):
        root = self.build_tree()
        assert KthSmallestBST().kthSmallest(root, 4) == 4