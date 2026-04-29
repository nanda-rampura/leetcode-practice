from typing import List


class SearchInRotatedSortedArray:
    """
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Pattern: Binary Search / Rotated Array
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums) - 1
        while st <= end:
            mid = st + (end - st)//2
            print(st, mid, end)
            if nums[mid] == target:
                return mid
            # is left side sorted
            if nums[st] <= nums[mid]:
                # is the target inside left side 
                if nums[st] <= target < nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
                
            else:
                if nums[mid] < target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1

        return -1