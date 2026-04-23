"""
Problem: Course Schedule
Difficulty: Medium
LeetCode: https://leetcode.com/problems/course-schedule/
Pattern: Graph / Topological Sort (Kahn's Algorithm BFS)
"""

from collections import defaultdict, deque
from typing import List


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjlist = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            adjlist[b].append(a)

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for nbor in adjlist[course]:
                indegree[nbor] -= 1
                if indegree[nbor] == 0:
                    queue.append(nbor)

        return count == numCourses