import pytest
from prefixsum.contiguous_array import Solution


@pytest.mark.parametrize("nums, expected", [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 1, 0, 1], 4),
    ([0], 0),
    ([1], 0),
    ([0, 0, 1, 0, 0, 0, 1, 1], 6),
    ([1, 1, 1, 0, 0, 0], 6),
    ([0, 0, 0, 1, 1], 4),
])
def test_find_max_length(nums, expected):
    sol = Solution()
    assert sol.findMaxLength(nums) == expected