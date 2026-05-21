import pytest
from strings.group_anagrams import AnagramGrouper


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]],
        ),
        (
            ["abc", "bca", "cab", "xyz"],
            [["abc", "bca", "cab"], ["xyz"]],
        ),
    ],
)

def test_group_anagrams(strs, expected):
    solution = AnagramGrouper()

    result = solution.groupAnagrams(strs)

    normalized_result = sorted([sorted(group) for group in result])
    normalized_expected = sorted([sorted(group) for group in expected])

    assert normalized_result == normalized_expected