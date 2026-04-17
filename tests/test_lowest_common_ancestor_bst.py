from trees.lowest_common_ancestor_bst import LowestCommonAncestorBST, TreeNode


def build_tree():
    r"""
          6
        /   \
       2     8
      / \   / \
     0   4 7   9
        / \
       3   5
    """
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    return root


def test_lca_root():
    root = build_tree()
    p = root.left  # 2
    q = root.right  # 8

    result = LowestCommonAncestorBST().lowestCommonAncestor(root, p, q)
    assert result.val == 6


def test_lca_subtree():
    root = build_tree()
    p = root.left  # 2
    q = root.left.right  # 4

    result = LowestCommonAncestorBST().lowestCommonAncestor(root, p, q)
    assert result.val == 2


def test_lca_parent_child():
    root = build_tree()
    p = root.left.right.left  # 3
    q = root.left.right.right  # 5

    result = LowestCommonAncestorBST().lowestCommonAncestor(root, p, q)
    assert result.val == 4


def test_small_tree():
    root = TreeNode(2)
    root.left = TreeNode(1)

    p = root
    q = root.left

    result = LowestCommonAncestorBST().lowestCommonAncestor(root, p, q)
    assert result.val == 2