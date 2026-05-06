from typing import List

class SortColors:
    """
    Problem: Sort Colors
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/sort-colors/
    Pattern: Two Pointers / Dutch National Flag (3-way Partition)
    """
    def sortColors(self, nums: List[int]) -> None:
        left, curr, right = 0, 0, len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1

            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1

            else:  # nums[curr] == 1
                curr += 1