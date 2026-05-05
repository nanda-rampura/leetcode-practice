class LowestCommonAncestor:
    """
    Metadata:
        Problem: Lowest Common Ancestor of a Binary Tree
        Difficulty: Medium
        LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
        Pattern: DFS / Post-order Traversal / Tree Recursion
        Key Idea: Return target node upward; split point is LCA
    """
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left if left else right

        return dfs(root)