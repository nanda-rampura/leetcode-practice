from typing import List

class Flood_Fill:
    """
Problem: Flood Fill
Difficulty: Easy
LeetCode: https://leetcode.com/problems/flood-fill/
Pattern: DFS / BFS (Graph Traversal)
"""
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]

        def dfs(r: int, c: int):
            if (0 <= r < rows and 
                0 <= c < cols and 
                image[r][c] == original):
                
                image[r][c] = color

                dfs(r-1, c)  # top
                dfs(r+1, c)  # bottom
                dfs(r, c-1)  # left
                dfs(r, c+1)  # right

        dfs(sr, sc)
        return image