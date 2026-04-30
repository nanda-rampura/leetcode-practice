from typing import List

class Subsets:
    """
    Problem: Subsets
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/subsets/
    Pattern: Backtracking (Start Index)
    Approach: Add current subset at every recursion level
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(start, path):
            output.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return output