import pytest
from trees.symmetric_tree import Solution, TreeNode


def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]

    for i, node in enumerate(nodes):
        if node is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]

    return nodes[0]


@pytest.mark.parametrize("values, expected", [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
    ([1], True),
    ([], True),
    ([1, 2, 2, None, 3, 3, None], True),
])
def test_is_symmetric(values, expected):
    sol = Solution()
    root = build_tree(values)
    assert sol.isSymmetric(root) == expected