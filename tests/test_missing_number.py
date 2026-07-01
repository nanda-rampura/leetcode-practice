import pytest
from bit_manipulation.missing_number import Solution


@pytest.mark.parametrize("nums, expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
    ([0], 1),
])
def test_missing_number(nums, expected):
    sol = Solution()
    assert sol.missingNumber(nums) == expected