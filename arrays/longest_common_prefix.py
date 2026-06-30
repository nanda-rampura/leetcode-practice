from typing import List


class Solution:
    """
Problem: Longest Common Prefix
Difficulty: Easy
LeetCode: https://leetcode.com/problems/longest-common-prefix/

Pattern: String Matching / Horizontal Scanning

Idea:
Iteratively grow prefix from the first string and validate against all others.

Edge Case:
- Empty input list → return ""

Complexity:
Time: O(S * N)
Space: O(1)
"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefixlength = 1
        prefix = ""

        while prefixlength <= len(strs[0]):
            tempprefix = strs[0][:prefixlength]

            for i in range(1, len(strs)):
                if strs[i][:prefixlength] != tempprefix:
                    return prefix

            prefix = tempprefix
            prefixlength += 1

        return prefix