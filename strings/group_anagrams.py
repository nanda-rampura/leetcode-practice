from collections import defaultdict
from typing import List


class AnagramGrouper:
    """
Problem: Group Anagrams
Difficulty: Medium
LeetCode: https://leetcode.com/problems/group-anagrams/
Pattern: Hash Map / Frequency Counting
Topics: Arrays, Strings, Hash Table
Time Complexity: O(n * k)
Space Complexity: O(n * k)
"""
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for i,word in enumerate(strs):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            mapping[(tuple(freq))].append(word)
        
        results = []
        for value in mapping.values():
            results.append(value)

        return results