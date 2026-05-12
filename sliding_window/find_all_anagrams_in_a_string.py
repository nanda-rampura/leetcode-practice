from collections import defaultdict
from typing import List


class FindAllAnagramsInAString:
    """
    Problem: Find All Anagrams in a String
    Difficulty: Medium
    LeetCode: https://leetcode.com/problems/find-all-anagrams-in-a-string/
    Pattern: Sliding Window / Hash Map
    """

    git_commit_message = (
        "feat: implement find all anagrams in a string using sliding window"
    )

    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        k = len(p)

        p_frq = defaultdict(int)
        for j in range(k):
            p_frq[p[j]] += 1

        window_frq = defaultdict(int)
        for j in range(k):
            window_frq[s[j]] += 1

        results = [0] if window_frq == p_frq else []

        for i in range(k, len(s)):

            left_char = s[i - k]

            window_frq[left_char] -= 1

            if window_frq[left_char] == 0:
                del window_frq[left_char]

            window_frq[s[i]] += 1

            if window_frq == p_frq:
                results.append(i - k + 1)

        return results