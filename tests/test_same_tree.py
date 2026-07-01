import pytest
from trees.same_tree import Solution, TreeNode


def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]

    for i in range(len(values)):
        if nodes[i] is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(values):
            nodes[i].left = nodes[left]
        if right < len(values):
            nodes[i].right = nodes[right]

    return nodes[0]


@pytest.mark.parametrize("p, q, expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([], [], True),
])
def test_same_tree(p, q, expected):
    sol = Solution()
    assert sol.isSameTree(build_tree(p), build_tree(q)) == expected