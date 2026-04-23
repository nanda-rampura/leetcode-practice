from typing import List


class MergeIntervals:
    """
Problem: Merge Intervals
Difficulty: Medium
Pattern: Sorting + Greedy / Interval Merging
LeetCode: https://leetcode.com/problems/merge-intervals/
"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        results = []
        results.append(intervals[0])
        for interval in intervals[1:]:
            #merge 
            if results[-1][1] >= interval[0]:
                results[-1][1] = max(results[-1][1], interval[1])
            else:
                results.append(interval)
        
        return results

