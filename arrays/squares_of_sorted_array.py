from typing import List


class SquaresOfSortedArray:
    """
Metadata:
    Problem: Squares of a Sorted Array
    Difficulty: Easy
    LeetCode: https://leetcode.com/problems/squares-of-a-sorted-array/
    Pattern: Two Pointers
    Key Idea: The largest square will come from either the leftmost negative number or the rightmost positive number. Compare both ends and place the larger square at the end of the result array, moving inward.
"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredsorted = [0] * len(nums)
        index = len(nums) - 1
        st = 0
        end = len(nums) - 1

        while st <= end:
            statproduct = nums[st] * nums[st]
            endproduct =  nums[end] * nums[end]
            if statproduct > endproduct:
                squaredsorted[index] = statproduct
                st += 1
            else:
                squaredsorted[index] = endproduct
                end -= 1
            index -= 1
        return squaredsorted