import pytest
from arrays.move_zeroes import Solution


def test_move_zeroes():
    sol = Solution()

    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    sol.moveZeroes(nums)
    assert nums == [0]

    nums = [1, 2, 3]
    sol.moveZeroes(nums)
    assert nums == [1, 2, 3]

    nums = [0, 0, 1]
    sol.moveZeroes(nums)
    assert nums == [1, 0, 0]