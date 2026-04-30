# tests/test_binary_tree_right_side_view.py

from trees.binary_tree_right_side_view import BinaryTreeRightSideView, TreeNode


def build_tree(values):
    """Build tree from level-order list (None allowed)"""
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


def test_basic():
    sol = BinaryTreeRightSideView()
    root = build_tree([1, 2, 3, None, 5, None, 4])
    assert sol.rightSideView(root) == [1, 3, 4]


def test_single_node():
    sol = BinaryTreeRightSideView()
    root = build_tree([1])
    assert sol.rightSideView(root) == [1]


def test_empty():
    sol = BinaryTreeRightSideView()
    assert sol.rightSideView(None) == []