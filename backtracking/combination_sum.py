from typing import List

class CombinationSum:
    """
    Problem: Combination Sum
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/combination-sum/
    Pattern: Backtracking (Combination / Reuse Allowed)
    Approach: Use start index and allow reuse by passing same index
    Time Complexity: O(2^n)
    Space Complexity: O(target)
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []

        def backtrack(start, total, path):
            if total == target:
                output.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i, total + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return output