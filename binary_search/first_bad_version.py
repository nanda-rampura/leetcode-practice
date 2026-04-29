bad = 4  # simulate first bad version

def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    """
Problem: First Bad Version
Difficulty: Easy
Pattern: Binary Search / Boundary (First True)
LeetCode: https://leetcode.com/problems/first-bad-version/
"""
    def firstBadVersion(self, n: int) -> int:
        st = 1
        end = n
        while st < end:
            mid = st + (end - st) // 2
            if isBadVersion(mid):
                end = mid
            else:
                st = mid + 1
        return st


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstBadVersion(5))  # Expected: 4