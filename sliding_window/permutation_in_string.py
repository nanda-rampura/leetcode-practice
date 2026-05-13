from collections import defaultdict
from typing import List


class PermutationInString:
    """
    Problem: Permutation in String
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/permutation-in-string/
    Pattern: Sliding Window / Frequency Map
    """

    git_commit_message = (
        "feat: solve permutation in string using sliding window frequency comparison"
    )

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if len(s1) > len(s2):
            return False

        p_frq = defaultdict(int)
        for j in range(k):
            p_frq[s1[j]] += 1

        window_frq = defaultdict(int)
        for j in range(k):
            window_frq[s2[j]] += 1

        if window_frq == p_frq:
            return True

        for i in range(k, len(s2)):

            left_char = s2[i - k]
            window_frq[left_char] -= 1

            if window_frq[left_char] == 0:
                del window_frq[left_char]

            window_frq[s2[i]] += 1

            if window_frq == p_frq:
                return True

        return False