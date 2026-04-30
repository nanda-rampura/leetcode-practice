from typing import List

class Permutations:
    """
    Problem: Permutations
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/permutations/
    Pattern: Backtracking (Used Array)
    Approach: Use used[] to track visited elements
    Time Complexity: O(n * n!)
    Space Complexity: O(n)
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                output.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return output