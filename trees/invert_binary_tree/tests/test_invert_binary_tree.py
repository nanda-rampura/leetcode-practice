import pytest
from invert_binary_tree.solution.invert_binary_tree import TreeNode, InvertBinaryTree
from collections import deque


def build_tree():
    # [4,2,7,1,3,6,9]
    return TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9)),
    )


def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # remove trailing None
    while result and result[-1] is None:
        result.pop()

    return result


def test_invert_tree():
    solution = InvertBinaryTree()
    root = build_tree()

    inverted = solution.invert_tree(root)

    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]


def test_empty_tree():
    solution = InvertBinaryTree()
    assert solution.invert_tree(None) is None