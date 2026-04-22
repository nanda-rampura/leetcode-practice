import pytest
from strings.longest_substring_without_repeating_characters import LongestSubstringWithoutRepeatingCharacters


class TestLongestSubstringWithoutRepeatingCharacters:

    def test_basic(self):
        sol = LongestSubstringWithoutRepeatingCharacters()
        assert sol.lengthOfLongestSubstring("abcabcbb") == 3

    def test_all_same_chars(self):
        sol = LongestSubstringWithoutRepeatingCharacters()
        assert sol.lengthOfLongestSubstring("bbbbb") == 1

    def test_mixed_case(self):
        sol = LongestSubstringWithoutRepeatingCharacters()
        assert sol.lengthOfLongestSubstring("pwwkew") == 3

    def test_empty_string(self):
        sol = LongestSubstringWithoutRepeatingCharacters()
        assert sol.lengthOfLongestSubstring("") == 0

    def test_single_char(self):
        sol = LongestSubstringWithoutRepeatingCharacters()
        assert sol.lengthOfLongestSubstring("a") == 1

    def test_no_repeats(self):
        sol = LongestSubstringWithoutRepeatingCharacters()
        assert sol.lengthOfLongestSubstring("abcdef") == 6