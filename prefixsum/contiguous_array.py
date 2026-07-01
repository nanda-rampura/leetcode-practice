from typing import List


class Solution:
    """
Problem: Contiguous Array
Difficulty: Medium
LeetCode: https://leetcode.com/problems/contiguous-array/

Pattern: Prefix Sum + Hash Map

Approach:
- Treat 0 as -1 and 1 as +1.
- Compute a running prefix sum while traversing the array.
- Store the first occurrence of each prefix sum in a hash map.
- When the same prefix sum appears again, the subarray between the two indices has an equal number of 0s and 1s.
- Track the maximum length of such subarrays.

Time Complexity: O(n)
Space Complexity: O(n)
"""
    def findMaxLength(self, nums: List[int]) -> int:
        prefixsummap = {0 : -1}        
        maxlength = 0
        currsum = 0
        for i, num in enumerate(nums):
            currsum += -1 if num == 0 else 1
            if currsum in prefixsummap:
                maxlength = max(maxlength, i - prefixsummap[currsum])
            else:
                prefixsummap[currsum] = i
        
        return maxlength

