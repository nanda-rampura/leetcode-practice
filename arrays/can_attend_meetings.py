from typing import List


class MeetingScheduler:
    """
Problem: Meeting Rooms (Can Attend Meetings)
Difficulty: Easy
LeetCode: https://leetcode.com/problems/meeting-rooms/
Pattern: Intervals / Sorting / Greedy
Topics: Sorting, Greedy, Arrays
Time Complexity: O(n log n)
Space Complexity: O(1)
Key Idea: Sort by start time and check for overlap between adjacent intervals
"""
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x : x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True