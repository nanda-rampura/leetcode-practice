from typing import List

class BinarySearch:
    """
Problem: Binary Search
Difficulty: Easy
LeetCode: https://leetcode.com/problems/binary-search/
Pattern: Binary Search / Divide and Conquer
"""

    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums) - 1

        while st <= end:
            mid = st + (end - st) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                st = mid + 1

        return -1