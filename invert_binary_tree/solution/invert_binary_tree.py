from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvertBinaryTree:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None

            left = node.left
            right = node.right

            node.right = dfs(left)
            node.left = dfs(right)

            return node

        return dfs(root)