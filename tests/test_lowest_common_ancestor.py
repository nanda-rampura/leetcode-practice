from trees.lowest_common_ancestor import LowestCommonAncestor


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLowestCommonAncestor:

    def setup_tree(self):
        """
            3
           / \
          5   1
         / \ / \
        6  2 0  8
          / \
         7   4
        """
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)

        return root

    def test_lca_same_subtree(self):
        sol = LowestCommonAncestor()
        root = self.setup_tree()

        p = root.left          # 5
        q = root.left.right    # 2

        assert sol.lowestCommonAncestor(root, p, q).val == 5

    def test_lca_different_subtrees(self):
        sol = LowestCommonAncestor()
        root = self.setup_tree()

        p = root.left          # 5
        q = root.right         # 1

        assert sol.lowestCommonAncestor(root, p, q).val == 3

    def test_lca_deep_nodes(self):
        sol = LowestCommonAncestor()
        root = self.setup_tree()

        p = root.left.right.left   # 7
        q = root.left.right.right  # 4

        assert sol.lowestCommonAncestor(root, p, q).val == 2