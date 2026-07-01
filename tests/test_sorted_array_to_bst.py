import pytest
from trees.sorted_array_to_bst import SortedArrayToBST, TreeNode


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


@pytest.mark.parametrize("nums", [
    [-10, -3, 0, 5, 9],
    [1, 3],
    [1],
    [],
])
def test_sorted_array_to_bst(nums):
    sol = SortedArrayToBST()
    root = sol.sortedArrayToBST(nums)

    # BST should preserve sorted order in inorder traversal
    assert inorder(root) == nums