from sliding_window.find_all_anagrams_in_a_string import (
    FindAllAnagramsInAString,
)


class TestFindAllAnagramsInAString:

    def test_example_1(self):
        s = "cbaebabacd"
        p = "abc"

        result = FindAllAnagramsInAString().findAnagrams(s, p)

        assert result == [0, 6]

    def test_example_2(self):
        s = "abab"
        p = "ab"

        result = FindAllAnagramsInAString().findAnagrams(s, p)

        assert result == [0, 1, 2]

    def test_no_anagram(self):
        s = "abcdefg"
        p = "hij"

        result = FindAllAnagramsInAString().findAnagrams(s, p)

        assert result == []

    def test_pattern_larger_than_string(self):
        s = "ab"
        p = "abcd"

        result = FindAllAnagramsInAString().findAnagrams(s, p)

        assert result == []

    def test_single_character_match(self):
        s = "a"
        p = "a"

        result = FindAllAnagramsInAString().findAnagrams(s, p)

        assert result == [0]