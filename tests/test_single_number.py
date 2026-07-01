import pytest
from bit_manipulation.single_number import Solution


@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
    ([7, 7, 8], 8),
])
def test_single_number(nums, expected):
    sol = Solution()
    assert sol.singleNumber(nums) == expected