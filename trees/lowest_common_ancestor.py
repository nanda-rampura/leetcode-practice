class LowestCommonAncestor:
    """
    Metadata:
        Problem: Maximum Depth of Binary Tree
        Difficulty: Easy
        LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
        Pattern: DFS / BFS / Tree Traversal
        Key Idea: Track depth while traversing tree; return maximum depth found
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