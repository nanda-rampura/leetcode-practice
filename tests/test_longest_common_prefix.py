import pytest
from arrays.longest_common_prefix import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["throne", "throne"], "throne"),
        ([""], ""),
        (["a"], "a"),
        (["ab", "a"], "a"),
        (["prefix", "prefix"], "prefix"),
    ],
)
def test_longest_common_prefix(strs, expected):
    assert Solution().longestCommonPrefix(strs) == expected