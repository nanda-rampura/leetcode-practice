from typing import List

class InsertInterval:
    """
Problem: Insert Interval
Difficulty: Medium
LeetCode: https://leetcode.com/problems/insert-interval/
Pattern: Intervals / Merge Intervals
"""

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        # keep adding until the insert
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1
        
        # merge the intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        results.append(newInterval)

        #append 
        while i < len(intervals):
            results.append(intervals[i])
            i += 1

        return results
        