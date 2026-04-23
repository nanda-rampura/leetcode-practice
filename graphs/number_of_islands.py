from typing import List


class NumIslands:
    """
Problem: Number of Islands
Difficulty: Medium
Pattern: DFS / BFS (Graph Traversal / Flood Fill)
LeetCode: https://leetcode.com/problems/number-of-islands/
"""
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row : int, col : int):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if grid[row][col] != "1":
                return
            grid[row][col] = "2"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        noofislands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    noofislands += 1
                    dfs(i,j) 
        
        return noofislands