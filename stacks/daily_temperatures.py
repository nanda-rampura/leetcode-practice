from typing import List


class DailyTemperatures:
    """
    Problem: Daily Temperatures
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/daily-temperatures/
    Pattern: Monotonic Stack / Next Greater Element
    """

    git_commit_message = (
        "feat: solve daily temperatures using monotonic decreasing stack"
    )

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                answer[index] = i - index

            stack.append(i)

        return answer